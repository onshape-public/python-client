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


class BTImageFilter853AllOf(object):
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
        'is_image': 'bool'
    }

    attribute_map = {
        'is_image': 'isImage'
    }

    def __init__(self, is_image=None, local_vars_configuration=None):  # noqa: E501
        """BTImageFilter853AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_image = None
        self.discriminator = None

        if is_image is not None:
            self.is_image = is_image

    @property
    def is_image(self):
        """Gets the is_image of this BTImageFilter853AllOf.  # noqa: E501


        :return: The is_image of this BTImageFilter853AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_image

    @is_image.setter
    def is_image(self, is_image):
        """Sets the is_image of this BTImageFilter853AllOf.


        :param is_image: The is_image of this BTImageFilter853AllOf.  # noqa: E501
        :type: bool
        """

        self._is_image = is_image

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
        if not isinstance(other, BTImageFilter853AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTImageFilter853AllOf):
            return True

        return self.to_dict() != other.to_dict()
