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


class BTAssemblyFeatureDataInfo(object):
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
        'mate_type': 'str',
        'name': 'str',
        'mated_entities': 'list[BTAssemblyMatedEntity]'
    }

    attribute_map = {
        'mate_type': 'mateType',
        'name': 'name',
        'mated_entities': 'matedEntities'
    }

    def __init__(self, mate_type=None, name=None, mated_entities=None, local_vars_configuration=None):  # noqa: E501
        """BTAssemblyFeatureDataInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mate_type = None
        self._name = None
        self._mated_entities = None
        self.discriminator = None

        if mate_type is not None:
            self.mate_type = mate_type
        if name is not None:
            self.name = name
        if mated_entities is not None:
            self.mated_entities = mated_entities

    @property
    def mate_type(self):
        """Gets the mate_type of this BTAssemblyFeatureDataInfo.  # noqa: E501


        :return: The mate_type of this BTAssemblyFeatureDataInfo.  # noqa: E501
        :rtype: str
        """
        return self._mate_type

    @mate_type.setter
    def mate_type(self, mate_type):
        """Sets the mate_type of this BTAssemblyFeatureDataInfo.


        :param mate_type: The mate_type of this BTAssemblyFeatureDataInfo.  # noqa: E501
        :type: str
        """

        self._mate_type = mate_type

    @property
    def name(self):
        """Gets the name of this BTAssemblyFeatureDataInfo.  # noqa: E501


        :return: The name of this BTAssemblyFeatureDataInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTAssemblyFeatureDataInfo.


        :param name: The name of this BTAssemblyFeatureDataInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mated_entities(self):
        """Gets the mated_entities of this BTAssemblyFeatureDataInfo.  # noqa: E501


        :return: The mated_entities of this BTAssemblyFeatureDataInfo.  # noqa: E501
        :rtype: list[BTAssemblyMatedEntity]
        """
        return self._mated_entities

    @mated_entities.setter
    def mated_entities(self, mated_entities):
        """Sets the mated_entities of this BTAssemblyFeatureDataInfo.


        :param mated_entities: The mated_entities of this BTAssemblyFeatureDataInfo.  # noqa: E501
        :type: list[BTAssemblyMatedEntity]
        """

        self._mated_entities = mated_entities

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
        if not isinstance(other, BTAssemblyFeatureDataInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTAssemblyFeatureDataInfo):
            return True

        return self.to_dict() != other.to_dict()
