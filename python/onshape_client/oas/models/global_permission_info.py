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


class GlobalPermissionInfo(object):
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
        'admin_enterprise': 'bool',
        'manage_rbac': 'bool',
        'manage_users': 'bool',
        'manage_guest_users': 'bool',
        'delete_permanently': 'bool',
        'access_reports': 'bool',
        'create_project': 'bool',
        'approve_releases': 'bool',
        'create_releases': 'bool',
        'share_for_anonymous_access': 'bool',
        'allow_app_store_access': 'bool'
    }

    attribute_map = {
        'admin_enterprise': 'adminEnterprise',
        'manage_rbac': 'manageRbac',
        'manage_users': 'manageUsers',
        'manage_guest_users': 'manageGuestUsers',
        'delete_permanently': 'deletePermanently',
        'access_reports': 'accessReports',
        'create_project': 'createProject',
        'approve_releases': 'approveReleases',
        'create_releases': 'createReleases',
        'share_for_anonymous_access': 'shareForAnonymousAccess',
        'allow_app_store_access': 'allowAppStoreAccess'
    }

    def __init__(self, admin_enterprise=None, manage_rbac=None, manage_users=None, manage_guest_users=None, delete_permanently=None, access_reports=None, create_project=None, approve_releases=None, create_releases=None, share_for_anonymous_access=None, allow_app_store_access=None, local_vars_configuration=None):  # noqa: E501
        """GlobalPermissionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_enterprise = None
        self._manage_rbac = None
        self._manage_users = None
        self._manage_guest_users = None
        self._delete_permanently = None
        self._access_reports = None
        self._create_project = None
        self._approve_releases = None
        self._create_releases = None
        self._share_for_anonymous_access = None
        self._allow_app_store_access = None
        self.discriminator = None

        if admin_enterprise is not None:
            self.admin_enterprise = admin_enterprise
        if manage_rbac is not None:
            self.manage_rbac = manage_rbac
        if manage_users is not None:
            self.manage_users = manage_users
        if manage_guest_users is not None:
            self.manage_guest_users = manage_guest_users
        if delete_permanently is not None:
            self.delete_permanently = delete_permanently
        if access_reports is not None:
            self.access_reports = access_reports
        if create_project is not None:
            self.create_project = create_project
        if approve_releases is not None:
            self.approve_releases = approve_releases
        if create_releases is not None:
            self.create_releases = create_releases
        if share_for_anonymous_access is not None:
            self.share_for_anonymous_access = share_for_anonymous_access
        if allow_app_store_access is not None:
            self.allow_app_store_access = allow_app_store_access

    @property
    def admin_enterprise(self):
        """Gets the admin_enterprise of this GlobalPermissionInfo.  # noqa: E501


        :return: The admin_enterprise of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._admin_enterprise

    @admin_enterprise.setter
    def admin_enterprise(self, admin_enterprise):
        """Sets the admin_enterprise of this GlobalPermissionInfo.


        :param admin_enterprise: The admin_enterprise of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._admin_enterprise = admin_enterprise

    @property
    def manage_rbac(self):
        """Gets the manage_rbac of this GlobalPermissionInfo.  # noqa: E501


        :return: The manage_rbac of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._manage_rbac

    @manage_rbac.setter
    def manage_rbac(self, manage_rbac):
        """Sets the manage_rbac of this GlobalPermissionInfo.


        :param manage_rbac: The manage_rbac of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._manage_rbac = manage_rbac

    @property
    def manage_users(self):
        """Gets the manage_users of this GlobalPermissionInfo.  # noqa: E501


        :return: The manage_users of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._manage_users

    @manage_users.setter
    def manage_users(self, manage_users):
        """Sets the manage_users of this GlobalPermissionInfo.


        :param manage_users: The manage_users of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._manage_users = manage_users

    @property
    def manage_guest_users(self):
        """Gets the manage_guest_users of this GlobalPermissionInfo.  # noqa: E501


        :return: The manage_guest_users of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._manage_guest_users

    @manage_guest_users.setter
    def manage_guest_users(self, manage_guest_users):
        """Sets the manage_guest_users of this GlobalPermissionInfo.


        :param manage_guest_users: The manage_guest_users of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._manage_guest_users = manage_guest_users

    @property
    def delete_permanently(self):
        """Gets the delete_permanently of this GlobalPermissionInfo.  # noqa: E501


        :return: The delete_permanently of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._delete_permanently

    @delete_permanently.setter
    def delete_permanently(self, delete_permanently):
        """Sets the delete_permanently of this GlobalPermissionInfo.


        :param delete_permanently: The delete_permanently of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._delete_permanently = delete_permanently

    @property
    def access_reports(self):
        """Gets the access_reports of this GlobalPermissionInfo.  # noqa: E501


        :return: The access_reports of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._access_reports

    @access_reports.setter
    def access_reports(self, access_reports):
        """Sets the access_reports of this GlobalPermissionInfo.


        :param access_reports: The access_reports of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._access_reports = access_reports

    @property
    def create_project(self):
        """Gets the create_project of this GlobalPermissionInfo.  # noqa: E501


        :return: The create_project of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._create_project

    @create_project.setter
    def create_project(self, create_project):
        """Sets the create_project of this GlobalPermissionInfo.


        :param create_project: The create_project of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._create_project = create_project

    @property
    def approve_releases(self):
        """Gets the approve_releases of this GlobalPermissionInfo.  # noqa: E501


        :return: The approve_releases of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._approve_releases

    @approve_releases.setter
    def approve_releases(self, approve_releases):
        """Sets the approve_releases of this GlobalPermissionInfo.


        :param approve_releases: The approve_releases of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._approve_releases = approve_releases

    @property
    def create_releases(self):
        """Gets the create_releases of this GlobalPermissionInfo.  # noqa: E501


        :return: The create_releases of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._create_releases

    @create_releases.setter
    def create_releases(self, create_releases):
        """Sets the create_releases of this GlobalPermissionInfo.


        :param create_releases: The create_releases of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._create_releases = create_releases

    @property
    def share_for_anonymous_access(self):
        """Gets the share_for_anonymous_access of this GlobalPermissionInfo.  # noqa: E501


        :return: The share_for_anonymous_access of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._share_for_anonymous_access

    @share_for_anonymous_access.setter
    def share_for_anonymous_access(self, share_for_anonymous_access):
        """Sets the share_for_anonymous_access of this GlobalPermissionInfo.


        :param share_for_anonymous_access: The share_for_anonymous_access of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._share_for_anonymous_access = share_for_anonymous_access

    @property
    def allow_app_store_access(self):
        """Gets the allow_app_store_access of this GlobalPermissionInfo.  # noqa: E501


        :return: The allow_app_store_access of this GlobalPermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._allow_app_store_access

    @allow_app_store_access.setter
    def allow_app_store_access(self, allow_app_store_access):
        """Sets the allow_app_store_access of this GlobalPermissionInfo.


        :param allow_app_store_access: The allow_app_store_access of this GlobalPermissionInfo.  # noqa: E501
        :type: bool
        """

        self._allow_app_store_access = allow_app_store_access

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
        if not isinstance(other, GlobalPermissionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GlobalPermissionInfo):
            return True

        return self.to_dict() != other.to_dict()
