# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SettleBill(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, bill_index: int=None, _date: date=None):  # noqa: E501
        """SettleBill - a model defined in Swagger

        :param bill_index: The bill_index of this SettleBill.  # noqa: E501
        :type bill_index: int
        :param _date: The _date of this SettleBill.  # noqa: E501
        :type _date: date
        """
        self.swagger_types = {
            'bill_index': int,
            '_date': date
        }

        self.attribute_map = {
            'bill_index': 'billIndex',
            '_date': 'date'
        }

        self._bill_index = bill_index
        self.__date = _date

    @classmethod
    def from_dict(cls, dikt) -> 'SettleBill':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SettleBill of this SettleBill.  # noqa: E501
        :rtype: SettleBill
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bill_index(self) -> int:
        """Gets the bill_index of this SettleBill.


        :return: The bill_index of this SettleBill.
        :rtype: int
        """
        return self._bill_index

    @bill_index.setter
    def bill_index(self, bill_index: int):
        """Sets the bill_index of this SettleBill.


        :param bill_index: The bill_index of this SettleBill.
        :type bill_index: int
        """

        self._bill_index = bill_index

    @property
    def _date(self) -> date:
        """Gets the _date of this SettleBill.


        :return: The _date of this SettleBill.
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date: date):
        """Sets the _date of this SettleBill.


        :param _date: The _date of this SettleBill.
        :type _date: date
        """

        self.__date = _date
