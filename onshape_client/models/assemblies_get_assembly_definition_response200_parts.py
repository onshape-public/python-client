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


class AssembliesGetAssemblyDefinitionResponse200Parts(object):
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
        'body_type': 'str',
        'part_id': 'str',
        'document_microversion': 'str',
        'document_version': 'str',
        'document_id': 'str',
        'configuration': 'str',
        'element_id': 'str',
        'is_standard_content': 'bool'
    }

    attribute_map = {
        'body_type': 'bodyType',
        'part_id': 'partId',
        'document_microversion': 'documentMicroversion',
        'document_version': 'documentVersion',
        'document_id': 'documentId',
        'configuration': 'configuration',
        'element_id': 'elementId',
        'is_standard_content': 'isStandardContent'
    }

    def __init__(self, body_type=None, part_id=None, document_microversion=None, document_version=None, document_id=None, configuration=None, element_id=None, is_standard_content=None):  # noqa: E501
        """AssembliesGetAssemblyDefinitionResponse200Parts - a model defined in Swagger"""  # noqa: E501

        self._body_type = None
        self._part_id = None
        self._document_microversion = None
        self._document_version = None
        self._document_id = None
        self._configuration = None
        self._element_id = None
        self._is_standard_content = None
        self.discriminator = None

        if body_type is not None:
            self.body_type = body_type
        if part_id is not None:
            self.part_id = part_id
        if document_microversion is not None:
            self.document_microversion = document_microversion
        if document_version is not None:
            self.document_version = document_version
        if document_id is not None:
            self.document_id = document_id
        if configuration is not None:
            self.configuration = configuration
        if element_id is not None:
            self.element_id = element_id
        if is_standard_content is not None:
            self.is_standard_content = is_standard_content

    @property
    def body_type(self):
        """Gets the body_type of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Type of part body. Current values that are possible are solid,             sheet. Others may be added in the future.  # noqa: E501

        :return: The body_type of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Type of part body. Current values that are possible are solid,             sheet. Others may be added in the future.  # noqa: E501

        :param body_type: The body_type of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._body_type = body_type

    @property
    def part_id(self):
        """Gets the part_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Deterministic part ID. If the part cannot be resolved, the value             will be the empty string. This can happen if a change in the source part studio causes the part that             was originally referenced to be missing.  # noqa: E501

        :return: The part_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Deterministic part ID. If the part cannot be resolved, the value             will be the empty string. This can happen if a change in the source part studio causes the part that             was originally referenced to be missing.  # noqa: E501

        :param part_id: The part_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def document_microversion(self):
        """Gets the document_microversion of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Document microversion ID of the document containing             the part  # noqa: E501

        :return: The document_microversion of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._document_microversion

    @document_microversion.setter
    def document_microversion(self, document_microversion):
        """Sets the document_microversion of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Document microversion ID of the document containing             the part  # noqa: E501

        :param document_microversion: The document_microversion of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._document_microversion = document_microversion

    @property
    def document_version(self):
        """Gets the document_version of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Version ID of document containing the part, if reached             through one or more version references  # noqa: E501

        :return: The document_version of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._document_version

    @document_version.setter
    def document_version(self, document_version):
        """Sets the document_version of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Version ID of document containing the part, if reached             through one or more version references  # noqa: E501

        :param document_version: The document_version of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._document_version = document_version

    @property
    def document_id(self):
        """Gets the document_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Document ID of the document containing the part  # noqa: E501

        :return: The document_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Document ID of the document containing the part  # noqa: E501

        :param document_id: The document_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def configuration(self):
        """Gets the configuration of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Configuration of the Part studio element.  # noqa: E501

        :return: The configuration of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Configuration of the Part studio element.  # noqa: E501

        :param configuration: The configuration of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def element_id(self):
        """Gets the element_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Element ID  # noqa: E501

        :return: The element_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Element ID  # noqa: E501

        :param element_id: The element_id of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def is_standard_content(self):
        """Gets the is_standard_content of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501

        Indicates whether the part is Standard Content.  # noqa: E501

        :return: The is_standard_content of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :rtype: bool
        """
        return self._is_standard_content

    @is_standard_content.setter
    def is_standard_content(self, is_standard_content):
        """Sets the is_standard_content of this AssembliesGetAssemblyDefinitionResponse200Parts.

        Indicates whether the part is Standard Content.  # noqa: E501

        :param is_standard_content: The is_standard_content of this AssembliesGetAssemblyDefinitionResponse200Parts.  # noqa: E501
        :type: bool
        """

        self._is_standard_content = is_standard_content

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
        if not isinstance(other, AssembliesGetAssemblyDefinitionResponse200Parts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
