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


class BTConfigurationResponse2019(object):
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
        'current_configuration': 'list[BTMParameter1]',
        'configuration_parameters': 'list[BTMConfigurationParameter819]'
    }

    attribute_map = {
        'current_configuration': 'currentConfiguration',
        'configuration_parameters': 'configurationParameters'
    }

    def __init__(self, current_configuration=None, configuration_parameters=None, local_vars_configuration=None):  # noqa: E501
        """BTConfigurationResponse2019 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_configuration = None
        self._configuration_parameters = None
        self.discriminator = None

        if current_configuration is not None:
            self.current_configuration = current_configuration
        if configuration_parameters is not None:
            self.configuration_parameters = configuration_parameters

    @property
    def current_configuration(self):
        """Gets the current_configuration of this BTConfigurationResponse2019.  # noqa: E501


        :return: The current_configuration of this BTConfigurationResponse2019.  # noqa: E501
        :rtype: list[BTMParameter1]
        """
        return self._current_configuration

    @current_configuration.setter
    def current_configuration(self, current_configuration):
        """Sets the current_configuration of this BTConfigurationResponse2019.


        :param current_configuration: The current_configuration of this BTConfigurationResponse2019.  # noqa: E501
        :type: list[BTMParameter1]
        """

        self._current_configuration = current_configuration

    @property
    def configuration_parameters(self):
        """Gets the configuration_parameters of this BTConfigurationResponse2019.  # noqa: E501


        :return: The configuration_parameters of this BTConfigurationResponse2019.  # noqa: E501
        :rtype: list[BTMConfigurationParameter819]
        """
        return self._configuration_parameters

    @configuration_parameters.setter
    def configuration_parameters(self, configuration_parameters):
        """Sets the configuration_parameters of this BTConfigurationResponse2019.


        :param configuration_parameters: The configuration_parameters of this BTConfigurationResponse2019.  # noqa: E501
        :type: list[BTMConfigurationParameter819]
        """

        self._configuration_parameters = configuration_parameters

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
        if not isinstance(other, BTConfigurationResponse2019):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTConfigurationResponse2019):
            return True

        return self.to_dict() != other.to_dict()
