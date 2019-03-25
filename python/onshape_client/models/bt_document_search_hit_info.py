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


class BTDocumentSearchHitInfo(object):
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
        'name': 'str',
        'type': 'str',
        'document_id': 'str',
        'highlighted_fields': 'dict(str, list[str])',
        'source_map': 'dict(str, object)',
        'hit': 'BTESDocumentHit',
        'version_or_workspace_name': 'str',
        'element_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'document_id': 'documentId',
        'highlighted_fields': 'highlightedFields',
        'source_map': 'sourceMap',
        'hit': 'hit',
        'version_or_workspace_name': 'versionOrWorkspaceName',
        'element_name': 'elementName'
    }

    def __init__(self, name=None, type=None, document_id=None, highlighted_fields=None, source_map=None, hit=None, version_or_workspace_name=None, element_name=None):  # noqa: E501
        """BTDocumentSearchHitInfo - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type = None
        self._document_id = None
        self._highlighted_fields = None
        self._source_map = None
        self._hit = None
        self._version_or_workspace_name = None
        self._element_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if document_id is not None:
            self.document_id = document_id
        if highlighted_fields is not None:
            self.highlighted_fields = highlighted_fields
        if source_map is not None:
            self.source_map = source_map
        if hit is not None:
            self.hit = hit
        if version_or_workspace_name is not None:
            self.version_or_workspace_name = version_or_workspace_name
        if element_name is not None:
            self.element_name = element_name

    @property
    def name(self):
        """Gets the name of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The name of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTDocumentSearchHitInfo.


        :param name: The name of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The type of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTDocumentSearchHitInfo.


        :param type: The type of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def document_id(self):
        """Gets the document_id of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The document_id of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTDocumentSearchHitInfo.


        :param document_id: The document_id of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def highlighted_fields(self):
        """Gets the highlighted_fields of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The highlighted_fields of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._highlighted_fields

    @highlighted_fields.setter
    def highlighted_fields(self, highlighted_fields):
        """Sets the highlighted_fields of this BTDocumentSearchHitInfo.


        :param highlighted_fields: The highlighted_fields of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._highlighted_fields = highlighted_fields

    @property
    def source_map(self):
        """Gets the source_map of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The source_map of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._source_map

    @source_map.setter
    def source_map(self, source_map):
        """Sets the source_map of this BTDocumentSearchHitInfo.


        :param source_map: The source_map of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._source_map = source_map

    @property
    def hit(self):
        """Gets the hit of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The hit of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: BTESDocumentHit
        """
        return self._hit

    @hit.setter
    def hit(self, hit):
        """Sets the hit of this BTDocumentSearchHitInfo.


        :param hit: The hit of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: BTESDocumentHit
        """

        self._hit = hit

    @property
    def version_or_workspace_name(self):
        """Gets the version_or_workspace_name of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The version_or_workspace_name of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_or_workspace_name

    @version_or_workspace_name.setter
    def version_or_workspace_name(self, version_or_workspace_name):
        """Sets the version_or_workspace_name of this BTDocumentSearchHitInfo.


        :param version_or_workspace_name: The version_or_workspace_name of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: str
        """

        self._version_or_workspace_name = version_or_workspace_name

    @property
    def element_name(self):
        """Gets the element_name of this BTDocumentSearchHitInfo.  # noqa: E501


        :return: The element_name of this BTDocumentSearchHitInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_name

    @element_name.setter
    def element_name(self, element_name):
        """Sets the element_name of this BTDocumentSearchHitInfo.


        :param element_name: The element_name of this BTDocumentSearchHitInfo.  # noqa: E501
        :type: str
        """

        self._element_name = element_name

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
        if not isinstance(other, BTDocumentSearchHitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
