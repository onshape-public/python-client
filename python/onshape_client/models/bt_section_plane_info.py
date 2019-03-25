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


class BTSectionPlaneInfo(object):
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
        'center': 'list[float]',
        'normal': 'list[float]',
        'tangent': 'list[float]'
    }

    attribute_map = {
        'center': 'center',
        'normal': 'normal',
        'tangent': 'tangent'
    }

    def __init__(self, center=None, normal=None, tangent=None):  # noqa: E501
        """BTSectionPlaneInfo - a model defined in OpenAPI"""  # noqa: E501

        self._center = None
        self._normal = None
        self._tangent = None
        self.discriminator = None

        if center is not None:
            self.center = center
        if normal is not None:
            self.normal = normal
        if tangent is not None:
            self.tangent = tangent

    @property
    def center(self):
        """Gets the center of this BTSectionPlaneInfo.  # noqa: E501


        :return: The center of this BTSectionPlaneInfo.  # noqa: E501
        :rtype: list[float]
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this BTSectionPlaneInfo.


        :param center: The center of this BTSectionPlaneInfo.  # noqa: E501
        :type: list[float]
        """

        self._center = center

    @property
    def normal(self):
        """Gets the normal of this BTSectionPlaneInfo.  # noqa: E501


        :return: The normal of this BTSectionPlaneInfo.  # noqa: E501
        :rtype: list[float]
        """
        return self._normal

    @normal.setter
    def normal(self, normal):
        """Sets the normal of this BTSectionPlaneInfo.


        :param normal: The normal of this BTSectionPlaneInfo.  # noqa: E501
        :type: list[float]
        """

        self._normal = normal

    @property
    def tangent(self):
        """Gets the tangent of this BTSectionPlaneInfo.  # noqa: E501


        :return: The tangent of this BTSectionPlaneInfo.  # noqa: E501
        :rtype: list[float]
        """
        return self._tangent

    @tangent.setter
    def tangent(self, tangent):
        """Sets the tangent of this BTSectionPlaneInfo.


        :param tangent: The tangent of this BTSectionPlaneInfo.  # noqa: E501
        :type: list[float]
        """

        self._tangent = tangent

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
        if not isinstance(other, BTSectionPlaneInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
