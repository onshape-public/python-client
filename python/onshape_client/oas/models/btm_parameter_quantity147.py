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


class BTMParameterQuantity147(object):
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
        'units': 'str',
        'is_integer': 'bool',
        'expression': 'str',
        'value': 'float'
    }

    attribute_map = {
        'units': 'units',
        'is_integer': 'isInteger',
        'expression': 'expression',
        'value': 'value'
    }

    discriminator_value_class_map = {
        'BTMParameterNullableQuantity-807': 'BTMParameterNullableQuantity807'
    }

    def __init__(self, units=None, is_integer=None, expression=None, value=None, local_vars_configuration=None):  # noqa: E501
        """BTMParameterQuantity147 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._units = None
        self._is_integer = None
        self._expression = None
        self._value = None
        self.discriminator = 'type'

        if units is not None:
            self.units = units
        if is_integer is not None:
            self.is_integer = is_integer
        if expression is not None:
            self.expression = expression
        if value is not None:
            self.value = value

    @property
    def units(self):
        """Gets the units of this BTMParameterQuantity147.  # noqa: E501


        :return: The units of this BTMParameterQuantity147.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this BTMParameterQuantity147.


        :param units: The units of this BTMParameterQuantity147.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def is_integer(self):
        """Gets the is_integer of this BTMParameterQuantity147.  # noqa: E501


        :return: The is_integer of this BTMParameterQuantity147.  # noqa: E501
        :rtype: bool
        """
        return self._is_integer

    @is_integer.setter
    def is_integer(self, is_integer):
        """Sets the is_integer of this BTMParameterQuantity147.


        :param is_integer: The is_integer of this BTMParameterQuantity147.  # noqa: E501
        :type: bool
        """

        self._is_integer = is_integer

    @property
    def expression(self):
        """Gets the expression of this BTMParameterQuantity147.  # noqa: E501


        :return: The expression of this BTMParameterQuantity147.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this BTMParameterQuantity147.


        :param expression: The expression of this BTMParameterQuantity147.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def value(self):
        """Gets the value of this BTMParameterQuantity147.  # noqa: E501


        :return: The value of this BTMParameterQuantity147.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTMParameterQuantity147.


        :param value: The value of this BTMParameterQuantity147.  # noqa: E501
        :type: float
        """

        self._value = value

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, BTMParameterQuantity147):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMParameterQuantity147):
            return True

        return self.to_dict() != other.to_dict()
