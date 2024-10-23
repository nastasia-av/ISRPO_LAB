# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RentalRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, movie_id: str=None, user_id: str=None):  # noqa: E501
        """RentalRequest - a model defined in Swagger

        :param movie_id: The movie_id of this RentalRequest.  # noqa: E501
        :type movie_id: str
        :param user_id: The user_id of this RentalRequest.  # noqa: E501
        :type user_id: str
        """
        self.swagger_types = {
            'movie_id': str,
            'user_id': str
        }

        self.attribute_map = {
            'movie_id': 'movieId',
            'user_id': 'userId'
        }
        self._movie_id = movie_id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'RentalRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RentalRequest of this RentalRequest.  # noqa: E501
        :rtype: RentalRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def movie_id(self) -> str:
        """Gets the movie_id of this RentalRequest.

        ID фильма для аренды  # noqa: E501

        :return: The movie_id of this RentalRequest.
        :rtype: str
        """
        return self._movie_id

    @movie_id.setter
    def movie_id(self, movie_id: str):
        """Sets the movie_id of this RentalRequest.

        ID фильма для аренды  # noqa: E501

        :param movie_id: The movie_id of this RentalRequest.
        :type movie_id: str
        """
        if movie_id is None:
            raise ValueError("Invalid value for `movie_id`, must not be `None`")  # noqa: E501

        self._movie_id = movie_id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this RentalRequest.

        ID пользователя, который арендует фильм  # noqa: E501

        :return: The user_id of this RentalRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this RentalRequest.

        ID пользователя, который арендует фильм  # noqa: E501

        :param user_id: The user_id of this RentalRequest.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id