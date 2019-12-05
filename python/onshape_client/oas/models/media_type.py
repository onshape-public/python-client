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


class MediaType(object):
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
        'schema': 'Schema',
        'examples': 'dict(str, Example)',
        'example': 'object',
        'encoding': 'dict(str, Encoding)',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'schema': 'schema',
        'examples': 'examples',
        'example': 'example',
        'encoding': 'encoding',
        'extensions': 'extensions'
    }

    def __init__(self, schema=None, examples=None, example=None, encoding=None, extensions=None, local_vars_configuration=None):  # noqa: E501
        """MediaType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._schema = None
        self._examples = None
        self._example = None
        self._encoding = None
        self._extensions = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        if examples is not None:
            self.examples = examples
        if example is not None:
            self.example = example
        if encoding is not None:
            self.encoding = encoding
        if extensions is not None:
            self.extensions = extensions

    @property
    def schema(self):
        """Gets the schema of this MediaType.  # noqa: E501


        :return: The schema of this MediaType.  # noqa: E501
        :rtype: Schema
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this MediaType.


        :param schema: The schema of this MediaType.  # noqa: E501
        :type: Schema
        """

        self._schema = schema

    @property
    def examples(self):
        """Gets the examples of this MediaType.  # noqa: E501


        :return: The examples of this MediaType.  # noqa: E501
        :rtype: dict(str, Example)
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """Sets the examples of this MediaType.


        :param examples: The examples of this MediaType.  # noqa: E501
        :type: dict(str, Example)
        """

        self._examples = examples

    @property
    def example(self):
        """Gets the example of this MediaType.  # noqa: E501


        :return: The example of this MediaType.  # noqa: E501
        :rtype: object
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this MediaType.


        :param example: The example of this MediaType.  # noqa: E501
        :type: object
        """

        self._example = example

    @property
    def encoding(self):
        """Gets the encoding of this MediaType.  # noqa: E501


        :return: The encoding of this MediaType.  # noqa: E501
        :rtype: dict(str, Encoding)
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this MediaType.


        :param encoding: The encoding of this MediaType.  # noqa: E501
        :type: dict(str, Encoding)
        """

        self._encoding = encoding

    @property
    def extensions(self):
        """Gets the extensions of this MediaType.  # noqa: E501


        :return: The extensions of this MediaType.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this MediaType.


        :param extensions: The extensions of this MediaType.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

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
        if not isinstance(other, MediaType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MediaType):
            return True

        return self.to_dict() != other.to_dict()
