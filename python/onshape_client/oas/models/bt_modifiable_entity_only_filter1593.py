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


class BTModifiableEntityOnlyFilter1593(object):
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
        'modifiable_only': 'bool'
    }

    attribute_map = {
        'modifiable_only': 'modifiableOnly'
    }

    def __init__(self, modifiable_only=None, local_vars_configuration=None):  # noqa: E501
        """BTModifiableEntityOnlyFilter1593 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._modifiable_only = None
        self.discriminator = None

        if modifiable_only is not None:
            self.modifiable_only = modifiable_only

    @property
    def modifiable_only(self):
        """Gets the modifiable_only of this BTModifiableEntityOnlyFilter1593.  # noqa: E501


        :return: The modifiable_only of this BTModifiableEntityOnlyFilter1593.  # noqa: E501
        :rtype: bool
        """
        return self._modifiable_only

    @modifiable_only.setter
    def modifiable_only(self, modifiable_only):
        """Sets the modifiable_only of this BTModifiableEntityOnlyFilter1593.


        :param modifiable_only: The modifiable_only of this BTModifiableEntityOnlyFilter1593.  # noqa: E501
        :type: bool
        """

        self._modifiable_only = modifiable_only

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
        if not isinstance(other, BTModifiableEntityOnlyFilter1593):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTModifiableEntityOnlyFilter1593):
            return True

        return self.to_dict() != other.to_dict()
