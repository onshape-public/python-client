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


class BTUserSummaryInfo(object):
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
        'source': 'int',
        'is_guest': 'bool',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'is_light': 'bool',
        'global_permissions': 'GlobalPermissionInfo',
        'last_login_time': 'datetime',
        'company': 'BTCompanySummaryInfo',
        'state': 'int',
        'image': 'str',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'source': 'source',
        'is_guest': 'isGuest',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'is_light': 'isLight',
        'global_permissions': 'globalPermissions',
        'last_login_time': 'lastLoginTime',
        'company': 'company',
        'state': 'state',
        'image': 'image',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, source=None, is_guest=None, first_name=None, last_name=None, email=None, is_light=None, global_permissions=None, last_login_time=None, company=None, state=None, image=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTUserSummaryInfo - a model defined in OpenAPI"""  # noqa: E501

        self._source = None
        self._is_guest = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._is_light = None
        self._global_permissions = None
        self._last_login_time = None
        self._company = None
        self._state = None
        self._image = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if is_guest is not None:
            self.is_guest = is_guest
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if is_light is not None:
            self.is_light = is_light
        if global_permissions is not None:
            self.global_permissions = global_permissions
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if company is not None:
            self.company = company
        if state is not None:
            self.state = state
        if image is not None:
            self.image = image
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def source(self):
        """Gets the source of this BTUserSummaryInfo.  # noqa: E501


        :return: The source of this BTUserSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BTUserSummaryInfo.


        :param source: The source of this BTUserSummaryInfo.  # noqa: E501
        :type: int
        """

        self._source = source

    @property
    def is_guest(self):
        """Gets the is_guest of this BTUserSummaryInfo.  # noqa: E501


        :return: The is_guest of this BTUserSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_guest

    @is_guest.setter
    def is_guest(self, is_guest):
        """Sets the is_guest of this BTUserSummaryInfo.


        :param is_guest: The is_guest of this BTUserSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_guest = is_guest

    @property
    def first_name(self):
        """Gets the first_name of this BTUserSummaryInfo.  # noqa: E501


        :return: The first_name of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this BTUserSummaryInfo.


        :param first_name: The first_name of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this BTUserSummaryInfo.  # noqa: E501


        :return: The last_name of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this BTUserSummaryInfo.


        :param last_name: The last_name of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this BTUserSummaryInfo.  # noqa: E501


        :return: The email of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTUserSummaryInfo.


        :param email: The email of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def is_light(self):
        """Gets the is_light of this BTUserSummaryInfo.  # noqa: E501


        :return: The is_light of this BTUserSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_light

    @is_light.setter
    def is_light(self, is_light):
        """Sets the is_light of this BTUserSummaryInfo.


        :param is_light: The is_light of this BTUserSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._is_light = is_light

    @property
    def global_permissions(self):
        """Gets the global_permissions of this BTUserSummaryInfo.  # noqa: E501


        :return: The global_permissions of this BTUserSummaryInfo.  # noqa: E501
        :rtype: GlobalPermissionInfo
        """
        return self._global_permissions

    @global_permissions.setter
    def global_permissions(self, global_permissions):
        """Sets the global_permissions of this BTUserSummaryInfo.


        :param global_permissions: The global_permissions of this BTUserSummaryInfo.  # noqa: E501
        :type: GlobalPermissionInfo
        """

        self._global_permissions = global_permissions

    @property
    def last_login_time(self):
        """Gets the last_login_time of this BTUserSummaryInfo.  # noqa: E501


        :return: The last_login_time of this BTUserSummaryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this BTUserSummaryInfo.


        :param last_login_time: The last_login_time of this BTUserSummaryInfo.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def company(self):
        """Gets the company of this BTUserSummaryInfo.  # noqa: E501


        :return: The company of this BTUserSummaryInfo.  # noqa: E501
        :rtype: BTCompanySummaryInfo
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this BTUserSummaryInfo.


        :param company: The company of this BTUserSummaryInfo.  # noqa: E501
        :type: BTCompanySummaryInfo
        """

        self._company = company

    @property
    def state(self):
        """Gets the state of this BTUserSummaryInfo.  # noqa: E501


        :return: The state of this BTUserSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BTUserSummaryInfo.


        :param state: The state of this BTUserSummaryInfo.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def image(self):
        """Gets the image of this BTUserSummaryInfo.  # noqa: E501


        :return: The image of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this BTUserSummaryInfo.


        :param image: The image of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this BTUserSummaryInfo.  # noqa: E501


        :return: The name of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTUserSummaryInfo.


        :param name: The name of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTUserSummaryInfo.  # noqa: E501


        :return: The id of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTUserSummaryInfo.


        :param id: The id of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTUserSummaryInfo.  # noqa: E501


        :return: The href of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTUserSummaryInfo.


        :param href: The href of this BTUserSummaryInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTUserSummaryInfo.  # noqa: E501


        :return: The view_ref of this BTUserSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTUserSummaryInfo.


        :param view_ref: The view_ref of this BTUserSummaryInfo.  # noqa: E501
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
        if not isinstance(other, BTUserSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
