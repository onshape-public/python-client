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


class BTAssociativeDataParams(object):
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
        'type': 'str',
        'microversion_id': 'str',
        'document_microversion': 'str',
        'associative_data_id': 'str',
        'operation': 'str',
        'view_id': 'str',
        'occurrence_id': 'str',
        'is_hidden_base_view': 'bool',
        'configuration': 'str',
        'version_id': 'str',
        'document_id': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'data': 'list[BTNameValuePair]',
        'id_tag': 'str'
    }

    attribute_map = {
        'type': 'type',
        'microversion_id': 'microversionId',
        'document_microversion': 'documentMicroversion',
        'associative_data_id': 'associativeDataId',
        'operation': 'operation',
        'view_id': 'viewId',
        'occurrence_id': 'occurrenceId',
        'is_hidden_base_view': 'isHiddenBaseView',
        'configuration': 'configuration',
        'version_id': 'versionId',
        'document_id': 'documentId',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'data': 'data',
        'id_tag': 'idTag'
    }

    def __init__(self, type=None, microversion_id=None, document_microversion=None, associative_data_id=None, operation=None, view_id=None, occurrence_id=None, is_hidden_base_view=None, configuration=None, version_id=None, document_id=None, workspace_id=None, element_id=None, data=None, id_tag=None):  # noqa: E501
        """BTAssociativeDataParams - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._microversion_id = None
        self._document_microversion = None
        self._associative_data_id = None
        self._operation = None
        self._view_id = None
        self._occurrence_id = None
        self._is_hidden_base_view = None
        self._configuration = None
        self._version_id = None
        self._document_id = None
        self._workspace_id = None
        self._element_id = None
        self._data = None
        self._id_tag = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if document_microversion is not None:
            self.document_microversion = document_microversion
        if associative_data_id is not None:
            self.associative_data_id = associative_data_id
        if operation is not None:
            self.operation = operation
        if view_id is not None:
            self.view_id = view_id
        if occurrence_id is not None:
            self.occurrence_id = occurrence_id
        if is_hidden_base_view is not None:
            self.is_hidden_base_view = is_hidden_base_view
        if configuration is not None:
            self.configuration = configuration
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if data is not None:
            self.data = data
        if id_tag is not None:
            self.id_tag = id_tag

    @property
    def type(self):
        """Gets the type of this BTAssociativeDataParams.  # noqa: E501


        :return: The type of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTAssociativeDataParams.


        :param type: The type of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONSHAPE_DRAWING_VIEW", "MODEL_TOPOLOGY", "MODEL_DEFINITION_FEATURE", "MODEL_DEFINITION_ENTITY", "UNKNOWN"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The microversion_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTAssociativeDataParams.


        :param microversion_id: The microversion_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def document_microversion(self):
        """Gets the document_microversion of this BTAssociativeDataParams.  # noqa: E501


        :return: The document_microversion of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._document_microversion

    @document_microversion.setter
    def document_microversion(self, document_microversion):
        """Sets the document_microversion of this BTAssociativeDataParams.


        :param document_microversion: The document_microversion of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._document_microversion = document_microversion

    @property
    def associative_data_id(self):
        """Gets the associative_data_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The associative_data_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._associative_data_id

    @associative_data_id.setter
    def associative_data_id(self, associative_data_id):
        """Sets the associative_data_id of this BTAssociativeDataParams.


        :param associative_data_id: The associative_data_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._associative_data_id = associative_data_id

    @property
    def operation(self):
        """Gets the operation of this BTAssociativeDataParams.  # noqa: E501


        :return: The operation of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this BTAssociativeDataParams.


        :param operation: The operation of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADD", "REMOVE", "UPDATE"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def view_id(self):
        """Gets the view_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The view_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._view_id

    @view_id.setter
    def view_id(self, view_id):
        """Sets the view_id of this BTAssociativeDataParams.


        :param view_id: The view_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._view_id = view_id

    @property
    def occurrence_id(self):
        """Gets the occurrence_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The occurrence_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._occurrence_id

    @occurrence_id.setter
    def occurrence_id(self, occurrence_id):
        """Sets the occurrence_id of this BTAssociativeDataParams.


        :param occurrence_id: The occurrence_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._occurrence_id = occurrence_id

    @property
    def is_hidden_base_view(self):
        """Gets the is_hidden_base_view of this BTAssociativeDataParams.  # noqa: E501


        :return: The is_hidden_base_view of this BTAssociativeDataParams.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden_base_view

    @is_hidden_base_view.setter
    def is_hidden_base_view(self, is_hidden_base_view):
        """Sets the is_hidden_base_view of this BTAssociativeDataParams.


        :param is_hidden_base_view: The is_hidden_base_view of this BTAssociativeDataParams.  # noqa: E501
        :type: bool
        """

        self._is_hidden_base_view = is_hidden_base_view

    @property
    def configuration(self):
        """Gets the configuration of this BTAssociativeDataParams.  # noqa: E501


        :return: The configuration of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this BTAssociativeDataParams.


        :param configuration: The configuration of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def version_id(self):
        """Gets the version_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The version_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTAssociativeDataParams.


        :param version_id: The version_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The document_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTAssociativeDataParams.


        :param document_id: The document_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The workspace_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTAssociativeDataParams.


        :param workspace_id: The workspace_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTAssociativeDataParams.  # noqa: E501


        :return: The element_id of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTAssociativeDataParams.


        :param element_id: The element_id of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def data(self):
        """Gets the data of this BTAssociativeDataParams.  # noqa: E501


        :return: The data of this BTAssociativeDataParams.  # noqa: E501
        :rtype: list[BTNameValuePair]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BTAssociativeDataParams.


        :param data: The data of this BTAssociativeDataParams.  # noqa: E501
        :type: list[BTNameValuePair]
        """

        self._data = data

    @property
    def id_tag(self):
        """Gets the id_tag of this BTAssociativeDataParams.  # noqa: E501


        :return: The id_tag of this BTAssociativeDataParams.  # noqa: E501
        :rtype: str
        """
        return self._id_tag

    @id_tag.setter
    def id_tag(self, id_tag):
        """Sets the id_tag of this BTAssociativeDataParams.


        :param id_tag: The id_tag of this BTAssociativeDataParams.  # noqa: E501
        :type: str
        """

        self._id_tag = id_tag

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
        if not isinstance(other, BTAssociativeDataParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
