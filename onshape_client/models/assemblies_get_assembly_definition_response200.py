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

from onshape_client.models.assemblies_get_assembly_definition_response200_part_studio_features import AssembliesGetAssemblyDefinitionResponse200PartStudioFeatures  # noqa: F401,E501
from onshape_client.models.assemblies_get_assembly_definition_response200_parts import AssembliesGetAssemblyDefinitionResponse200Parts  # noqa: F401,E501
from onshape_client.models.assemblies_get_assembly_definition_response200_root_assembly import AssembliesGetAssemblyDefinitionResponse200RootAssembly  # noqa: F401,E501
from onshape_client.models.assemblies_get_assembly_definition_response200_sub_assemblies import AssembliesGetAssemblyDefinitionResponse200SubAssemblies  # noqa: F401,E501


class AssembliesGetAssemblyDefinitionResponse200(object):
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
        'root_assembly': 'AssembliesGetAssemblyDefinitionResponse200RootAssembly',
        'sub_assemblies': 'list[AssembliesGetAssemblyDefinitionResponse200SubAssemblies]',
        'parts': 'list[AssembliesGetAssemblyDefinitionResponse200Parts]',
        'part_studio_features': 'list[AssembliesGetAssemblyDefinitionResponse200PartStudioFeatures]'
    }

    attribute_map = {
        'root_assembly': 'rootAssembly',
        'sub_assemblies': 'subAssemblies',
        'parts': 'parts',
        'part_studio_features': 'partStudioFeatures'
    }

    def __init__(self, root_assembly=None, sub_assemblies=None, parts=None, part_studio_features=None):  # noqa: E501
        """AssembliesGetAssemblyDefinitionResponse200 - a model defined in Swagger"""  # noqa: E501

        self._root_assembly = None
        self._sub_assemblies = None
        self._parts = None
        self._part_studio_features = None
        self.discriminator = None

        if root_assembly is not None:
            self.root_assembly = root_assembly
        if sub_assemblies is not None:
            self.sub_assemblies = sub_assemblies
        if parts is not None:
            self.parts = parts
        if part_studio_features is not None:
            self.part_studio_features = part_studio_features

    @property
    def root_assembly(self):
        """Gets the root_assembly of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501


        :return: The root_assembly of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :rtype: AssembliesGetAssemblyDefinitionResponse200RootAssembly
        """
        return self._root_assembly

    @root_assembly.setter
    def root_assembly(self, root_assembly):
        """Sets the root_assembly of this AssembliesGetAssemblyDefinitionResponse200.


        :param root_assembly: The root_assembly of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :type: AssembliesGetAssemblyDefinitionResponse200RootAssembly
        """

        self._root_assembly = root_assembly

    @property
    def sub_assemblies(self):
        """Gets the sub_assemblies of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501

        Array of sub-assemblies  # noqa: E501

        :return: The sub_assemblies of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :rtype: list[AssembliesGetAssemblyDefinitionResponse200SubAssemblies]
        """
        return self._sub_assemblies

    @sub_assemblies.setter
    def sub_assemblies(self, sub_assemblies):
        """Sets the sub_assemblies of this AssembliesGetAssemblyDefinitionResponse200.

        Array of sub-assemblies  # noqa: E501

        :param sub_assemblies: The sub_assemblies of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :type: list[AssembliesGetAssemblyDefinitionResponse200SubAssemblies]
        """

        self._sub_assemblies = sub_assemblies

    @property
    def parts(self):
        """Gets the parts of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501

        Parts in the assembly  # noqa: E501

        :return: The parts of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :rtype: list[AssembliesGetAssemblyDefinitionResponse200Parts]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this AssembliesGetAssemblyDefinitionResponse200.

        Parts in the assembly  # noqa: E501

        :param parts: The parts of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :type: list[AssembliesGetAssemblyDefinitionResponse200Parts]
        """

        self._parts = parts

    @property
    def part_studio_features(self):
        """Gets the part_studio_features of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501

        Features defined in Part Studios that are referenced by the             assembly, including sketches.  # noqa: E501

        :return: The part_studio_features of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :rtype: list[AssembliesGetAssemblyDefinitionResponse200PartStudioFeatures]
        """
        return self._part_studio_features

    @part_studio_features.setter
    def part_studio_features(self, part_studio_features):
        """Sets the part_studio_features of this AssembliesGetAssemblyDefinitionResponse200.

        Features defined in Part Studios that are referenced by the             assembly, including sketches.  # noqa: E501

        :param part_studio_features: The part_studio_features of this AssembliesGetAssemblyDefinitionResponse200.  # noqa: E501
        :type: list[AssembliesGetAssemblyDefinitionResponse200PartStudioFeatures]
        """

        self._part_studio_features = part_studio_features

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
        if not isinstance(other, AssembliesGetAssemblyDefinitionResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
