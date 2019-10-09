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


class SimplePayment(object):
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
        'amount': 'str'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount'
    }

    def __init__(self, id=None, amount=None):  # noqa: E501
        """SimplePayment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if amount is not None:
            self.amount = amount

    @property
    def id(self):
        """Gets the id of this SimplePayment.  # noqa: E501


        :return: The id of this SimplePayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimplePayment.


        :param id: The id of this SimplePayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this SimplePayment.  # noqa: E501

        how much was billed for the user in FIAT  # noqa: E501

        :return: The amount of this SimplePayment.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SimplePayment.

        how much was billed for the user in FIAT  # noqa: E501

        :param amount: The amount of this SimplePayment.  # noqa: E501
        :type: str
        """

        self._amount = amount

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
        if issubclass(SimplePayment, dict):
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
        if not isinstance(other, SimplePayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
