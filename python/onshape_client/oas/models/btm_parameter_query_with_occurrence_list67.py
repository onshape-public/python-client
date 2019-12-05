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


class BTMParameterQueryWithOccurrenceList67(object):
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
        'occurrences': 'list[BTOccurrence74]',
        'queries': 'list[BTMIndividualQueryWithOccurrenceBase904]',
        'parameter_id': 'str',
        'import_microversion': 'str',
        'node_id': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'occurrences': 'occurrences',
        'queries': 'queries',
        'parameter_id': 'parameterId',
        'import_microversion': 'importMicroversion',
        'node_id': 'nodeId',
        'bt_type': 'btType'
    }

    def __init__(self, occurrences=None, queries=None, parameter_id=None, import_microversion=None, node_id=None, bt_type=None, local_vars_configuration=None):  # noqa: E501
        """BTMParameterQueryWithOccurrenceList67 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._occurrences = None
        self._queries = None
        self._parameter_id = None
        self._import_microversion = None
        self._node_id = None
        self._bt_type = None
        self.discriminator = None

        if occurrences is not None:
            self.occurrences = occurrences
        if queries is not None:
            self.queries = queries
        if parameter_id is not None:
            self.parameter_id = parameter_id
        if import_microversion is not None:
            self.import_microversion = import_microversion
        if node_id is not None:
            self.node_id = node_id
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def occurrences(self):
        """Gets the occurrences of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501


        :return: The occurrences of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :rtype: list[BTOccurrence74]
        """
        return self._occurrences

    @occurrences.setter
    def occurrences(self, occurrences):
        """Sets the occurrences of this BTMParameterQueryWithOccurrenceList67.


        :param occurrences: The occurrences of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :type: list[BTOccurrence74]
        """

        self._occurrences = occurrences

    @property
    def queries(self):
        """Gets the queries of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501


        :return: The queries of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :rtype: list[BTMIndividualQueryWithOccurrenceBase904]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this BTMParameterQueryWithOccurrenceList67.


        :param queries: The queries of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :type: list[BTMIndividualQueryWithOccurrenceBase904]
        """

        self._queries = queries

    @property
    def parameter_id(self):
        """Gets the parameter_id of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501


        :return: The parameter_id of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :rtype: str
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this BTMParameterQueryWithOccurrenceList67.


        :param parameter_id: The parameter_id of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :type: str
        """

        self._parameter_id = parameter_id

    @property
    def import_microversion(self):
        """Gets the import_microversion of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501


        :return: The import_microversion of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :rtype: str
        """
        return self._import_microversion

    @import_microversion.setter
    def import_microversion(self, import_microversion):
        """Sets the import_microversion of this BTMParameterQueryWithOccurrenceList67.


        :param import_microversion: The import_microversion of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :type: str
        """

        self._import_microversion = import_microversion

    @property
    def node_id(self):
        """Gets the node_id of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501


        :return: The node_id of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTMParameterQueryWithOccurrenceList67.


        :param node_id: The node_id of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def bt_type(self):
        """Gets the bt_type of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501


        :return: The bt_type of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTMParameterQueryWithOccurrenceList67.


        :param bt_type: The bt_type of this BTMParameterQueryWithOccurrenceList67.  # noqa: E501
        :type: str
        """

        self._bt_type = bt_type

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
        if not isinstance(other, BTMParameterQueryWithOccurrenceList67):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMParameterQueryWithOccurrenceList67):
            return True

        return self.to_dict() != other.to_dict()
