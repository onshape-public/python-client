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


class BTFlatSheetMetalFilter3018(object):
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
        'allows': 'str'
    }

    attribute_map = {
        'allows': 'allows'
    }

    def __init__(self, allows=None, local_vars_configuration=None):  # noqa: E501
        """BTFlatSheetMetalFilter3018 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allows = None
        self.discriminator = None

        if allows is not None:
            self.allows = allows

    @property
    def allows(self):
        """Gets the allows of this BTFlatSheetMetalFilter3018.  # noqa: E501


        :return: The allows of this BTFlatSheetMetalFilter3018.  # noqa: E501
        :rtype: str
        """
        return self._allows

    @allows.setter
    def allows(self, allows):
        """Sets the allows of this BTFlatSheetMetalFilter3018.


        :param allows: The allows of this BTFlatSheetMetalFilter3018.  # noqa: E501
        :type: str
        """
        allowed_values = ["MODEL_ONLY", "FLATTENED_ONLY", "MODEL_AND_FLATTENED", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and allows not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `allows` ({0}), must be one of {1}"  # noqa: E501
                .format(allows, allowed_values)
            )

        self._allows = allows

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
        if not isinstance(other, BTFlatSheetMetalFilter3018):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTFlatSheetMetalFilter3018):
            return True

        return self.to_dict() != other.to_dict()
