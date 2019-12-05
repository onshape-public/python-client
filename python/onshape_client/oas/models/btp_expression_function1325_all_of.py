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


class BTPExpressionFunction1325AllOf(object):
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
        'arguments': 'list[BTPArgumentDeclaration232]',
        'body': 'BTPStatementBlock271',
        'precondition': 'BTPStatement269',
        'space_after_arglist': 'BTPSpace10',
        'space_in_empty_list': 'BTPSpace10',
        'space_after_function': 'BTPSpace10',
        'return_type': 'BTPTypeName290'
    }

    attribute_map = {
        'arguments': 'arguments',
        'body': 'body',
        'precondition': 'precondition',
        'space_after_arglist': 'spaceAfterArglist',
        'space_in_empty_list': 'spaceInEmptyList',
        'space_after_function': 'spaceAfterFunction',
        'return_type': 'returnType'
    }

    def __init__(self, arguments=None, body=None, precondition=None, space_after_arglist=None, space_in_empty_list=None, space_after_function=None, return_type=None, local_vars_configuration=None):  # noqa: E501
        """BTPExpressionFunction1325AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._arguments = None
        self._body = None
        self._precondition = None
        self._space_after_arglist = None
        self._space_in_empty_list = None
        self._space_after_function = None
        self._return_type = None
        self.discriminator = None

        if arguments is not None:
            self.arguments = arguments
        if body is not None:
            self.body = body
        if precondition is not None:
            self.precondition = precondition
        if space_after_arglist is not None:
            self.space_after_arglist = space_after_arglist
        if space_in_empty_list is not None:
            self.space_in_empty_list = space_in_empty_list
        if space_after_function is not None:
            self.space_after_function = space_after_function
        if return_type is not None:
            self.return_type = return_type

    @property
    def arguments(self):
        """Gets the arguments of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The arguments of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: list[BTPArgumentDeclaration232]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this BTPExpressionFunction1325AllOf.


        :param arguments: The arguments of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: list[BTPArgumentDeclaration232]
        """

        self._arguments = arguments

    @property
    def body(self):
        """Gets the body of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The body of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: BTPStatementBlock271
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BTPExpressionFunction1325AllOf.


        :param body: The body of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: BTPStatementBlock271
        """

        self._body = body

    @property
    def precondition(self):
        """Gets the precondition of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The precondition of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: BTPStatement269
        """
        return self._precondition

    @precondition.setter
    def precondition(self, precondition):
        """Sets the precondition of this BTPExpressionFunction1325AllOf.


        :param precondition: The precondition of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: BTPStatement269
        """

        self._precondition = precondition

    @property
    def space_after_arglist(self):
        """Gets the space_after_arglist of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The space_after_arglist of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after_arglist

    @space_after_arglist.setter
    def space_after_arglist(self, space_after_arglist):
        """Sets the space_after_arglist of this BTPExpressionFunction1325AllOf.


        :param space_after_arglist: The space_after_arglist of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after_arglist = space_after_arglist

    @property
    def space_in_empty_list(self):
        """Gets the space_in_empty_list of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The space_in_empty_list of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_in_empty_list

    @space_in_empty_list.setter
    def space_in_empty_list(self, space_in_empty_list):
        """Sets the space_in_empty_list of this BTPExpressionFunction1325AllOf.


        :param space_in_empty_list: The space_in_empty_list of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_in_empty_list = space_in_empty_list

    @property
    def space_after_function(self):
        """Gets the space_after_function of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The space_after_function of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after_function

    @space_after_function.setter
    def space_after_function(self, space_after_function):
        """Sets the space_after_function of this BTPExpressionFunction1325AllOf.


        :param space_after_function: The space_after_function of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after_function = space_after_function

    @property
    def return_type(self):
        """Gets the return_type of this BTPExpressionFunction1325AllOf.  # noqa: E501


        :return: The return_type of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :rtype: BTPTypeName290
        """
        return self._return_type

    @return_type.setter
    def return_type(self, return_type):
        """Sets the return_type of this BTPExpressionFunction1325AllOf.


        :param return_type: The return_type of this BTPExpressionFunction1325AllOf.  # noqa: E501
        :type: BTPTypeName290
        """

        self._return_type = return_type

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
        if not isinstance(other, BTPExpressionFunction1325AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTPExpressionFunction1325AllOf):
            return True

        return self.to_dict() != other.to_dict()
