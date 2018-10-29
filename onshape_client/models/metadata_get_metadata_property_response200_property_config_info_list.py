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


class MetadataGetMetadataPropertyResponse200PropertyConfigInfoList(object):
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
        'pattern': 'str',
        'schema_id': 'str',
        'required': 'bool',
        'max_value': 'float',
        'min_value': 'float',
        'multiline': 'bool',
        'min_length': 'float',
        'publish_state': 'float',
        'max_length': 'float',
        'default_value': 'str',
        'property_id': 'str',
        'object_type': 'float'
    }

    attribute_map = {
        'pattern': 'pattern',
        'schema_id': 'schemaId',
        'required': 'required',
        'max_value': 'maxValue',
        'min_value': 'minValue',
        'multiline': 'multiline',
        'min_length': 'minLength',
        'publish_state': 'publishState',
        'max_length': 'maxLength',
        'default_value': 'defaultValue',
        'property_id': 'propertyId',
        'object_type': 'objectType'
    }

    def __init__(self, pattern=None, schema_id=None, required=None, max_value=None, min_value=None, multiline=None, min_length=None, publish_state=None, max_length=None, default_value=None, property_id=None, object_type=None):  # noqa: E501
        """MetadataGetMetadataPropertyResponse200PropertyConfigInfoList - a model defined in Swagger"""  # noqa: E501

        self._pattern = None
        self._schema_id = None
        self._required = None
        self._max_value = None
        self._min_value = None
        self._multiline = None
        self._min_length = None
        self._publish_state = None
        self._max_length = None
        self._default_value = None
        self._property_id = None
        self._object_type = None
        self.discriminator = None

        if pattern is not None:
            self.pattern = pattern
        if schema_id is not None:
            self.schema_id = schema_id
        if required is not None:
            self.required = required
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if multiline is not None:
            self.multiline = multiline
        if min_length is not None:
            self.min_length = min_length
        if publish_state is not None:
            self.publish_state = publish_state
        if max_length is not None:
            self.max_length = max_length
        if default_value is not None:
            self.default_value = default_value
        if property_id is not None:
            self.property_id = property_id
        if object_type is not None:
            self.object_type = object_type

    @property
    def pattern(self):
        """Gets the pattern of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Regular expression pattern validation for             properties whose valueType == STRING (0)  # noqa: E501

        :return: The pattern of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Regular expression pattern validation for             properties whose valueType == STRING (0)  # noqa: E501

        :param pattern: The pattern of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

    @property
    def schema_id(self):
        """Gets the schema_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Schema ID associated with this property config             object  # noqa: E501

        :return: The schema_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: str
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Schema ID associated with this property config             object  # noqa: E501

        :param schema_id: The schema_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: str
        """

        self._schema_id = schema_id

    @property
    def required(self):
        """Gets the required of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        True if property is required to have a             non-empty value  # noqa: E501

        :return: The required of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        True if property is required to have a             non-empty value  # noqa: E501

        :param required: The required of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def max_value(self):
        """Gets the max_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Max value validation for properties whose             valueType == DOUBLE or INT  # noqa: E501

        :return: The max_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Max value validation for properties whose             valueType == DOUBLE or INT  # noqa: E501

        :param max_value: The max_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Min value validation for properties whose             valueType == DOUBLE or INT  # noqa: E501

        :return: The min_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Min value validation for properties whose             valueType == DOUBLE or INT  # noqa: E501

        :param min_value: The min_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def multiline(self):
        """Gets the multiline of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        True if string input should be multiline.             Only used if valueType == STRING  # noqa: E501

        :return: The multiline of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: bool
        """
        return self._multiline

    @multiline.setter
    def multiline(self, multiline):
        """Sets the multiline of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        True if string input should be multiline.             Only used if valueType == STRING  # noqa: E501

        :param multiline: The multiline of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: bool
        """

        self._multiline = multiline

    @property
    def min_length(self):
        """Gets the min_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Min length validation for properties whose             valueType == STRING  # noqa: E501

        :return: The min_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: float
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Min length validation for properties whose             valueType == STRING  # noqa: E501

        :param min_length: The min_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: float
        """

        self._min_length = min_length

    @property
    def publish_state(self):
        """Gets the publish_state of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Property publish state, which can be: 0:             PENDING, 1: ACTIVE, 2: INACTIVE  # noqa: E501

        :return: The publish_state of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: float
        """
        return self._publish_state

    @publish_state.setter
    def publish_state(self, publish_state):
        """Sets the publish_state of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Property publish state, which can be: 0:             PENDING, 1: ACTIVE, 2: INACTIVE  # noqa: E501

        :param publish_state: The publish_state of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: float
        """

        self._publish_state = publish_state

    @property
    def max_length(self):
        """Gets the max_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Max length validation for properties whose             valueType == STRING  # noqa: E501

        :return: The max_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: float
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Max length validation for properties whose             valueType == STRING  # noqa: E501

        :param max_length: The max_length of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: float
        """

        self._max_length = max_length

    @property
    def default_value(self):
        """Gets the default_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Default value, must be set if required ==             true  # noqa: E501

        :return: The default_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Default value, must be set if required ==             true  # noqa: E501

        :param default_value: The default_value of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def property_id(self):
        """Gets the property_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Property ID associated with this property             config object  # noqa: E501

        :return: The property_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: str
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Property ID associated with this property             config object  # noqa: E501

        :param property_id: The property_id of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: str
        """

        self._property_id = property_id

    @property
    def object_type(self):
        """Gets the object_type of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501

        Metadata object type, which can be: 0:GLOBAL,             1:DOCUMENT, 2:PART, 3:ASSEMBLY, 4:DRAWING, 5:PART_STUDIO, 6: BLOB_ELEMENT, 7:APP_ELEMENT, 8:VERSION,             9:WORKSPACE  # noqa: E501

        :return: The object_type of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :rtype: float
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.

        Metadata object type, which can be: 0:GLOBAL,             1:DOCUMENT, 2:PART, 3:ASSEMBLY, 4:DRAWING, 5:PART_STUDIO, 6: BLOB_ELEMENT, 7:APP_ELEMENT, 8:VERSION,             9:WORKSPACE  # noqa: E501

        :param object_type: The object_type of this MetadataGetMetadataPropertyResponse200PropertyConfigInfoList.  # noqa: E501
        :type: float
        """

        self._object_type = object_type

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
        if not isinstance(other, MetadataGetMetadataPropertyResponse200PropertyConfigInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
