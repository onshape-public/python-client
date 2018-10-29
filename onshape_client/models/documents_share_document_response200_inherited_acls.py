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

from onshape_client.models.documents_share_document_response200_entries import DocumentsShareDocumentResponse200Entries  # noqa: F401,E501
from onshape_client.models.documents_share_document_response200_owner import DocumentsShareDocumentResponse200Owner  # noqa: F401,E501


class DocumentsShareDocumentResponse200InheritedAcls(object):
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
        'object_id': 'str',
        'object_name': 'float',
        'visibility': 'str',
        'name': 'str',
        'href': 'str',
        'entries': 'list[DocumentsShareDocumentResponse200Entries]',
        'owner': 'DocumentsShareDocumentResponse200Owner',
        'id': 'str',
        'object_type': 'float'
    }

    attribute_map = {
        'object_id': 'objectId',
        'object_name': 'objectName',
        'visibility': 'visibility',
        'name': 'name',
        'href': 'href',
        'entries': 'entries',
        'owner': 'owner',
        'id': 'id',
        'object_type': 'objectType'
    }

    def __init__(self, object_id=None, object_name=None, visibility=None, name=None, href=None, entries=None, owner=None, id=None, object_type=None):  # noqa: E501
        """DocumentsShareDocumentResponse200InheritedAcls - a model defined in Swagger"""  # noqa: E501

        self._object_id = None
        self._object_name = None
        self._visibility = None
        self._name = None
        self._href = None
        self._entries = None
        self._owner = None
        self._id = None
        self._object_type = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        if visibility is not None:
            self.visibility = visibility
        if name is not None:
            self.name = name
        if href is not None:
            self.href = href
        if entries is not None:
            self.entries = entries
        if owner is not None:
            self.owner = owner
        if id is not None:
            self.id = id
        if object_type is not None:
            self.object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        The ID of the parent folder that contributes access rights  # noqa: E501

        :return: The object_id of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this DocumentsShareDocumentResponse200InheritedAcls.

        The ID of the parent folder that contributes access rights  # noqa: E501

        :param object_id: The object_id of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_name(self):
        """Gets the object_name of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        The name of the parent object  # noqa: E501

        :return: The object_name of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: float
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this DocumentsShareDocumentResponse200InheritedAcls.

        The name of the parent object  # noqa: E501

        :param object_name: The object_name of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: float
        """

        self._object_name = object_name

    @property
    def visibility(self):
        """Gets the visibility of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        A description string indicating whether the folder is       public or private. Currently always private  # noqa: E501

        :return: The visibility of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this DocumentsShareDocumentResponse200InheritedAcls.

        A description string indicating whether the folder is       public or private. Currently always private  # noqa: E501

        :param visibility: The visibility of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def name(self):
        """Gets the name of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        Not used  # noqa: E501

        :return: The name of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentsShareDocumentResponse200InheritedAcls.

        Not used  # noqa: E501

        :param name: The name of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        A URL referencing the API to get this structure  # noqa: E501

        :return: The href of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DocumentsShareDocumentResponse200InheritedAcls.

        A URL referencing the API to get this structure  # noqa: E501

        :param href: The href of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def entries(self):
        """Gets the entries of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        The current share entries for the parent folder. Each share      entry indicates an entity that the folder and contained objects are shared with and the permissions granted      to the entity  # noqa: E501

        :return: The entries of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: list[DocumentsShareDocumentResponse200Entries]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this DocumentsShareDocumentResponse200InheritedAcls.

        The current share entries for the parent folder. Each share      entry indicates an entity that the folder and contained objects are shared with and the permissions granted      to the entity  # noqa: E501

        :param entries: The entries of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: list[DocumentsShareDocumentResponse200Entries]
        """

        self._entries = entries

    @property
    def owner(self):
        """Gets the owner of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501


        :return: The owner of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: DocumentsShareDocumentResponse200Owner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DocumentsShareDocumentResponse200InheritedAcls.


        :param owner: The owner of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: DocumentsShareDocumentResponse200Owner
        """

        self._owner = owner

    @property
    def id(self):
        """Gets the id of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        Not used  # noqa: E501

        :return: The id of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsShareDocumentResponse200InheritedAcls.

        Not used  # noqa: E501

        :param id: The id of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object_type(self):
        """Gets the object_type of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501

        Set to the value 4, indicating the the objectId       identifies a folder  # noqa: E501

        :return: The object_type of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :rtype: float
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this DocumentsShareDocumentResponse200InheritedAcls.

        Set to the value 4, indicating the the objectId       identifies a folder  # noqa: E501

        :param object_type: The object_type of this DocumentsShareDocumentResponse200InheritedAcls.  # noqa: E501
        :type: float
        """

        self._object_type = object_type

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
        if not isinstance(other, DocumentsShareDocumentResponse200InheritedAcls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
