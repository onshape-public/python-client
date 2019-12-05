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


class BTPTopLevelConstantDeclaration283AllOf(object):
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
        'declaration': 'BTPStatementConstantDeclaration273'
    }

    attribute_map = {
        'declaration': 'declaration'
    }

    def __init__(self, declaration=None, local_vars_configuration=None):  # noqa: E501
        """BTPTopLevelConstantDeclaration283AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._declaration = None
        self.discriminator = None

        if declaration is not None:
            self.declaration = declaration

    @property
    def declaration(self):
        """Gets the declaration of this BTPTopLevelConstantDeclaration283AllOf.  # noqa: E501


        :return: The declaration of this BTPTopLevelConstantDeclaration283AllOf.  # noqa: E501
        :rtype: BTPStatementConstantDeclaration273
        """
        return self._declaration

    @declaration.setter
    def declaration(self, declaration):
        """Sets the declaration of this BTPTopLevelConstantDeclaration283AllOf.


        :param declaration: The declaration of this BTPTopLevelConstantDeclaration283AllOf.  # noqa: E501
        :type: BTPStatementConstantDeclaration273
        """

        self._declaration = declaration

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
        if not isinstance(other, BTPTopLevelConstantDeclaration283AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTPTopLevelConstantDeclaration283AllOf):
            return True

        return self.to_dict() != other.to_dict()
