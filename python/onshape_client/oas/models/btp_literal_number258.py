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


class BTPLiteralNumber258(object):
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
        'short_descriptor': 'str',
        'integer': 'bool',
        'text': 'str',
        'value': 'float',
        'start_source_location': 'int',
        'end_source_location': 'int',
        'atomic': 'bool',
        'documentation_type': 'str',
        'space_before': 'BTPSpace10',
        'space_default': 'bool',
        'space_after': 'BTPSpace10',
        'node_id': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'short_descriptor': 'shortDescriptor',
        'integer': 'integer',
        'text': 'text',
        'value': 'value',
        'start_source_location': 'startSourceLocation',
        'end_source_location': 'endSourceLocation',
        'atomic': 'atomic',
        'documentation_type': 'documentationType',
        'space_before': 'spaceBefore',
        'space_default': 'spaceDefault',
        'space_after': 'spaceAfter',
        'node_id': 'nodeId',
        'bt_type': 'btType'
    }

    def __init__(self, short_descriptor=None, integer=None, text=None, value=None, start_source_location=None, end_source_location=None, atomic=None, documentation_type=None, space_before=None, space_default=None, space_after=None, node_id=None, bt_type=None, local_vars_configuration=None):  # noqa: E501
        """BTPLiteralNumber258 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._short_descriptor = None
        self._integer = None
        self._text = None
        self._value = None
        self._start_source_location = None
        self._end_source_location = None
        self._atomic = None
        self._documentation_type = None
        self._space_before = None
        self._space_default = None
        self._space_after = None
        self._node_id = None
        self._bt_type = None
        self.discriminator = None

        if short_descriptor is not None:
            self.short_descriptor = short_descriptor
        if integer is not None:
            self.integer = integer
        if text is not None:
            self.text = text
        if value is not None:
            self.value = value
        if start_source_location is not None:
            self.start_source_location = start_source_location
        if end_source_location is not None:
            self.end_source_location = end_source_location
        if atomic is not None:
            self.atomic = atomic
        if documentation_type is not None:
            self.documentation_type = documentation_type
        if space_before is not None:
            self.space_before = space_before
        if space_default is not None:
            self.space_default = space_default
        if space_after is not None:
            self.space_after = space_after
        if node_id is not None:
            self.node_id = node_id
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def short_descriptor(self):
        """Gets the short_descriptor of this BTPLiteralNumber258.  # noqa: E501


        :return: The short_descriptor of this BTPLiteralNumber258.  # noqa: E501
        :rtype: str
        """
        return self._short_descriptor

    @short_descriptor.setter
    def short_descriptor(self, short_descriptor):
        """Sets the short_descriptor of this BTPLiteralNumber258.


        :param short_descriptor: The short_descriptor of this BTPLiteralNumber258.  # noqa: E501
        :type: str
        """

        self._short_descriptor = short_descriptor

    @property
    def integer(self):
        """Gets the integer of this BTPLiteralNumber258.  # noqa: E501


        :return: The integer of this BTPLiteralNumber258.  # noqa: E501
        :rtype: bool
        """
        return self._integer

    @integer.setter
    def integer(self, integer):
        """Sets the integer of this BTPLiteralNumber258.


        :param integer: The integer of this BTPLiteralNumber258.  # noqa: E501
        :type: bool
        """

        self._integer = integer

    @property
    def text(self):
        """Gets the text of this BTPLiteralNumber258.  # noqa: E501


        :return: The text of this BTPLiteralNumber258.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this BTPLiteralNumber258.


        :param text: The text of this BTPLiteralNumber258.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def value(self):
        """Gets the value of this BTPLiteralNumber258.  # noqa: E501


        :return: The value of this BTPLiteralNumber258.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTPLiteralNumber258.


        :param value: The value of this BTPLiteralNumber258.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def start_source_location(self):
        """Gets the start_source_location of this BTPLiteralNumber258.  # noqa: E501


        :return: The start_source_location of this BTPLiteralNumber258.  # noqa: E501
        :rtype: int
        """
        return self._start_source_location

    @start_source_location.setter
    def start_source_location(self, start_source_location):
        """Sets the start_source_location of this BTPLiteralNumber258.


        :param start_source_location: The start_source_location of this BTPLiteralNumber258.  # noqa: E501
        :type: int
        """

        self._start_source_location = start_source_location

    @property
    def end_source_location(self):
        """Gets the end_source_location of this BTPLiteralNumber258.  # noqa: E501


        :return: The end_source_location of this BTPLiteralNumber258.  # noqa: E501
        :rtype: int
        """
        return self._end_source_location

    @end_source_location.setter
    def end_source_location(self, end_source_location):
        """Sets the end_source_location of this BTPLiteralNumber258.


        :param end_source_location: The end_source_location of this BTPLiteralNumber258.  # noqa: E501
        :type: int
        """

        self._end_source_location = end_source_location

    @property
    def atomic(self):
        """Gets the atomic of this BTPLiteralNumber258.  # noqa: E501


        :return: The atomic of this BTPLiteralNumber258.  # noqa: E501
        :rtype: bool
        """
        return self._atomic

    @atomic.setter
    def atomic(self, atomic):
        """Sets the atomic of this BTPLiteralNumber258.


        :param atomic: The atomic of this BTPLiteralNumber258.  # noqa: E501
        :type: bool
        """

        self._atomic = atomic

    @property
    def documentation_type(self):
        """Gets the documentation_type of this BTPLiteralNumber258.  # noqa: E501


        :return: The documentation_type of this BTPLiteralNumber258.  # noqa: E501
        :rtype: str
        """
        return self._documentation_type

    @documentation_type.setter
    def documentation_type(self, documentation_type):
        """Sets the documentation_type of this BTPLiteralNumber258.


        :param documentation_type: The documentation_type of this BTPLiteralNumber258.  # noqa: E501
        :type: str
        """
        allowed_values = ["FUNCTION", "PREDICATE", "CONSTANT", "ENUM", "USER_TYPE", "FEATURE_DEFINITION", "FILE_HEADER", "UNDOCUMENTABLE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and documentation_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `documentation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(documentation_type, allowed_values)
            )

        self._documentation_type = documentation_type

    @property
    def space_before(self):
        """Gets the space_before of this BTPLiteralNumber258.  # noqa: E501


        :return: The space_before of this BTPLiteralNumber258.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_before

    @space_before.setter
    def space_before(self, space_before):
        """Sets the space_before of this BTPLiteralNumber258.


        :param space_before: The space_before of this BTPLiteralNumber258.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_before = space_before

    @property
    def space_default(self):
        """Gets the space_default of this BTPLiteralNumber258.  # noqa: E501


        :return: The space_default of this BTPLiteralNumber258.  # noqa: E501
        :rtype: bool
        """
        return self._space_default

    @space_default.setter
    def space_default(self, space_default):
        """Sets the space_default of this BTPLiteralNumber258.


        :param space_default: The space_default of this BTPLiteralNumber258.  # noqa: E501
        :type: bool
        """

        self._space_default = space_default

    @property
    def space_after(self):
        """Gets the space_after of this BTPLiteralNumber258.  # noqa: E501


        :return: The space_after of this BTPLiteralNumber258.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after

    @space_after.setter
    def space_after(self, space_after):
        """Sets the space_after of this BTPLiteralNumber258.


        :param space_after: The space_after of this BTPLiteralNumber258.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after = space_after

    @property
    def node_id(self):
        """Gets the node_id of this BTPLiteralNumber258.  # noqa: E501


        :return: The node_id of this BTPLiteralNumber258.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTPLiteralNumber258.


        :param node_id: The node_id of this BTPLiteralNumber258.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def bt_type(self):
        """Gets the bt_type of this BTPLiteralNumber258.  # noqa: E501


        :return: The bt_type of this BTPLiteralNumber258.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTPLiteralNumber258.


        :param bt_type: The bt_type of this BTPLiteralNumber258.  # noqa: E501
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
        if not isinstance(other, BTPLiteralNumber258):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTPLiteralNumber258):
            return True

        return self.to_dict() != other.to_dict()
