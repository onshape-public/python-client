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


class BTGlobalTreeNodeOwnerParams(object):
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
        'resource_id': 'str',
        'resource_type': 'str',
        'new_owner_type': 'int',
        'new_owner_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resourceId',
        'resource_type': 'resourceType',
        'new_owner_type': 'newOwnerType',
        'new_owner_id': 'newOwnerId'
    }

    def __init__(self, resource_id=None, resource_type=None, new_owner_type=None, new_owner_id=None):  # noqa: E501
        """BTGlobalTreeNodeOwnerParams - a model defined in OpenAPI"""  # noqa: E501

        self._resource_id = None
        self._resource_type = None
        self._new_owner_type = None
        self._new_owner_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if new_owner_type is not None:
            self.new_owner_type = new_owner_type
        if new_owner_id is not None:
            self.new_owner_id = new_owner_id

    @property
    def resource_id(self):
        """Gets the resource_id of this BTGlobalTreeNodeOwnerParams.  # noqa: E501


        :return: The resource_id of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BTGlobalTreeNodeOwnerParams.


        :param resource_id: The resource_id of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this BTGlobalTreeNodeOwnerParams.  # noqa: E501


        :return: The resource_type of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BTGlobalTreeNodeOwnerParams.


        :param resource_type: The resource_type of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def new_owner_type(self):
        """Gets the new_owner_type of this BTGlobalTreeNodeOwnerParams.  # noqa: E501


        :return: The new_owner_type of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :rtype: int
        """
        return self._new_owner_type

    @new_owner_type.setter
    def new_owner_type(self, new_owner_type):
        """Sets the new_owner_type of this BTGlobalTreeNodeOwnerParams.


        :param new_owner_type: The new_owner_type of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :type: int
        """

        self._new_owner_type = new_owner_type

    @property
    def new_owner_id(self):
        """Gets the new_owner_id of this BTGlobalTreeNodeOwnerParams.  # noqa: E501


        :return: The new_owner_id of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :rtype: str
        """
        return self._new_owner_id

    @new_owner_id.setter
    def new_owner_id(self, new_owner_id):
        """Sets the new_owner_id of this BTGlobalTreeNodeOwnerParams.


        :param new_owner_id: The new_owner_id of this BTGlobalTreeNodeOwnerParams.  # noqa: E501
        :type: str
        """

        self._new_owner_id = new_owner_id

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
        if not isinstance(other, BTGlobalTreeNodeOwnerParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
