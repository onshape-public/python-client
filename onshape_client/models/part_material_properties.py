# coding: utf-8

"""
    Onshape API

    Onshape API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ekeller@onshape.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PartMaterialProperties(object):
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
        'units': 'str',
        'name': 'str',
        'value': 'float',
        'description': 'str'
    }

    attribute_map = {
        'units': 'units',
        'name': 'name',
        'value': 'value',
        'description': 'description'
    }

    def __init__(self, units=None, name=None, value=None, description=None):  # noqa: E501
        """PartMaterialProperties - a model defined in Swagger"""  # noqa: E501

        self._units = None
        self._name = None
        self._value = None
        self._description = None
        self.discriminator = None

        if units is not None:
            self.units = units
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if description is not None:
            self.description = description

    @property
    def units(self):
        """Gets the units of this PartMaterialProperties.  # noqa: E501

        Units of the material property value  # noqa: E501

        :return: The units of this PartMaterialProperties.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this PartMaterialProperties.

        Units of the material property value  # noqa: E501

        :param units: The units of this PartMaterialProperties.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def name(self):
        """Gets the name of this PartMaterialProperties.  # noqa: E501

        Material property name  # noqa: E501

        :return: The name of this PartMaterialProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartMaterialProperties.

        Material property name  # noqa: E501

        :param name: The name of this PartMaterialProperties.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this PartMaterialProperties.  # noqa: E501

        Material property value  # noqa: E501

        :return: The value of this PartMaterialProperties.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PartMaterialProperties.

        Material property value  # noqa: E501

        :param value: The value of this PartMaterialProperties.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def description(self):
        """Gets the description of this PartMaterialProperties.  # noqa: E501

        Material property description  # noqa: E501

        :return: The description of this PartMaterialProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PartMaterialProperties.

        Material property description  # noqa: E501

        :param description: The description of this PartMaterialProperties.  # noqa: E501
        :type: str
        """

        self._description = description

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PartMaterialProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
