# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.models.payment_request import PaymentRequest  # noqa: E501
from swagger_server.models.rental import Rental  # noqa: E501
from swagger_server.models.rental_request import RentalRequest  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_registration import UserRegistration  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_movies_get(self):
        """Test case for movies_get

        Получить список доступных фильмов
        """
        query_string = [('genre', 'genre_example'),
                        ('release_year', 56)]
        response = self.client.open(
            '/movies',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_movies_movie_id_delete(self):
        """Test case for movies_movie_id_delete

        Удалить фильм
        """
        response = self.client.open(
            '/movies/{movieId}'.format(movie_id='movie_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_movies_movie_id_get(self):
        """Test case for movies_movie_id_get

        Получить детали фильма
        """
        response = self.client.open(
            '/movies/{movieId}'.format(movie_id='movie_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_movies_movie_id_put(self):
        """Test case for movies_movie_id_put

        Обновить детали фильма
        """
        body = Movie()
        response = self.client.open(
            '/movies/{movieId}'.format(movie_id='movie_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_movies_post(self):
        """Test case for movies_post

        Добавить новый фильм
        """
        body = Movie()
        response = self.client.open(
            '/movies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_payments_post(self):
        """Test case for payments_post

        Провести платеж
        """
        body = PaymentRequest()
        response = self.client.open(
            '/payments',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rentals_get(self):
        """Test case for rentals_get

        Получить список активных аренд
        """
        query_string = [('user_id', 'user_id_example')]
        response = self.client.open(
            '/rentals',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rentals_post(self):
        """Test case for rentals_post

        Арендовать фильм
        """
        body = RentalRequest()
        response = self.client.open(
            '/rentals',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rentals_rental_id_delete(self):
        """Test case for rentals_rental_id_delete

        Вернуть фильм
        """
        response = self.client.open(
            '/rentals/{rentalId}'.format(rental_id='rental_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rentals_rental_id_get(self):
        """Test case for rentals_rental_id_get

        Получить детали аренды
        """
        response = self.client.open(
            '/rentals/{rentalId}'.format(rental_id='rental_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Получить список пользователей
        """
        response = self.client.open(
            '/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Зарегистрировать нового пользователя
        """
        body = UserRegistration()
        response = self.client.open(
            '/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_rentals_get(self):
        """Test case for users_user_id_rentals_get

        Получить историю аренд пользователя
        """
        response = self.client.open(
            '/users/{userId}/rentals'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
