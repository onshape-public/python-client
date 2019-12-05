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


class BTStringMinimumLengthPattern895AllOf(object):
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
        'minimum_length': 'int'
    }

    attribute_map = {
        'minimum_length': 'minimumLength'
    }

    def __init__(self, minimum_length=None, local_vars_configuration=None):  # noqa: E501
        """BTStringMinimumLengthPattern895AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._minimum_length = None
        self.discriminator = None

        if minimum_length is not None:
            self.minimum_length = minimum_length

    @property
    def minimum_length(self):
        """Gets the minimum_length of this BTStringMinimumLengthPattern895AllOf.  # noqa: E501


        :return: The minimum_length of this BTStringMinimumLengthPattern895AllOf.  # noqa: E501
        :rtype: int
        """
        return self._minimum_length

    @minimum_length.setter
    def minimum_length(self, minimum_length):
        """Sets the minimum_length of this BTStringMinimumLengthPattern895AllOf.


        :param minimum_length: The minimum_length of this BTStringMinimumLengthPattern895AllOf.  # noqa: E501
        :type: int
        """

        self._minimum_length = minimum_length

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
        if not isinstance(other, BTStringMinimumLengthPattern895AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTStringMinimumLengthPattern895AllOf):
            return True

        return self.to_dict() != other.to_dict()
