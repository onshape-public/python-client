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


class BTOccurrenceFilter166AllOf(object):
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
        'solid_or_composite_body_only': 'bool',
        'exclude_sub_assemblies': 'bool',
        'exclude_suppressed': 'bool',
        'exclude_flattened_parts': 'bool',
        'exclude_pattern_instances': 'bool',
        'include_pattern_occurrence': 'bool',
        'exclude_studio_inserts': 'bool',
        'exclude_standard_content': 'bool',
        'include_assembly_root': 'bool',
        'top_level_only': 'bool'
    }

    attribute_map = {
        'solid_or_composite_body_only': 'solidOrCompositeBodyOnly',
        'exclude_sub_assemblies': 'excludeSubAssemblies',
        'exclude_suppressed': 'excludeSuppressed',
        'exclude_flattened_parts': 'excludeFlattenedParts',
        'exclude_pattern_instances': 'excludePatternInstances',
        'include_pattern_occurrence': 'includePatternOccurrence',
        'exclude_studio_inserts': 'excludeStudioInserts',
        'exclude_standard_content': 'excludeStandardContent',
        'include_assembly_root': 'includeAssemblyRoot',
        'top_level_only': 'topLevelOnly'
    }

    def __init__(self, solid_or_composite_body_only=None, exclude_sub_assemblies=None, exclude_suppressed=None, exclude_flattened_parts=None, exclude_pattern_instances=None, include_pattern_occurrence=None, exclude_studio_inserts=None, exclude_standard_content=None, include_assembly_root=None, top_level_only=None, local_vars_configuration=None):  # noqa: E501
        """BTOccurrenceFilter166AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._solid_or_composite_body_only = None
        self._exclude_sub_assemblies = None
        self._exclude_suppressed = None
        self._exclude_flattened_parts = None
        self._exclude_pattern_instances = None
        self._include_pattern_occurrence = None
        self._exclude_studio_inserts = None
        self._exclude_standard_content = None
        self._include_assembly_root = None
        self._top_level_only = None
        self.discriminator = None

        if solid_or_composite_body_only is not None:
            self.solid_or_composite_body_only = solid_or_composite_body_only
        if exclude_sub_assemblies is not None:
            self.exclude_sub_assemblies = exclude_sub_assemblies
        if exclude_suppressed is not None:
            self.exclude_suppressed = exclude_suppressed
        if exclude_flattened_parts is not None:
            self.exclude_flattened_parts = exclude_flattened_parts
        if exclude_pattern_instances is not None:
            self.exclude_pattern_instances = exclude_pattern_instances
        if include_pattern_occurrence is not None:
            self.include_pattern_occurrence = include_pattern_occurrence
        if exclude_studio_inserts is not None:
            self.exclude_studio_inserts = exclude_studio_inserts
        if exclude_standard_content is not None:
            self.exclude_standard_content = exclude_standard_content
        if include_assembly_root is not None:
            self.include_assembly_root = include_assembly_root
        if top_level_only is not None:
            self.top_level_only = top_level_only

    @property
    def solid_or_composite_body_only(self):
        """Gets the solid_or_composite_body_only of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The solid_or_composite_body_only of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._solid_or_composite_body_only

    @solid_or_composite_body_only.setter
    def solid_or_composite_body_only(self, solid_or_composite_body_only):
        """Sets the solid_or_composite_body_only of this BTOccurrenceFilter166AllOf.


        :param solid_or_composite_body_only: The solid_or_composite_body_only of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._solid_or_composite_body_only = solid_or_composite_body_only

    @property
    def exclude_sub_assemblies(self):
        """Gets the exclude_sub_assemblies of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The exclude_sub_assemblies of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_sub_assemblies

    @exclude_sub_assemblies.setter
    def exclude_sub_assemblies(self, exclude_sub_assemblies):
        """Sets the exclude_sub_assemblies of this BTOccurrenceFilter166AllOf.


        :param exclude_sub_assemblies: The exclude_sub_assemblies of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._exclude_sub_assemblies = exclude_sub_assemblies

    @property
    def exclude_suppressed(self):
        """Gets the exclude_suppressed of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The exclude_suppressed of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_suppressed

    @exclude_suppressed.setter
    def exclude_suppressed(self, exclude_suppressed):
        """Sets the exclude_suppressed of this BTOccurrenceFilter166AllOf.


        :param exclude_suppressed: The exclude_suppressed of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._exclude_suppressed = exclude_suppressed

    @property
    def exclude_flattened_parts(self):
        """Gets the exclude_flattened_parts of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The exclude_flattened_parts of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_flattened_parts

    @exclude_flattened_parts.setter
    def exclude_flattened_parts(self, exclude_flattened_parts):
        """Sets the exclude_flattened_parts of this BTOccurrenceFilter166AllOf.


        :param exclude_flattened_parts: The exclude_flattened_parts of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._exclude_flattened_parts = exclude_flattened_parts

    @property
    def exclude_pattern_instances(self):
        """Gets the exclude_pattern_instances of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The exclude_pattern_instances of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_pattern_instances

    @exclude_pattern_instances.setter
    def exclude_pattern_instances(self, exclude_pattern_instances):
        """Sets the exclude_pattern_instances of this BTOccurrenceFilter166AllOf.


        :param exclude_pattern_instances: The exclude_pattern_instances of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._exclude_pattern_instances = exclude_pattern_instances

    @property
    def include_pattern_occurrence(self):
        """Gets the include_pattern_occurrence of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The include_pattern_occurrence of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._include_pattern_occurrence

    @include_pattern_occurrence.setter
    def include_pattern_occurrence(self, include_pattern_occurrence):
        """Sets the include_pattern_occurrence of this BTOccurrenceFilter166AllOf.


        :param include_pattern_occurrence: The include_pattern_occurrence of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._include_pattern_occurrence = include_pattern_occurrence

    @property
    def exclude_studio_inserts(self):
        """Gets the exclude_studio_inserts of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The exclude_studio_inserts of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_studio_inserts

    @exclude_studio_inserts.setter
    def exclude_studio_inserts(self, exclude_studio_inserts):
        """Sets the exclude_studio_inserts of this BTOccurrenceFilter166AllOf.


        :param exclude_studio_inserts: The exclude_studio_inserts of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._exclude_studio_inserts = exclude_studio_inserts

    @property
    def exclude_standard_content(self):
        """Gets the exclude_standard_content of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The exclude_standard_content of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_standard_content

    @exclude_standard_content.setter
    def exclude_standard_content(self, exclude_standard_content):
        """Sets the exclude_standard_content of this BTOccurrenceFilter166AllOf.


        :param exclude_standard_content: The exclude_standard_content of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._exclude_standard_content = exclude_standard_content

    @property
    def include_assembly_root(self):
        """Gets the include_assembly_root of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The include_assembly_root of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._include_assembly_root

    @include_assembly_root.setter
    def include_assembly_root(self, include_assembly_root):
        """Sets the include_assembly_root of this BTOccurrenceFilter166AllOf.


        :param include_assembly_root: The include_assembly_root of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._include_assembly_root = include_assembly_root

    @property
    def top_level_only(self):
        """Gets the top_level_only of this BTOccurrenceFilter166AllOf.  # noqa: E501


        :return: The top_level_only of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._top_level_only

    @top_level_only.setter
    def top_level_only(self, top_level_only):
        """Sets the top_level_only of this BTOccurrenceFilter166AllOf.


        :param top_level_only: The top_level_only of this BTOccurrenceFilter166AllOf.  # noqa: E501
        :type: bool
        """

        self._top_level_only = top_level_only

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
        if not isinstance(other, BTOccurrenceFilter166AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTOccurrenceFilter166AllOf):
            return True

        return self.to_dict() != other.to_dict()
