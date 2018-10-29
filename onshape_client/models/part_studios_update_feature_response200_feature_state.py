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

from onshape_client.models.part_studios_update_feature_response200_feature_state_message import PartStudiosUpdateFeatureResponse200FeatureStateMessage  # noqa: F401,E501


class PartStudiosUpdateFeatureResponse200FeatureState(object):
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
        'message': 'PartStudiosUpdateFeatureResponse200FeatureStateMessage'
    }

    attribute_map = {
        'message': 'message'
    }

    def __init__(self, message=None):  # noqa: E501
        """PartStudiosUpdateFeatureResponse200FeatureState - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self.discriminator = None

        if message is not None:
            self.message = message

    @property
    def message(self):
        """Gets the message of this PartStudiosUpdateFeatureResponse200FeatureState.  # noqa: E501


        :return: The message of this PartStudiosUpdateFeatureResponse200FeatureState.  # noqa: E501
        :rtype: PartStudiosUpdateFeatureResponse200FeatureStateMessage
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PartStudiosUpdateFeatureResponse200FeatureState.


        :param message: The message of this PartStudiosUpdateFeatureResponse200FeatureState.  # noqa: E501
        :type: PartStudiosUpdateFeatureResponse200FeatureStateMessage
        """

        self._message = message

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
        if not isinstance(other, PartStudiosUpdateFeatureResponse200FeatureState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
