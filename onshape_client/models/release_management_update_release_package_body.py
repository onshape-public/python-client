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

from onshape_client.models.release_management_update_release_package_body_items import ReleaseManagementUpdateReleasePackageBodyItems  # noqa: F401,E501
from onshape_client.models.release_management_update_release_package_body_properties_1 import ReleaseManagementUpdateReleasePackageBodyProperties1  # noqa: F401,E501


class ReleaseManagementUpdateReleasePackageBody(object):
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
        'items': 'list[ReleaseManagementUpdateReleasePackageBodyItems]',
        'properties': 'list[ReleaseManagementUpdateReleasePackageBodyProperties1]'
    }

    attribute_map = {
        'items': 'items',
        'properties': 'properties'
    }

    def __init__(self, items=None, properties=None):  # noqa: E501
        """ReleaseManagementUpdateReleasePackageBody - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._properties = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if properties is not None:
            self.properties = properties

    @property
    def items(self):
        """Gets the items of this ReleaseManagementUpdateReleasePackageBody.  # noqa: E501

        Array of items to be updated along with their desired new properties. Only the           items for which properties need to be updated to be included in this list  # noqa: E501

        :return: The items of this ReleaseManagementUpdateReleasePackageBody.  # noqa: E501
        :rtype: list[ReleaseManagementUpdateReleasePackageBodyItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ReleaseManagementUpdateReleasePackageBody.

        Array of items to be updated along with their desired new properties. Only the           items for which properties need to be updated to be included in this list  # noqa: E501

        :param items: The items of this ReleaseManagementUpdateReleasePackageBody.  # noqa: E501
        :type: list[ReleaseManagementUpdateReleasePackageBodyItems]
        """

        self._items = items

    @property
    def properties(self):
        """Gets the properties of this ReleaseManagementUpdateReleasePackageBody.  # noqa: E501

        Array of properties to update before doing the transition. All properties           with required=true which do not have a value must be specified. No properties with editable=false           should be specified.  # noqa: E501

        :return: The properties of this ReleaseManagementUpdateReleasePackageBody.  # noqa: E501
        :rtype: list[ReleaseManagementUpdateReleasePackageBodyProperties1]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ReleaseManagementUpdateReleasePackageBody.

        Array of properties to update before doing the transition. All properties           with required=true which do not have a value must be specified. No properties with editable=false           should be specified.  # noqa: E501

        :param properties: The properties of this ReleaseManagementUpdateReleasePackageBody.  # noqa: E501
        :type: list[ReleaseManagementUpdateReleasePackageBodyProperties1]
        """

        self._properties = properties

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
        if not isinstance(other, ReleaseManagementUpdateReleasePackageBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
