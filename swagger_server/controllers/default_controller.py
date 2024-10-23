import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.models.payment_request import PaymentRequest  # noqa: E501
from swagger_server.models.rental import Rental  # noqa: E501
from swagger_server.models.rental_request import RentalRequest  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_registration import UserRegistration  # noqa: E501
from swagger_server import util


def movies_get(genre=None, release_year=None):  # noqa: E501
    """Получить список доступных фильмов

    Возвращает список фильмов, доступных для аренды. # noqa: E501

    :param genre: Фильтр по жанру
    :type genre: str
    :param release_year: Фильтр по году выпуска
    :type release_year: int

    :rtype: List[Movie]
    """
    return 'do some magic!'


def movies_movie_id_delete(movie_id):  # noqa: E501
    """Удалить фильм

    Удаляет фильм по его ID. # noqa: E501

    :param movie_id: 
    :type movie_id: str

    :rtype: None
    """
    return 'do some magic!'


def movies_movie_id_get(movie_id):  # noqa: E501
    """Получить детали фильма

    Возвращает подробную информацию о фильме по его ID. # noqa: E501

    :param movie_id: 
    :type movie_id: str

    :rtype: Movie
    """
    return 'do some magic!'


def movies_movie_id_put(body, movie_id):  # noqa: E501
    """Обновить детали фильма

    Обновляет информацию о фильме по его ID. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param movie_id: 
    :type movie_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def movies_post(body):  # noqa: E501
    """Добавить новый фильм

    Добавляет новый фильм в каталог. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def payments_post(body):  # noqa: E501
    """Провести платеж

    Провести платеж за аренду фильма. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = PaymentRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def rentals_get(user_id=None):  # noqa: E501
    """Получить список активных аренд

    Возвращает список фильмов, которые в данный момент находятся в аренде. # noqa: E501

    :param user_id: Фильтр аренд по пользователю
    :type user_id: str

    :rtype: List[Rental]
    """
    return 'do some magic!'


def rentals_post(body):  # noqa: E501
    """Арендовать фильм

    Арендовать фильм, указав детали пользователя и фильма. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = RentalRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def rentals_rental_id_delete(rental_id):  # noqa: E501
    """Вернуть фильм

    Отмечает аренду как завершенную и удаляет запись. # noqa: E501

    :param rental_id: 
    :type rental_id: str

    :rtype: None
    """
    return 'do some magic!'


def rentals_rental_id_get(rental_id):  # noqa: E501
    """Получить детали аренды

    Возвращает детали конкретной аренды по её ID. # noqa: E501

    :param rental_id: 
    :type rental_id: str

    :rtype: Rental
    """
    return 'do some magic!'


def users_get():  # noqa: E501
    """Получить список пользователей

    Возвращает список зарегистрированных пользователей. # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Зарегистрировать нового пользователя

    Регистрирует нового пользователя в системе. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserRegistration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_rentals_get(user_id):  # noqa: E501
    """Получить историю аренд пользователя

    Возвращает список всех аренд, сделанных конкретным пользователем. # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: List[Rental]
    """
    return 'do some magic!'
