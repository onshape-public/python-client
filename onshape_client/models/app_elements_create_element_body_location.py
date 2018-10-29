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


class AppElementsCreateElementBodyLocation(object):
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
        'position': 'float',
        'group_id': 'str',
        'element_id': 'str'
    }

    attribute_map = {
        'position': 'position',
        'group_id': 'groupId',
        'element_id': 'elementId'
    }

    def __init__(self, position=None, group_id=None, element_id=None):  # noqa: E501
        """AppElementsCreateElementBodyLocation - a model defined in Swagger"""  # noqa: E501

        self._position = None
        self._group_id = None
        self._element_id = None
        self.discriminator = None

        if position is not None:
            self.position = position
        if group_id is not None:
            self.group_id = group_id
        if element_id is not None:
            self.element_id = element_id

    @property
    def position(self):
        """Gets the position of this AppElementsCreateElementBodyLocation.  # noqa: E501

        An indicator for the relative placement of the new element.    If elementId is specified, a negative number indicates insertion prior to the element and a non-negative    number indicates insertion following the element. If no elementId is specified, a negative value indicates    insertion at the end of the group or element list and a non-negative number indicates insertion at the start    of the group or elmenet list.  # noqa: E501

        :return: The position of this AppElementsCreateElementBodyLocation.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this AppElementsCreateElementBodyLocation.

        An indicator for the relative placement of the new element.    If elementId is specified, a negative number indicates insertion prior to the element and a non-negative    number indicates insertion following the element. If no elementId is specified, a negative value indicates    insertion at the end of the group or element list and a non-negative number indicates insertion at the start    of the group or elmenet list.  # noqa: E501

        :param position: The position of this AppElementsCreateElementBodyLocation.  # noqa: E501
        :type: float
        """

        self._position = position

    @property
    def group_id(self):
        """Gets the group_id of this AppElementsCreateElementBodyLocation.  # noqa: E501

        For internal use.  # noqa: E501

        :return: The group_id of this AppElementsCreateElementBodyLocation.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AppElementsCreateElementBodyLocation.

        For internal use.  # noqa: E501

        :param group_id: The group_id of this AppElementsCreateElementBodyLocation.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def element_id(self):
        """Gets the element_id of this AppElementsCreateElementBodyLocation.  # noqa: E501

        Id of an element to place the new element near.  # noqa: E501

        :return: The element_id of this AppElementsCreateElementBodyLocation.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this AppElementsCreateElementBodyLocation.

        Id of an element to place the new element near.  # noqa: E501

        :param element_id: The element_id of this AppElementsCreateElementBodyLocation.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

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
        if not isinstance(other, AppElementsCreateElementBodyLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
