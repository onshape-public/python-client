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


class DocumentsCopyWorkspaceBody(object):
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
        'new_name': 'str',
        'owner_id': 'str',
        'beta_capability_ids': 'list[str]',
        'is_public': 'bool',
        'owner_type_index': 'float'
    }

    attribute_map = {
        'new_name': 'newName',
        'owner_id': 'ownerId',
        'beta_capability_ids': 'betaCapabilityIds',
        'is_public': 'isPublic',
        'owner_type_index': 'ownerTypeIndex'
    }

    def __init__(self, new_name=None, owner_id=None, beta_capability_ids=None, is_public=None, owner_type_index=None):  # noqa: E501
        """DocumentsCopyWorkspaceBody - a model defined in Swagger"""  # noqa: E501

        self._new_name = None
        self._owner_id = None
        self._beta_capability_ids = None
        self._is_public = None
        self._owner_type_index = None
        self.discriminator = None

        if new_name is not None:
            self.new_name = new_name
        if owner_id is not None:
            self.owner_id = owner_id
        if beta_capability_ids is not None:
            self.beta_capability_ids = beta_capability_ids
        if is_public is not None:
            self.is_public = is_public
        if owner_type_index is not None:
            self.owner_type_index = owner_type_index

    @property
    def new_name(self):
        """Gets the new_name of this DocumentsCopyWorkspaceBody.  # noqa: E501

        New document name  # noqa: E501

        :return: The new_name of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this DocumentsCopyWorkspaceBody.

        New document name  # noqa: E501

        :param new_name: The new_name of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def owner_id(self):
        """Gets the owner_id of this DocumentsCopyWorkspaceBody.  # noqa: E501

        Owner's user ID (default: current user)  # noqa: E501

        :return: The owner_id of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this DocumentsCopyWorkspaceBody.

        Owner's user ID (default: current user)  # noqa: E501

        :param owner_id: The owner_id of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def beta_capability_ids(self):
        """Gets the beta_capability_ids of this DocumentsCopyWorkspaceBody.  # noqa: E501

        Onshape internal use  # noqa: E501

        :return: The beta_capability_ids of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._beta_capability_ids

    @beta_capability_ids.setter
    def beta_capability_ids(self, beta_capability_ids):
        """Sets the beta_capability_ids of this DocumentsCopyWorkspaceBody.

        Onshape internal use  # noqa: E501

        :param beta_capability_ids: The beta_capability_ids of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :type: list[str]
        """

        self._beta_capability_ids = beta_capability_ids

    @property
    def is_public(self):
        """Gets the is_public of this DocumentsCopyWorkspaceBody.  # noqa: E501

        Whether new document is public (default: false)  # noqa: E501

        :return: The is_public of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this DocumentsCopyWorkspaceBody.

        Whether new document is public (default: false)  # noqa: E501

        :param is_public: The is_public of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def owner_type_index(self):
        """Gets the owner_type_index of this DocumentsCopyWorkspaceBody.  # noqa: E501

        Owner's user type, which can be: 0: user 1: company 2: Team (default:           0)  # noqa: E501

        :return: The owner_type_index of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :rtype: float
        """
        return self._owner_type_index

    @owner_type_index.setter
    def owner_type_index(self, owner_type_index):
        """Sets the owner_type_index of this DocumentsCopyWorkspaceBody.

        Owner's user type, which can be: 0: user 1: company 2: Team (default:           0)  # noqa: E501

        :param owner_type_index: The owner_type_index of this DocumentsCopyWorkspaceBody.  # noqa: E501
        :type: float
        """

        self._owner_type_index = owner_type_index

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
        if not isinstance(other, DocumentsCopyWorkspaceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
