#!/usr/bin/env python3

import connexion
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from flask import request
from swagger_server import encoder
import random
import time
import logging
import requests
from logging.handlers import HTTPHandler
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = connexion.App(__name__, specification_dir='./swagger/')

REQUEST_COUNT = Counter('request_count', 'Общее количество запросов',
                        ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Время обработки запроса',
                            ['method', 'endpoint'])
ERROR_COUNT = Counter('error_count', 'Количество ошибок', ['method', 'endpoint', 'http_status'])

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer_provider().get_tracer(__name__)
otlp_exporter = OTLPSpanExporter(endpoint="http://tempo:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

FlaskInstrumentor().instrument_app(app.app)

class LokiHandler(HTTPHandler):
    def __init__(self, url):
        self.url = url
        super().__init__(host='', url=url, method='POST')

    def emit(self, record):
        log_entry = self.format(record)
        payload = {
            "streams": [
                {
                    "stream": {"job": "flask-api", "level": record.levelname},
                    "values": [[str(int(time.time() * 1000000000)), log_entry]]
                }
            ]
        }
        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            app.app.logger.error(f"Failed to send log entry to Loki: {e}")

loki_url = "http://loki:3100/loki/api/v1/push"

loki_handler = LokiHandler(loki_url)
loki_handler.setLevel(logging.INFO)
loki_formatter = logging.Formatter('%(asctime)s - %(message)s')
loki_handler.setFormatter(loki_formatter)

app.app.logger.addHandler(loki_handler)
app.app.logger.setLevel(logging.INFO)

@app.app.route("/trace-example")
def trace_example():
    with tracer.start_as_current_span("example-span"):
        time.sleep(random.uniform(0.1, 0.5))
        return "Trace example!"

@app.app.route('/metrics')

def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

def start_timer():
    request.start_time = time.time()

def record_metrics(response):
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path, http_status=response.status_code).inc()

    if hasattr(request, 'start_time'):
        latency = time.time() - request.start_time
        latency_histogram = REQUEST_LATENCY.labels(method=request.method, endpoint=request.path)
        latency_histogram.observe(latency)

    if response.status_code >= 400:
        ERROR_COUNT.labels(method=request.method, endpoint=request.path, http_status=response.status_code).inc()
        app.app.logger.error(f"Request {request.method} to {request.path} failed with status {response.status_code}")
    else:
        app.app.logger.info(f"Request {request.method} to {request.path} succeeded with status {response.status_code}")

    return response

def main():
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Movie Rental API'}, pythonic_params=True)

    app.app.before_request(start_timer)
    app.app.after_request(record_metrics)

    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()
