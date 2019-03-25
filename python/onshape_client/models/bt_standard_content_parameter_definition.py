# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTStandardContentParameterDefinition(object):
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
        'default_value': 'str',
        'display_name': 'str',
        'parameter_id': 'str',
        'visible': 'bool',
        'is_custom_parameter': 'bool',
        'is_driving_configuration': 'bool'
    }

    attribute_map = {
        'default_value': 'defaultValue',
        'display_name': 'displayName',
        'parameter_id': 'parameterId',
        'visible': 'visible',
        'is_custom_parameter': 'isCustomParameter',
        'is_driving_configuration': 'isDrivingConfiguration'
    }

    def __init__(self, default_value=None, display_name=None, parameter_id=None, visible=None, is_custom_parameter=None, is_driving_configuration=None):  # noqa: E501
        """BTStandardContentParameterDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._default_value = None
        self._display_name = None
        self._parameter_id = None
        self._visible = None
        self._is_custom_parameter = None
        self._is_driving_configuration = None
        self.discriminator = None

        if default_value is not None:
            self.default_value = default_value
        if display_name is not None:
            self.display_name = display_name
        if parameter_id is not None:
            self.parameter_id = parameter_id
        if visible is not None:
            self.visible = visible
        if is_custom_parameter is not None:
            self.is_custom_parameter = is_custom_parameter
        if is_driving_configuration is not None:
            self.is_driving_configuration = is_driving_configuration

    @property
    def default_value(self):
        """Gets the default_value of this BTStandardContentParameterDefinition.  # noqa: E501


        :return: The default_value of this BTStandardContentParameterDefinition.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this BTStandardContentParameterDefinition.


        :param default_value: The default_value of this BTStandardContentParameterDefinition.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def display_name(self):
        """Gets the display_name of this BTStandardContentParameterDefinition.  # noqa: E501


        :return: The display_name of this BTStandardContentParameterDefinition.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BTStandardContentParameterDefinition.


        :param display_name: The display_name of this BTStandardContentParameterDefinition.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def parameter_id(self):
        """Gets the parameter_id of this BTStandardContentParameterDefinition.  # noqa: E501


        :return: The parameter_id of this BTStandardContentParameterDefinition.  # noqa: E501
        :rtype: str
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this BTStandardContentParameterDefinition.


        :param parameter_id: The parameter_id of this BTStandardContentParameterDefinition.  # noqa: E501
        :type: str
        """

        self._parameter_id = parameter_id

    @property
    def visible(self):
        """Gets the visible of this BTStandardContentParameterDefinition.  # noqa: E501


        :return: The visible of this BTStandardContentParameterDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this BTStandardContentParameterDefinition.


        :param visible: The visible of this BTStandardContentParameterDefinition.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def is_custom_parameter(self):
        """Gets the is_custom_parameter of this BTStandardContentParameterDefinition.  # noqa: E501


        :return: The is_custom_parameter of this BTStandardContentParameterDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom_parameter

    @is_custom_parameter.setter
    def is_custom_parameter(self, is_custom_parameter):
        """Sets the is_custom_parameter of this BTStandardContentParameterDefinition.


        :param is_custom_parameter: The is_custom_parameter of this BTStandardContentParameterDefinition.  # noqa: E501
        :type: bool
        """

        self._is_custom_parameter = is_custom_parameter

    @property
    def is_driving_configuration(self):
        """Gets the is_driving_configuration of this BTStandardContentParameterDefinition.  # noqa: E501


        :return: The is_driving_configuration of this BTStandardContentParameterDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._is_driving_configuration

    @is_driving_configuration.setter
    def is_driving_configuration(self, is_driving_configuration):
        """Sets the is_driving_configuration of this BTStandardContentParameterDefinition.


        :param is_driving_configuration: The is_driving_configuration of this BTStandardContentParameterDefinition.  # noqa: E501
        :type: bool
        """

        self._is_driving_configuration = is_driving_configuration

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
        if not isinstance(other, BTStandardContentParameterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
