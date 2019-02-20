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


class BTUniqueDocumentItemParams(object):
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
        'revision': 'str',
        'version_id': 'str',
        'document_id': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'element_type': 'str',
        'part_number': 'str',
        'part_id': 'str',
        'api_configuration': 'str'
    }

    attribute_map = {
        'revision': 'revision',
        'version_id': 'versionId',
        'document_id': 'documentId',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'element_type': 'elementType',
        'part_number': 'partNumber',
        'part_id': 'partId',
        'api_configuration': 'apiConfiguration'
    }

    def __init__(self, revision=None, version_id=None, document_id=None, workspace_id=None, element_id=None, element_type=None, part_number=None, part_id=None, api_configuration=None):  # noqa: E501
        """BTUniqueDocumentItemParams - a model defined in OpenAPI"""  # noqa: E501

        self._revision = None
        self._version_id = None
        self._document_id = None
        self._workspace_id = None
        self._element_id = None
        self._element_type = None
        self._part_number = None
        self._part_id = None
        self._api_configuration = None
        self.discriminator = None

        if revision is not None:
            self.revision = revision
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if element_type is not None:
            self.element_type = element_type
        if part_number is not None:
            self.part_number = part_number
        if part_id is not None:
            self.part_id = part_id
        if api_configuration is not None:
            self.api_configuration = api_configuration

    @property
    def revision(self):
        """Gets the revision of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The revision of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTUniqueDocumentItemParams.


        :param revision: The revision of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def version_id(self):
        """Gets the version_id of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The version_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTUniqueDocumentItemParams.


        :param version_id: The version_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The document_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTUniqueDocumentItemParams.


        :param document_id: The document_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The workspace_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTUniqueDocumentItemParams.


        :param workspace_id: The workspace_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The element_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTUniqueDocumentItemParams.


        :param element_id: The element_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def element_type(self):
        """Gets the element_type of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The element_type of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTUniqueDocumentItemParams.


        :param element_type: The element_type of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._element_type = element_type

    @property
    def part_number(self):
        """Gets the part_number of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The part_number of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTUniqueDocumentItemParams.


        :param part_number: The part_number of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def part_id(self):
        """Gets the part_id of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The part_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTUniqueDocumentItemParams.


        :param part_id: The part_id of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def api_configuration(self):
        """Gets the api_configuration of this BTUniqueDocumentItemParams.  # noqa: E501


        :return: The api_configuration of this BTUniqueDocumentItemParams.  # noqa: E501
        :rtype: str
        """
        return self._api_configuration

    @api_configuration.setter
    def api_configuration(self, api_configuration):
        """Sets the api_configuration of this BTUniqueDocumentItemParams.


        :param api_configuration: The api_configuration of this BTUniqueDocumentItemParams.  # noqa: E501
        :type: str
        """

        self._api_configuration = api_configuration

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
        if not isinstance(other, BTUniqueDocumentItemParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
