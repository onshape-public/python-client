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


class AppElementsGetSubElementContentResponse200Deltas(object):
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
        'delta': 'str'
    }

    attribute_map = {
        'delta': 'delta'
    }

    def __init__(self, delta=None):  # noqa: E501
        """AppElementsGetSubElementContentResponse200Deltas - a model defined in Swagger"""  # noqa: E501

        self._delta = None
        self.discriminator = None

        if delta is not None:
            self.delta = delta

    @property
    def delta(self):
        """Gets the delta of this AppElementsGetSubElementContentResponse200Deltas.  # noqa: E501

        A single content delta, in Base-64 encodding  # noqa: E501

        :return: The delta of this AppElementsGetSubElementContentResponse200Deltas.  # noqa: E501
        :rtype: str
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this AppElementsGetSubElementContentResponse200Deltas.

        A single content delta, in Base-64 encodding  # noqa: E501

        :param delta: The delta of this AppElementsGetSubElementContentResponse200Deltas.  # noqa: E501
        :type: str
        """

        self._delta = delta

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
        if not isinstance(other, AppElementsGetSubElementContentResponse200Deltas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
