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


class BTIdentityInfo(object):
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
        'identity_type': 'int',
        'user': 'BTUserSummaryInfo',
        'team': 'BTTeamSummaryInfo',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'identity_type': 'identityType',
        'user': 'user',
        'team': 'team',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, identity_type=None, user=None, team=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTIdentityInfo - a model defined in OpenAPI"""  # noqa: E501

        self._identity_type = None
        self._user = None
        self._team = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if identity_type is not None:
            self.identity_type = identity_type
        if user is not None:
            self.user = user
        if team is not None:
            self.team = team
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def identity_type(self):
        """Gets the identity_type of this BTIdentityInfo.  # noqa: E501


        :return: The identity_type of this BTIdentityInfo.  # noqa: E501
        :rtype: int
        """
        return self._identity_type

    @identity_type.setter
    def identity_type(self, identity_type):
        """Sets the identity_type of this BTIdentityInfo.


        :param identity_type: The identity_type of this BTIdentityInfo.  # noqa: E501
        :type: int
        """

        self._identity_type = identity_type

    @property
    def user(self):
        """Gets the user of this BTIdentityInfo.  # noqa: E501


        :return: The user of this BTIdentityInfo.  # noqa: E501
        :rtype: BTUserSummaryInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BTIdentityInfo.


        :param user: The user of this BTIdentityInfo.  # noqa: E501
        :type: BTUserSummaryInfo
        """

        self._user = user

    @property
    def team(self):
        """Gets the team of this BTIdentityInfo.  # noqa: E501


        :return: The team of this BTIdentityInfo.  # noqa: E501
        :rtype: BTTeamSummaryInfo
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BTIdentityInfo.


        :param team: The team of this BTIdentityInfo.  # noqa: E501
        :type: BTTeamSummaryInfo
        """

        self._team = team

    @property
    def name(self):
        """Gets the name of this BTIdentityInfo.  # noqa: E501


        :return: The name of this BTIdentityInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTIdentityInfo.


        :param name: The name of this BTIdentityInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTIdentityInfo.  # noqa: E501


        :return: The id of this BTIdentityInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTIdentityInfo.


        :param id: The id of this BTIdentityInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTIdentityInfo.  # noqa: E501


        :return: The href of this BTIdentityInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTIdentityInfo.


        :param href: The href of this BTIdentityInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTIdentityInfo.  # noqa: E501


        :return: The view_ref of this BTIdentityInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTIdentityInfo.


        :param view_ref: The view_ref of this BTIdentityInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

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
        if not isinstance(other, BTIdentityInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
