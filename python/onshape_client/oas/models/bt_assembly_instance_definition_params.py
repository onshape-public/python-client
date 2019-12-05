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


class BTAssemblyInstanceDefinitionParams(object):
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
        'microversion_id': 'str',
        'part_number': 'str',
        'document_id': 'str',
        'element_id': 'str',
        'version_id': 'str',
        'revision': 'str',
        'part_id': 'str',
        'configuration': 'str',
        'feature_id': 'str',
        'is_hidden': 'bool',
        'is_suppressed': 'bool',
        'is_assembly': 'bool',
        'is_whole_part_studio': 'bool'
    }

    attribute_map = {
        'microversion_id': 'microversionId',
        'part_number': 'partNumber',
        'document_id': 'documentId',
        'element_id': 'elementId',
        'version_id': 'versionId',
        'revision': 'revision',
        'part_id': 'partId',
        'configuration': 'configuration',
        'feature_id': 'featureId',
        'is_hidden': 'isHidden',
        'is_suppressed': 'isSuppressed',
        'is_assembly': 'isAssembly',
        'is_whole_part_studio': 'isWholePartStudio'
    }

    def __init__(self, microversion_id=None, part_number=None, document_id=None, element_id=None, version_id=None, revision=None, part_id=None, configuration=None, feature_id=None, is_hidden=None, is_suppressed=None, is_assembly=None, is_whole_part_studio=None, local_vars_configuration=None):  # noqa: E501
        """BTAssemblyInstanceDefinitionParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._microversion_id = None
        self._part_number = None
        self._document_id = None
        self._element_id = None
        self._version_id = None
        self._revision = None
        self._part_id = None
        self._configuration = None
        self._feature_id = None
        self._is_hidden = None
        self._is_suppressed = None
        self._is_assembly = None
        self._is_whole_part_studio = None
        self.discriminator = None

        if microversion_id is not None:
            self.microversion_id = microversion_id
        if part_number is not None:
            self.part_number = part_number
        if document_id is not None:
            self.document_id = document_id
        if element_id is not None:
            self.element_id = element_id
        if version_id is not None:
            self.version_id = version_id
        if revision is not None:
            self.revision = revision
        if part_id is not None:
            self.part_id = part_id
        if configuration is not None:
            self.configuration = configuration
        if feature_id is not None:
            self.feature_id = feature_id
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if is_suppressed is not None:
            self.is_suppressed = is_suppressed
        if is_assembly is not None:
            self.is_assembly = is_assembly
        if is_whole_part_studio is not None:
            self.is_whole_part_studio = is_whole_part_studio

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The microversion_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTAssemblyInstanceDefinitionParams.


        :param microversion_id: The microversion_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def part_number(self):
        """Gets the part_number of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The part_number of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this BTAssemblyInstanceDefinitionParams.


        :param part_number: The part_number of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def document_id(self):
        """Gets the document_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The document_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTAssemblyInstanceDefinitionParams.


        :param document_id: The document_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def element_id(self):
        """Gets the element_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The element_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTAssemblyInstanceDefinitionParams.


        :param element_id: The element_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def version_id(self):
        """Gets the version_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The version_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTAssemblyInstanceDefinitionParams.


        :param version_id: The version_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def revision(self):
        """Gets the revision of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The revision of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this BTAssemblyInstanceDefinitionParams.


        :param revision: The revision of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def part_id(self):
        """Gets the part_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The part_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTAssemblyInstanceDefinitionParams.


        :param part_id: The part_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def configuration(self):
        """Gets the configuration of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The configuration of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTAssemblyInstanceDefinitionParams.


        :param configuration: The configuration of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def feature_id(self):
        """Gets the feature_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The feature_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this BTAssemblyInstanceDefinitionParams.


        :param feature_id: The feature_id of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def is_hidden(self):
        """Gets the is_hidden of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The is_hidden of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this BTAssemblyInstanceDefinitionParams.


        :param is_hidden: The is_hidden of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def is_suppressed(self):
        """Gets the is_suppressed of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The is_suppressed of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_suppressed

    @is_suppressed.setter
    def is_suppressed(self, is_suppressed):
        """Sets the is_suppressed of this BTAssemblyInstanceDefinitionParams.


        :param is_suppressed: The is_suppressed of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: bool
        """

        self._is_suppressed = is_suppressed

    @property
    def is_assembly(self):
        """Gets the is_assembly of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The is_assembly of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_assembly

    @is_assembly.setter
    def is_assembly(self, is_assembly):
        """Sets the is_assembly of this BTAssemblyInstanceDefinitionParams.


        :param is_assembly: The is_assembly of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: bool
        """

        self._is_assembly = is_assembly

    @property
    def is_whole_part_studio(self):
        """Gets the is_whole_part_studio of this BTAssemblyInstanceDefinitionParams.  # noqa: E501


        :return: The is_whole_part_studio of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_whole_part_studio

    @is_whole_part_studio.setter
    def is_whole_part_studio(self, is_whole_part_studio):
        """Sets the is_whole_part_studio of this BTAssemblyInstanceDefinitionParams.


        :param is_whole_part_studio: The is_whole_part_studio of this BTAssemblyInstanceDefinitionParams.  # noqa: E501
        :type: bool
        """

        self._is_whole_part_studio = is_whole_part_studio

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
        if not isinstance(other, BTAssemblyInstanceDefinitionParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTAssemblyInstanceDefinitionParams):
            return True

        return self.to_dict() != other.to_dict()
