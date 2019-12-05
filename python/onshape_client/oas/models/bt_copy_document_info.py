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


class BTCopyDocumentInfo(object):
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
        'new_document_id': 'str',
        'new_document_name': 'str',
        'new_workspace_id': 'str',
        'new_parent_id': 'str',
        'new_project_id': 'str',
        'new_owner': 'BTOwnerInfo'
    }

    attribute_map = {
        'new_document_id': 'newDocumentId',
        'new_document_name': 'newDocumentName',
        'new_workspace_id': 'newWorkspaceId',
        'new_parent_id': 'newParentId',
        'new_project_id': 'newProjectId',
        'new_owner': 'newOwner'
    }

    def __init__(self, new_document_id=None, new_document_name=None, new_workspace_id=None, new_parent_id=None, new_project_id=None, new_owner=None, local_vars_configuration=None):  # noqa: E501
        """BTCopyDocumentInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._new_document_id = None
        self._new_document_name = None
        self._new_workspace_id = None
        self._new_parent_id = None
        self._new_project_id = None
        self._new_owner = None
        self.discriminator = None

        if new_document_id is not None:
            self.new_document_id = new_document_id
        if new_document_name is not None:
            self.new_document_name = new_document_name
        if new_workspace_id is not None:
            self.new_workspace_id = new_workspace_id
        if new_parent_id is not None:
            self.new_parent_id = new_parent_id
        if new_project_id is not None:
            self.new_project_id = new_project_id
        if new_owner is not None:
            self.new_owner = new_owner

    @property
    def new_document_id(self):
        """Gets the new_document_id of this BTCopyDocumentInfo.  # noqa: E501


        :return: The new_document_id of this BTCopyDocumentInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_document_id

    @new_document_id.setter
    def new_document_id(self, new_document_id):
        """Sets the new_document_id of this BTCopyDocumentInfo.


        :param new_document_id: The new_document_id of this BTCopyDocumentInfo.  # noqa: E501
        :type: str
        """

        self._new_document_id = new_document_id

    @property
    def new_document_name(self):
        """Gets the new_document_name of this BTCopyDocumentInfo.  # noqa: E501


        :return: The new_document_name of this BTCopyDocumentInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_document_name

    @new_document_name.setter
    def new_document_name(self, new_document_name):
        """Sets the new_document_name of this BTCopyDocumentInfo.


        :param new_document_name: The new_document_name of this BTCopyDocumentInfo.  # noqa: E501
        :type: str
        """

        self._new_document_name = new_document_name

    @property
    def new_workspace_id(self):
        """Gets the new_workspace_id of this BTCopyDocumentInfo.  # noqa: E501


        :return: The new_workspace_id of this BTCopyDocumentInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_workspace_id

    @new_workspace_id.setter
    def new_workspace_id(self, new_workspace_id):
        """Sets the new_workspace_id of this BTCopyDocumentInfo.


        :param new_workspace_id: The new_workspace_id of this BTCopyDocumentInfo.  # noqa: E501
        :type: str
        """

        self._new_workspace_id = new_workspace_id

    @property
    def new_parent_id(self):
        """Gets the new_parent_id of this BTCopyDocumentInfo.  # noqa: E501


        :return: The new_parent_id of this BTCopyDocumentInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_parent_id

    @new_parent_id.setter
    def new_parent_id(self, new_parent_id):
        """Sets the new_parent_id of this BTCopyDocumentInfo.


        :param new_parent_id: The new_parent_id of this BTCopyDocumentInfo.  # noqa: E501
        :type: str
        """

        self._new_parent_id = new_parent_id

    @property
    def new_project_id(self):
        """Gets the new_project_id of this BTCopyDocumentInfo.  # noqa: E501


        :return: The new_project_id of this BTCopyDocumentInfo.  # noqa: E501
        :rtype: str
        """
        return self._new_project_id

    @new_project_id.setter
    def new_project_id(self, new_project_id):
        """Sets the new_project_id of this BTCopyDocumentInfo.


        :param new_project_id: The new_project_id of this BTCopyDocumentInfo.  # noqa: E501
        :type: str
        """

        self._new_project_id = new_project_id

    @property
    def new_owner(self):
        """Gets the new_owner of this BTCopyDocumentInfo.  # noqa: E501


        :return: The new_owner of this BTCopyDocumentInfo.  # noqa: E501
        :rtype: BTOwnerInfo
        """
        return self._new_owner

    @new_owner.setter
    def new_owner(self, new_owner):
        """Sets the new_owner of this BTCopyDocumentInfo.


        :param new_owner: The new_owner of this BTCopyDocumentInfo.  # noqa: E501
        :type: BTOwnerInfo
        """

        self._new_owner = new_owner

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
        if not isinstance(other, BTCopyDocumentInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTCopyDocumentInfo):
            return True

        return self.to_dict() != other.to_dict()
