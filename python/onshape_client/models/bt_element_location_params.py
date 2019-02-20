# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.93
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTElementLocationParams(object):
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
        'element_id': 'str',
        'position': 'int',
        'group_id': 'str'
    }

    attribute_map = {
        'element_id': 'elementId',
        'position': 'position',
        'group_id': 'groupId'
    }

    def __init__(self, element_id=None, position=None, group_id=None):  # noqa: E501
        """BTElementLocationParams - a model defined in OpenAPI"""  # noqa: E501

        self._element_id = None
        self._position = None
        self._group_id = None
        self.discriminator = None

        if element_id is not None:
            self.element_id = element_id
        if position is not None:
            self.position = position
        if group_id is not None:
            self.group_id = group_id

    @property
    def element_id(self):
        """Gets the element_id of this BTElementLocationParams.  # noqa: E501


        :return: The element_id of this BTElementLocationParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTElementLocationParams.


        :param element_id: The element_id of this BTElementLocationParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def position(self):
        """Gets the position of this BTElementLocationParams.  # noqa: E501


        :return: The position of this BTElementLocationParams.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BTElementLocationParams.


        :param position: The position of this BTElementLocationParams.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def group_id(self):
        """Gets the group_id of this BTElementLocationParams.  # noqa: E501


        :return: The group_id of this BTElementLocationParams.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this BTElementLocationParams.


        :param group_id: The group_id of this BTElementLocationParams.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

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
        if not isinstance(other, BTElementLocationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
