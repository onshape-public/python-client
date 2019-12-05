# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.107
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onshape_client.oas.configuration import Configuration


class NextCharge(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'current_period_end': 'datetime',
        'interval': 'str',
        'amount': 'int',
        'total': 'int'
    }

    attribute_map = {
        'current_period_end': 'currentPeriodEnd',
        'interval': 'interval',
        'amount': 'amount',
        'total': 'total'
    }

    def __init__(self, current_period_end=None, interval=None, amount=None, total=None, local_vars_configuration=None):  # noqa: E501
        """NextCharge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_period_end = None
        self._interval = None
        self._amount = None
        self._total = None
        self.discriminator = None

        if current_period_end is not None:
            self.current_period_end = current_period_end
        if interval is not None:
            self.interval = interval
        if amount is not None:
            self.amount = amount
        if total is not None:
            self.total = total

    @property
    def current_period_end(self):
        """Gets the current_period_end of this NextCharge.  # noqa: E501


        :return: The current_period_end of this NextCharge.  # noqa: E501
        :rtype: datetime
        """
        return self._current_period_end

    @current_period_end.setter
    def current_period_end(self, current_period_end):
        """Sets the current_period_end of this NextCharge.


        :param current_period_end: The current_period_end of this NextCharge.  # noqa: E501
        :type: datetime
        """

        self._current_period_end = current_period_end

    @property
    def interval(self):
        """Gets the interval of this NextCharge.  # noqa: E501


        :return: The interval of this NextCharge.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this NextCharge.


        :param interval: The interval of this NextCharge.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def amount(self):
        """Gets the amount of this NextCharge.  # noqa: E501


        :return: The amount of this NextCharge.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this NextCharge.


        :param amount: The amount of this NextCharge.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def total(self):
        """Gets the total of this NextCharge.  # noqa: E501


        :return: The total of this NextCharge.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NextCharge.


        :param total: The total of this NextCharge.  # noqa: E501
        :type: int
        """

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NextCharge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NextCharge):
            return True

        return self.to_dict() != other.to_dict()
