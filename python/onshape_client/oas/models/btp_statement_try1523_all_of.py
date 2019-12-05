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


class BTPStatementTry1523AllOf(object):
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
        'standard_type': 'str',
        'name': 'BTPIdentifier8',
        'type_name': 'str',
        'body': 'BTPStatementBlock271',
        'silent': 'bool',
        'catch_variable': 'BTPIdentifier8',
        'space_before_silent': 'BTPSpace10',
        'catch_block': 'BTPStatementBlock271',
        'space_after_catch': 'BTPSpace10'
    }

    attribute_map = {
        'standard_type': 'standardType',
        'name': 'name',
        'type_name': 'typeName',
        'body': 'body',
        'silent': 'silent',
        'catch_variable': 'catchVariable',
        'space_before_silent': 'spaceBeforeSilent',
        'catch_block': 'catchBlock',
        'space_after_catch': 'spaceAfterCatch'
    }

    def __init__(self, standard_type=None, name=None, type_name=None, body=None, silent=None, catch_variable=None, space_before_silent=None, catch_block=None, space_after_catch=None, local_vars_configuration=None):  # noqa: E501
        """BTPStatementTry1523AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._standard_type = None
        self._name = None
        self._type_name = None
        self._body = None
        self._silent = None
        self._catch_variable = None
        self._space_before_silent = None
        self._catch_block = None
        self._space_after_catch = None
        self.discriminator = None

        if standard_type is not None:
            self.standard_type = standard_type
        if name is not None:
            self.name = name
        if type_name is not None:
            self.type_name = type_name
        if body is not None:
            self.body = body
        if silent is not None:
            self.silent = silent
        if catch_variable is not None:
            self.catch_variable = catch_variable
        if space_before_silent is not None:
            self.space_before_silent = space_before_silent
        if catch_block is not None:
            self.catch_block = catch_block
        if space_after_catch is not None:
            self.space_after_catch = space_after_catch

    @property
    def standard_type(self):
        """Gets the standard_type of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The standard_type of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: str
        """
        return self._standard_type

    @standard_type.setter
    def standard_type(self, standard_type):
        """Sets the standard_type of this BTPStatementTry1523AllOf.


        :param standard_type: The standard_type of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNDEFINED", "BOOLEAN", "NUMBER", "STRING", "ARRAY", "MAP", "BOX", "BUILTIN", "FUNCTION", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and standard_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `standard_type` ({0}), must be one of {1}"  # noqa: E501
                .format(standard_type, allowed_values)
            )

        self._standard_type = standard_type

    @property
    def name(self):
        """Gets the name of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The name of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: BTPIdentifier8
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPStatementTry1523AllOf.


        :param name: The name of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: BTPIdentifier8
        """

        self._name = name

    @property
    def type_name(self):
        """Gets the type_name of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The type_name of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this BTPStatementTry1523AllOf.


        :param type_name: The type_name of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def body(self):
        """Gets the body of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The body of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: BTPStatementBlock271
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BTPStatementTry1523AllOf.


        :param body: The body of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: BTPStatementBlock271
        """

        self._body = body

    @property
    def silent(self):
        """Gets the silent of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The silent of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._silent

    @silent.setter
    def silent(self, silent):
        """Sets the silent of this BTPStatementTry1523AllOf.


        :param silent: The silent of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: bool
        """

        self._silent = silent

    @property
    def catch_variable(self):
        """Gets the catch_variable of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The catch_variable of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: BTPIdentifier8
        """
        return self._catch_variable

    @catch_variable.setter
    def catch_variable(self, catch_variable):
        """Sets the catch_variable of this BTPStatementTry1523AllOf.


        :param catch_variable: The catch_variable of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: BTPIdentifier8
        """

        self._catch_variable = catch_variable

    @property
    def space_before_silent(self):
        """Gets the space_before_silent of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The space_before_silent of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_before_silent

    @space_before_silent.setter
    def space_before_silent(self, space_before_silent):
        """Sets the space_before_silent of this BTPStatementTry1523AllOf.


        :param space_before_silent: The space_before_silent of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_before_silent = space_before_silent

    @property
    def catch_block(self):
        """Gets the catch_block of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The catch_block of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: BTPStatementBlock271
        """
        return self._catch_block

    @catch_block.setter
    def catch_block(self, catch_block):
        """Sets the catch_block of this BTPStatementTry1523AllOf.


        :param catch_block: The catch_block of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: BTPStatementBlock271
        """

        self._catch_block = catch_block

    @property
    def space_after_catch(self):
        """Gets the space_after_catch of this BTPStatementTry1523AllOf.  # noqa: E501


        :return: The space_after_catch of this BTPStatementTry1523AllOf.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after_catch

    @space_after_catch.setter
    def space_after_catch(self, space_after_catch):
        """Sets the space_after_catch of this BTPStatementTry1523AllOf.


        :param space_after_catch: The space_after_catch of this BTPStatementTry1523AllOf.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after_catch = space_after_catch

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
        if not isinstance(other, BTPStatementTry1523AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTPStatementTry1523AllOf):
            return True

        return self.to_dict() != other.to_dict()
