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


class BTFeatureListResponse(object):
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
        'is_complete': 'bool',
        'feature_states': 'dict(str, BTFeatureState)',
        'features': 'list[BTMFeature]',
        'default_features': 'list[BTMFeature]',
        'imports': 'list[BTMImport]',
        'rollback_index': 'int',
        'bel_script_library_version': 'BTBelScriptLibraryVersion',
        'serialization_version': 'str',
        'library_version': 'int',
        'source_microversion': 'str',
        'reject_microversion_skew': 'bool',
        'microversion_skew': 'bool',
        'type_id': 'int',
        'export_type_name': 'str',
        'connection_source': 'BTConnection',
        'unknown_class': 'bool'
    }

    attribute_map = {
        'is_complete': 'isComplete',
        'feature_states': 'featureStates',
        'features': 'features',
        'default_features': 'defaultFeatures',
        'imports': 'imports',
        'rollback_index': 'rollbackIndex',
        'bel_script_library_version': 'belScriptLibraryVersion',
        'serialization_version': 'serializationVersion',
        'library_version': 'libraryVersion',
        'source_microversion': 'sourceMicroversion',
        'reject_microversion_skew': 'rejectMicroversionSkew',
        'microversion_skew': 'microversionSkew',
        'type_id': 'typeId',
        'export_type_name': 'exportTypeName',
        'connection_source': 'connectionSource',
        'unknown_class': 'unknownClass'
    }

    def __init__(self, is_complete=None, feature_states=None, features=None, default_features=None, imports=None, rollback_index=None, bel_script_library_version=None, serialization_version=None, library_version=None, source_microversion=None, reject_microversion_skew=None, microversion_skew=None, type_id=None, export_type_name=None, connection_source=None, unknown_class=None):  # noqa: E501
        """BTFeatureListResponse - a model defined in OpenAPI"""  # noqa: E501

        self._is_complete = None
        self._feature_states = None
        self._features = None
        self._default_features = None
        self._imports = None
        self._rollback_index = None
        self._bel_script_library_version = None
        self._serialization_version = None
        self._library_version = None
        self._source_microversion = None
        self._reject_microversion_skew = None
        self._microversion_skew = None
        self._type_id = None
        self._export_type_name = None
        self._connection_source = None
        self._unknown_class = None
        self.discriminator = None

        if is_complete is not None:
            self.is_complete = is_complete
        if feature_states is not None:
            self.feature_states = feature_states
        if features is not None:
            self.features = features
        if default_features is not None:
            self.default_features = default_features
        if imports is not None:
            self.imports = imports
        if rollback_index is not None:
            self.rollback_index = rollback_index
        if bel_script_library_version is not None:
            self.bel_script_library_version = bel_script_library_version
        if serialization_version is not None:
            self.serialization_version = serialization_version
        if library_version is not None:
            self.library_version = library_version
        if source_microversion is not None:
            self.source_microversion = source_microversion
        if reject_microversion_skew is not None:
            self.reject_microversion_skew = reject_microversion_skew
        if microversion_skew is not None:
            self.microversion_skew = microversion_skew
        if type_id is not None:
            self.type_id = type_id
        if export_type_name is not None:
            self.export_type_name = export_type_name
        if connection_source is not None:
            self.connection_source = connection_source
        if unknown_class is not None:
            self.unknown_class = unknown_class

    @property
    def is_complete(self):
        """Gets the is_complete of this BTFeatureListResponse.  # noqa: E501


        :return: The is_complete of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this BTFeatureListResponse.


        :param is_complete: The is_complete of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

    @property
    def feature_states(self):
        """Gets the feature_states of this BTFeatureListResponse.  # noqa: E501


        :return: The feature_states of this BTFeatureListResponse.  # noqa: E501
        :rtype: dict(str, BTFeatureState)
        """
        return self._feature_states

    @feature_states.setter
    def feature_states(self, feature_states):
        """Sets the feature_states of this BTFeatureListResponse.


        :param feature_states: The feature_states of this BTFeatureListResponse.  # noqa: E501
        :type: dict(str, BTFeatureState)
        """

        self._feature_states = feature_states

    @property
    def features(self):
        """Gets the features of this BTFeatureListResponse.  # noqa: E501


        :return: The features of this BTFeatureListResponse.  # noqa: E501
        :rtype: list[BTMFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this BTFeatureListResponse.


        :param features: The features of this BTFeatureListResponse.  # noqa: E501
        :type: list[BTMFeature]
        """

        self._features = features

    @property
    def default_features(self):
        """Gets the default_features of this BTFeatureListResponse.  # noqa: E501


        :return: The default_features of this BTFeatureListResponse.  # noqa: E501
        :rtype: list[BTMFeature]
        """
        return self._default_features

    @default_features.setter
    def default_features(self, default_features):
        """Sets the default_features of this BTFeatureListResponse.


        :param default_features: The default_features of this BTFeatureListResponse.  # noqa: E501
        :type: list[BTMFeature]
        """

        self._default_features = default_features

    @property
    def imports(self):
        """Gets the imports of this BTFeatureListResponse.  # noqa: E501


        :return: The imports of this BTFeatureListResponse.  # noqa: E501
        :rtype: list[BTMImport]
        """
        return self._imports

    @imports.setter
    def imports(self, imports):
        """Sets the imports of this BTFeatureListResponse.


        :param imports: The imports of this BTFeatureListResponse.  # noqa: E501
        :type: list[BTMImport]
        """

        self._imports = imports

    @property
    def rollback_index(self):
        """Gets the rollback_index of this BTFeatureListResponse.  # noqa: E501


        :return: The rollback_index of this BTFeatureListResponse.  # noqa: E501
        :rtype: int
        """
        return self._rollback_index

    @rollback_index.setter
    def rollback_index(self, rollback_index):
        """Sets the rollback_index of this BTFeatureListResponse.


        :param rollback_index: The rollback_index of this BTFeatureListResponse.  # noqa: E501
        :type: int
        """

        self._rollback_index = rollback_index

    @property
    def bel_script_library_version(self):
        """Gets the bel_script_library_version of this BTFeatureListResponse.  # noqa: E501


        :return: The bel_script_library_version of this BTFeatureListResponse.  # noqa: E501
        :rtype: BTBelScriptLibraryVersion
        """
        return self._bel_script_library_version

    @bel_script_library_version.setter
    def bel_script_library_version(self, bel_script_library_version):
        """Sets the bel_script_library_version of this BTFeatureListResponse.


        :param bel_script_library_version: The bel_script_library_version of this BTFeatureListResponse.  # noqa: E501
        :type: BTBelScriptLibraryVersion
        """

        self._bel_script_library_version = bel_script_library_version

    @property
    def serialization_version(self):
        """Gets the serialization_version of this BTFeatureListResponse.  # noqa: E501


        :return: The serialization_version of this BTFeatureListResponse.  # noqa: E501
        :rtype: str
        """
        return self._serialization_version

    @serialization_version.setter
    def serialization_version(self, serialization_version):
        """Sets the serialization_version of this BTFeatureListResponse.


        :param serialization_version: The serialization_version of this BTFeatureListResponse.  # noqa: E501
        :type: str
        """

        self._serialization_version = serialization_version

    @property
    def library_version(self):
        """Gets the library_version of this BTFeatureListResponse.  # noqa: E501


        :return: The library_version of this BTFeatureListResponse.  # noqa: E501
        :rtype: int
        """
        return self._library_version

    @library_version.setter
    def library_version(self, library_version):
        """Sets the library_version of this BTFeatureListResponse.


        :param library_version: The library_version of this BTFeatureListResponse.  # noqa: E501
        :type: int
        """

        self._library_version = library_version

    @property
    def source_microversion(self):
        """Gets the source_microversion of this BTFeatureListResponse.  # noqa: E501


        :return: The source_microversion of this BTFeatureListResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_microversion

    @source_microversion.setter
    def source_microversion(self, source_microversion):
        """Sets the source_microversion of this BTFeatureListResponse.


        :param source_microversion: The source_microversion of this BTFeatureListResponse.  # noqa: E501
        :type: str
        """

        self._source_microversion = source_microversion

    @property
    def reject_microversion_skew(self):
        """Gets the reject_microversion_skew of this BTFeatureListResponse.  # noqa: E501


        :return: The reject_microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._reject_microversion_skew

    @reject_microversion_skew.setter
    def reject_microversion_skew(self, reject_microversion_skew):
        """Sets the reject_microversion_skew of this BTFeatureListResponse.


        :param reject_microversion_skew: The reject_microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._reject_microversion_skew = reject_microversion_skew

    @property
    def microversion_skew(self):
        """Gets the microversion_skew of this BTFeatureListResponse.  # noqa: E501


        :return: The microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._microversion_skew

    @microversion_skew.setter
    def microversion_skew(self, microversion_skew):
        """Sets the microversion_skew of this BTFeatureListResponse.


        :param microversion_skew: The microversion_skew of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._microversion_skew = microversion_skew

    @property
    def type_id(self):
        """Gets the type_id of this BTFeatureListResponse.  # noqa: E501


        :return: The type_id of this BTFeatureListResponse.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this BTFeatureListResponse.


        :param type_id: The type_id of this BTFeatureListResponse.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def export_type_name(self):
        """Gets the export_type_name of this BTFeatureListResponse.  # noqa: E501


        :return: The export_type_name of this BTFeatureListResponse.  # noqa: E501
        :rtype: str
        """
        return self._export_type_name

    @export_type_name.setter
    def export_type_name(self, export_type_name):
        """Sets the export_type_name of this BTFeatureListResponse.


        :param export_type_name: The export_type_name of this BTFeatureListResponse.  # noqa: E501
        :type: str
        """

        self._export_type_name = export_type_name

    @property
    def connection_source(self):
        """Gets the connection_source of this BTFeatureListResponse.  # noqa: E501


        :return: The connection_source of this BTFeatureListResponse.  # noqa: E501
        :rtype: BTConnection
        """
        return self._connection_source

    @connection_source.setter
    def connection_source(self, connection_source):
        """Sets the connection_source of this BTFeatureListResponse.


        :param connection_source: The connection_source of this BTFeatureListResponse.  # noqa: E501
        :type: BTConnection
        """

        self._connection_source = connection_source

    @property
    def unknown_class(self):
        """Gets the unknown_class of this BTFeatureListResponse.  # noqa: E501


        :return: The unknown_class of this BTFeatureListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_class

    @unknown_class.setter
    def unknown_class(self, unknown_class):
        """Sets the unknown_class of this BTFeatureListResponse.


        :param unknown_class: The unknown_class of this BTFeatureListResponse.  # noqa: E501
        :type: bool
        """

        self._unknown_class = unknown_class

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
        if not isinstance(other, BTFeatureListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
