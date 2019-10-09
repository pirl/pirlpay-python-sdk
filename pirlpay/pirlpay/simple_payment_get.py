# coding: utf-8

"""
    PirlPay API

    The PirlPay API for automated payment processing  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@pirl.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SimplePaymentGet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'date_transaction': 'datetime',
        'amount': 'str',
        'pending': 'bool',
        'cancelled': 'bool',
        'pirl_amount': 'float'
    }

    attribute_map = {
        'id': 'id',
        'date_transaction': 'date_transaction',
        'amount': 'amount',
        'pending': 'pending',
        'cancelled': 'cancelled',
        'pirl_amount': 'pirl_amount'
    }

    def __init__(self, id=None, date_transaction=None, amount=None, pending=None, cancelled=None, pirl_amount=None):  # noqa: E501
        """SimplePaymentGet - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._date_transaction = None
        self._amount = None
        self._pending = None
        self._cancelled = None
        self._pirl_amount = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if date_transaction is not None:
            self.date_transaction = date_transaction
        if amount is not None:
            self.amount = amount
        if pending is not None:
            self.pending = pending
        if cancelled is not None:
            self.cancelled = cancelled
        if pirl_amount is not None:
            self.pirl_amount = pirl_amount

    @property
    def id(self):
        """Gets the id of this SimplePaymentGet.  # noqa: E501


        :return: The id of this SimplePaymentGet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimplePaymentGet.


        :param id: The id of this SimplePaymentGet.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def date_transaction(self):
        """Gets the date_transaction of this SimplePaymentGet.  # noqa: E501

        the datetime the transaction was billed  # noqa: E501

        :return: The date_transaction of this SimplePaymentGet.  # noqa: E501
        :rtype: datetime
        """
        return self._date_transaction

    @date_transaction.setter
    def date_transaction(self, date_transaction):
        """Sets the date_transaction of this SimplePaymentGet.

        the datetime the transaction was billed  # noqa: E501

        :param date_transaction: The date_transaction of this SimplePaymentGet.  # noqa: E501
        :type: datetime
        """

        self._date_transaction = date_transaction

    @property
    def amount(self):
        """Gets the amount of this SimplePaymentGet.  # noqa: E501

        how much was billed for the user in FIAT  # noqa: E501

        :return: The amount of this SimplePaymentGet.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SimplePaymentGet.

        how much was billed for the user in FIAT  # noqa: E501

        :param amount: The amount of this SimplePaymentGet.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def pending(self):
        """Gets the pending of this SimplePaymentGet.  # noqa: E501

        pending reception of the subscriber funds  # noqa: E501

        :return: The pending of this SimplePaymentGet.  # noqa: E501
        :rtype: bool
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this SimplePaymentGet.

        pending reception of the subscriber funds  # noqa: E501

        :param pending: The pending of this SimplePaymentGet.  # noqa: E501
        :type: bool
        """

        self._pending = pending

    @property
    def cancelled(self):
        """Gets the cancelled of this SimplePaymentGet.  # noqa: E501

        whether this payment is cancelled or not  # noqa: E501

        :return: The cancelled of this SimplePaymentGet.  # noqa: E501
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this SimplePaymentGet.

        whether this payment is cancelled or not  # noqa: E501

        :param cancelled: The cancelled of this SimplePaymentGet.  # noqa: E501
        :type: bool
        """

        self._cancelled = cancelled

    @property
    def pirl_amount(self):
        """Gets the pirl_amount of this SimplePaymentGet.  # noqa: E501


        :return: The pirl_amount of this SimplePaymentGet.  # noqa: E501
        :rtype: float
        """
        return self._pirl_amount

    @pirl_amount.setter
    def pirl_amount(self, pirl_amount):
        """Sets the pirl_amount of this SimplePaymentGet.


        :param pirl_amount: The pirl_amount of this SimplePaymentGet.  # noqa: E501
        :type: float
        """

        self._pirl_amount = pirl_amount

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SimplePaymentGet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SimplePaymentGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
