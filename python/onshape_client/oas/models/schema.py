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


class Schema(object):
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
        'title': 'str',
        'multiple_of': 'float',
        'maximum': 'float',
        'exclusive_maximum': 'bool',
        'minimum': 'float',
        'exclusive_minimum': 'bool',
        'max_length': 'int',
        'min_length': 'int',
        'pattern': 'str',
        'max_items': 'int',
        'min_items': 'int',
        'unique_items': 'bool',
        'max_properties': 'int',
        'min_properties': 'int',
        'required': 'list[str]',
        'type': 'str',
        '_not': 'Schema',
        'properties': 'dict(str, Schema)',
        'default': 'object',
        'description': 'str',
        'format': 'str',
        'getref': 'str',
        'nullable': 'bool',
        'read_only': 'bool',
        'write_only': 'bool',
        'external_docs': 'ExternalDocumentation',
        'deprecated': 'bool',
        'xml': 'XML',
        'extensions': 'dict(str, object)',
        'discriminator': 'Discriminator',
        'enum': 'list[object]'
    }

    attribute_map = {
        'title': 'title',
        'multiple_of': 'multipleOf',
        'maximum': 'maximum',
        'exclusive_maximum': 'exclusiveMaximum',
        'minimum': 'minimum',
        'exclusive_minimum': 'exclusiveMinimum',
        'max_length': 'maxLength',
        'min_length': 'minLength',
        'pattern': 'pattern',
        'max_items': 'maxItems',
        'min_items': 'minItems',
        'unique_items': 'uniqueItems',
        'max_properties': 'maxProperties',
        'min_properties': 'minProperties',
        'required': 'required',
        'type': 'type',
        '_not': 'not',
        'properties': 'properties',
        'default': 'default',
        'description': 'description',
        'format': 'format',
        'getref': 'get$ref',
        'nullable': 'nullable',
        'read_only': 'readOnly',
        'write_only': 'writeOnly',
        'external_docs': 'externalDocs',
        'deprecated': 'deprecated',
        'xml': 'xml',
        'extensions': 'extensions',
        'discriminator': 'discriminator',
        'enum': 'enum'
    }

    def __init__(self, title=None, multiple_of=None, maximum=None, exclusive_maximum=None, minimum=None, exclusive_minimum=None, max_length=None, min_length=None, pattern=None, max_items=None, min_items=None, unique_items=None, max_properties=None, min_properties=None, required=None, type=None, _not=None, properties=None, default=None, description=None, format=None, getref=None, nullable=None, read_only=None, write_only=None, external_docs=None, deprecated=None, xml=None, extensions=None, discriminator=None, enum=None, local_vars_configuration=None):  # noqa: E501
        """Schema - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._multiple_of = None
        self._maximum = None
        self._exclusive_maximum = None
        self._minimum = None
        self._exclusive_minimum = None
        self._max_length = None
        self._min_length = None
        self._pattern = None
        self._max_items = None
        self._min_items = None
        self._unique_items = None
        self._max_properties = None
        self._min_properties = None
        self._required = None
        self._type = None
        self.__not = None
        self._properties = None
        self._default = None
        self._description = None
        self._format = None
        self._getref = None
        self._nullable = None
        self._read_only = None
        self._write_only = None
        self._external_docs = None
        self._deprecated = None
        self._xml = None
        self._extensions = None
        self._discriminator = None
        self._enum = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if multiple_of is not None:
            self.multiple_of = multiple_of
        if maximum is not None:
            self.maximum = maximum
        if exclusive_maximum is not None:
            self.exclusive_maximum = exclusive_maximum
        if minimum is not None:
            self.minimum = minimum
        if exclusive_minimum is not None:
            self.exclusive_minimum = exclusive_minimum
        if max_length is not None:
            self.max_length = max_length
        if min_length is not None:
            self.min_length = min_length
        if pattern is not None:
            self.pattern = pattern
        if max_items is not None:
            self.max_items = max_items
        if min_items is not None:
            self.min_items = min_items
        if unique_items is not None:
            self.unique_items = unique_items
        if max_properties is not None:
            self.max_properties = max_properties
        if min_properties is not None:
            self.min_properties = min_properties
        if required is not None:
            self.required = required
        if type is not None:
            self.type = type
        if _not is not None:
            self._not = _not
        if properties is not None:
            self.properties = properties
        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if format is not None:
            self.format = format
        if getref is not None:
            self.getref = getref
        if nullable is not None:
            self.nullable = nullable
        if read_only is not None:
            self.read_only = read_only
        if write_only is not None:
            self.write_only = write_only
        if external_docs is not None:
            self.external_docs = external_docs
        if deprecated is not None:
            self.deprecated = deprecated
        if xml is not None:
            self.xml = xml
        if extensions is not None:
            self.extensions = extensions
        if discriminator is not None:
            self.discriminator = discriminator
        if enum is not None:
            self.enum = enum

    @property
    def title(self):
        """Gets the title of this Schema.  # noqa: E501


        :return: The title of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Schema.


        :param title: The title of this Schema.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def multiple_of(self):
        """Gets the multiple_of of this Schema.  # noqa: E501


        :return: The multiple_of of this Schema.  # noqa: E501
        :rtype: float
        """
        return self._multiple_of

    @multiple_of.setter
    def multiple_of(self, multiple_of):
        """Sets the multiple_of of this Schema.


        :param multiple_of: The multiple_of of this Schema.  # noqa: E501
        :type: float
        """

        self._multiple_of = multiple_of

    @property
    def maximum(self):
        """Gets the maximum of this Schema.  # noqa: E501


        :return: The maximum of this Schema.  # noqa: E501
        :rtype: float
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this Schema.


        :param maximum: The maximum of this Schema.  # noqa: E501
        :type: float
        """

        self._maximum = maximum

    @property
    def exclusive_maximum(self):
        """Gets the exclusive_maximum of this Schema.  # noqa: E501


        :return: The exclusive_maximum of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_maximum

    @exclusive_maximum.setter
    def exclusive_maximum(self, exclusive_maximum):
        """Sets the exclusive_maximum of this Schema.


        :param exclusive_maximum: The exclusive_maximum of this Schema.  # noqa: E501
        :type: bool
        """

        self._exclusive_maximum = exclusive_maximum

    @property
    def minimum(self):
        """Gets the minimum of this Schema.  # noqa: E501


        :return: The minimum of this Schema.  # noqa: E501
        :rtype: float
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this Schema.


        :param minimum: The minimum of this Schema.  # noqa: E501
        :type: float
        """

        self._minimum = minimum

    @property
    def exclusive_minimum(self):
        """Gets the exclusive_minimum of this Schema.  # noqa: E501


        :return: The exclusive_minimum of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._exclusive_minimum

    @exclusive_minimum.setter
    def exclusive_minimum(self, exclusive_minimum):
        """Sets the exclusive_minimum of this Schema.


        :param exclusive_minimum: The exclusive_minimum of this Schema.  # noqa: E501
        :type: bool
        """

        self._exclusive_minimum = exclusive_minimum

    @property
    def max_length(self):
        """Gets the max_length of this Schema.  # noqa: E501


        :return: The max_length of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this Schema.


        :param max_length: The max_length of this Schema.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this Schema.  # noqa: E501


        :return: The min_length of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this Schema.


        :param min_length: The min_length of this Schema.  # noqa: E501
        :type: int
        """

        self._min_length = min_length

    @property
    def pattern(self):
        """Gets the pattern of this Schema.  # noqa: E501


        :return: The pattern of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this Schema.


        :param pattern: The pattern of this Schema.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def max_items(self):
        """Gets the max_items of this Schema.  # noqa: E501


        :return: The max_items of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._max_items

    @max_items.setter
    def max_items(self, max_items):
        """Sets the max_items of this Schema.


        :param max_items: The max_items of this Schema.  # noqa: E501
        :type: int
        """

        self._max_items = max_items

    @property
    def min_items(self):
        """Gets the min_items of this Schema.  # noqa: E501


        :return: The min_items of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._min_items

    @min_items.setter
    def min_items(self, min_items):
        """Sets the min_items of this Schema.


        :param min_items: The min_items of this Schema.  # noqa: E501
        :type: int
        """

        self._min_items = min_items

    @property
    def unique_items(self):
        """Gets the unique_items of this Schema.  # noqa: E501


        :return: The unique_items of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._unique_items

    @unique_items.setter
    def unique_items(self, unique_items):
        """Sets the unique_items of this Schema.


        :param unique_items: The unique_items of this Schema.  # noqa: E501
        :type: bool
        """

        self._unique_items = unique_items

    @property
    def max_properties(self):
        """Gets the max_properties of this Schema.  # noqa: E501


        :return: The max_properties of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._max_properties

    @max_properties.setter
    def max_properties(self, max_properties):
        """Sets the max_properties of this Schema.


        :param max_properties: The max_properties of this Schema.  # noqa: E501
        :type: int
        """

        self._max_properties = max_properties

    @property
    def min_properties(self):
        """Gets the min_properties of this Schema.  # noqa: E501


        :return: The min_properties of this Schema.  # noqa: E501
        :rtype: int
        """
        return self._min_properties

    @min_properties.setter
    def min_properties(self, min_properties):
        """Sets the min_properties of this Schema.


        :param min_properties: The min_properties of this Schema.  # noqa: E501
        :type: int
        """

        self._min_properties = min_properties

    @property
    def required(self):
        """Gets the required of this Schema.  # noqa: E501


        :return: The required of this Schema.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Schema.


        :param required: The required of this Schema.  # noqa: E501
        :type: list[str]
        """

        self._required = required

    @property
    def type(self):
        """Gets the type of this Schema.  # noqa: E501


        :return: The type of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Schema.


        :param type: The type of this Schema.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def _not(self):
        """Gets the _not of this Schema.  # noqa: E501


        :return: The _not of this Schema.  # noqa: E501
        :rtype: Schema
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this Schema.


        :param _not: The _not of this Schema.  # noqa: E501
        :type: Schema
        """

        self.__not = _not

    @property
    def properties(self):
        """Gets the properties of this Schema.  # noqa: E501


        :return: The properties of this Schema.  # noqa: E501
        :rtype: dict(str, Schema)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Schema.


        :param properties: The properties of this Schema.  # noqa: E501
        :type: dict(str, Schema)
        """

        self._properties = properties

    @property
    def default(self):
        """Gets the default of this Schema.  # noqa: E501


        :return: The default of this Schema.  # noqa: E501
        :rtype: object
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Schema.


        :param default: The default of this Schema.  # noqa: E501
        :type: object
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this Schema.  # noqa: E501


        :return: The description of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Schema.


        :param description: The description of this Schema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format(self):
        """Gets the format of this Schema.  # noqa: E501


        :return: The format of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Schema.


        :param format: The format of this Schema.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def getref(self):
        """Gets the getref of this Schema.  # noqa: E501


        :return: The getref of this Schema.  # noqa: E501
        :rtype: str
        """
        return self._getref

    @getref.setter
    def getref(self, getref):
        """Sets the getref of this Schema.


        :param getref: The getref of this Schema.  # noqa: E501
        :type: str
        """

        self._getref = getref

    @property
    def nullable(self):
        """Gets the nullable of this Schema.  # noqa: E501


        :return: The nullable of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        """Sets the nullable of this Schema.


        :param nullable: The nullable of this Schema.  # noqa: E501
        :type: bool
        """

        self._nullable = nullable

    @property
    def read_only(self):
        """Gets the read_only of this Schema.  # noqa: E501


        :return: The read_only of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Schema.


        :param read_only: The read_only of this Schema.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def write_only(self):
        """Gets the write_only of this Schema.  # noqa: E501


        :return: The write_only of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._write_only

    @write_only.setter
    def write_only(self, write_only):
        """Sets the write_only of this Schema.


        :param write_only: The write_only of this Schema.  # noqa: E501
        :type: bool
        """

        self._write_only = write_only

    @property
    def external_docs(self):
        """Gets the external_docs of this Schema.  # noqa: E501


        :return: The external_docs of this Schema.  # noqa: E501
        :rtype: ExternalDocumentation
        """
        return self._external_docs

    @external_docs.setter
    def external_docs(self, external_docs):
        """Sets the external_docs of this Schema.


        :param external_docs: The external_docs of this Schema.  # noqa: E501
        :type: ExternalDocumentation
        """

        self._external_docs = external_docs

    @property
    def deprecated(self):
        """Gets the deprecated of this Schema.  # noqa: E501


        :return: The deprecated of this Schema.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this Schema.


        :param deprecated: The deprecated of this Schema.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def xml(self):
        """Gets the xml of this Schema.  # noqa: E501


        :return: The xml of this Schema.  # noqa: E501
        :rtype: XML
        """
        return self._xml

    @xml.setter
    def xml(self, xml):
        """Sets the xml of this Schema.


        :param xml: The xml of this Schema.  # noqa: E501
        :type: XML
        """

        self._xml = xml

    @property
    def extensions(self):
        """Gets the extensions of this Schema.  # noqa: E501


        :return: The extensions of this Schema.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this Schema.


        :param extensions: The extensions of this Schema.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

    @property
    def discriminator(self):
        """Gets the discriminator of this Schema.  # noqa: E501


        :return: The discriminator of this Schema.  # noqa: E501
        :rtype: Discriminator
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this Schema.


        :param discriminator: The discriminator of this Schema.  # noqa: E501
        :type: Discriminator
        """

        self._discriminator = discriminator

    @property
    def enum(self):
        """Gets the enum of this Schema.  # noqa: E501


        :return: The enum of this Schema.  # noqa: E501
        :rtype: list[object]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this Schema.


        :param enum: The enum of this Schema.  # noqa: E501
        :type: list[object]
        """

        self._enum = enum

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
        if not isinstance(other, Schema):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Schema):
            return True

        return self.to_dict() != other.to_dict()
