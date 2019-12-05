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


class BTDocumentWithVersionAndElementId(object):
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
        'document_id': 'str',
        'document_version_id': 'str',
        'element_id': 'str',
        'part_number': 'str',
        'revision': 'str',
        'valid_revision_reference': 'bool',
        'unique_version_id': 'str'
    }

    attribute_map = {
        'document_id': 'documentId',
        'document_version_id': 'documentVersionId',
        'element_id': 'elementId',
        'part_number': 'partNumber',
        'revision': 'revision',
        'valid_revision_reference': 'validRevisionReference',
        'unique_version_id': 'uniqueVersionId'
    }

    def __init__(self, document_id=None, document_version_id=None, element_id=None, part_number=None, revision=None, valid_revision_reference=None, unique_version_id=None, local_vars_configuration=None):  # noqa: E501
        """BTDocumentWithVersionAndElementId - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._document_id = None
        self._document_version_id = None
        self._element_id = None
        self._part_number = None
        self._revision = None
        self._valid_revision_reference = None
        self._unique_version_id = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if document_version_id is not None:
            self.document_version_id = document_version_id
        if element_id is not None:
            self.element_id = element_id
        if part_number is not None:
            self.part_number = part_number
        if revision is not None:
            self.revision = revision
        if valid_revision_reference is not None:
            self.valid_revision_reference = valid_revision_reference
        if unique_version_id is not None:
            self.unique_version_id = unique_version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The document_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTDocumentWithVersionAndElementId.


        :param document_id: The document_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_version_id(self):
        """Gets the document_version_id of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The document_version_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: str
        """
        return self._document_version_id

    @document_version_id.setter
    def document_version_id(self, document_version_id):
        """Sets the document_version_id of this BTDocumentWithVersionAndElementId.


        :param document_version_id: The document_version_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: str
        """

        self._document_version_id = document_version_id

    @property
    def element_id(self):
        """Gets the element_id of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The element_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTDocumentWithVersionAndElementId.


        :param element_id: The element_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def part_number(self):
        """Gets the part_number of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The part_number of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTDocumentWithVersionAndElementId.


        :param part_number: The part_number of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def revision(self):
        """Gets the revision of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The revision of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTDocumentWithVersionAndElementId.


        :param revision: The revision of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def valid_revision_reference(self):
        """Gets the valid_revision_reference of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The valid_revision_reference of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: bool
        """
        return self._valid_revision_reference

    @valid_revision_reference.setter
    def valid_revision_reference(self, valid_revision_reference):
        """Sets the valid_revision_reference of this BTDocumentWithVersionAndElementId.


        :param valid_revision_reference: The valid_revision_reference of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: bool
        """

        self._valid_revision_reference = valid_revision_reference

    @property
    def unique_version_id(self):
        """Gets the unique_version_id of this BTDocumentWithVersionAndElementId.  # noqa: E501


        :return: The unique_version_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :rtype: str
        """
        return self._unique_version_id

    @unique_version_id.setter
    def unique_version_id(self, unique_version_id):
        """Sets the unique_version_id of this BTDocumentWithVersionAndElementId.


        :param unique_version_id: The unique_version_id of this BTDocumentWithVersionAndElementId.  # noqa: E501
        :type: str
        """

        self._unique_version_id = unique_version_id

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
        if not isinstance(other, BTDocumentWithVersionAndElementId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTDocumentWithVersionAndElementId):
            return True

        return self.to_dict() != other.to_dict()
