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


class BTMMateConnector66AllOf(object):
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
        'saved_feature_type': 'str',
        'is_hidden': 'bool',
        'implicit': 'bool'
    }

    attribute_map = {
        'saved_feature_type': 'savedFeatureType',
        'is_hidden': 'isHidden',
        'implicit': 'implicit'
    }

    def __init__(self, saved_feature_type=None, is_hidden=None, implicit=None, local_vars_configuration=None):  # noqa: E501
        """BTMMateConnector66AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._saved_feature_type = None
        self._is_hidden = None
        self._implicit = None
        self.discriminator = None

        if saved_feature_type is not None:
            self.saved_feature_type = saved_feature_type
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if implicit is not None:
            self.implicit = implicit

    @property
    def saved_feature_type(self):
        """Gets the saved_feature_type of this BTMMateConnector66AllOf.  # noqa: E501


        :return: The saved_feature_type of this BTMMateConnector66AllOf.  # noqa: E501
        :rtype: str
        """
        return self._saved_feature_type

    @saved_feature_type.setter
    def saved_feature_type(self, saved_feature_type):
        """Sets the saved_feature_type of this BTMMateConnector66AllOf.


        :param saved_feature_type: The saved_feature_type of this BTMMateConnector66AllOf.  # noqa: E501
        :type: str
        """

        self._saved_feature_type = saved_feature_type

    @property
    def is_hidden(self):
        """Gets the is_hidden of this BTMMateConnector66AllOf.  # noqa: E501


        :return: The is_hidden of this BTMMateConnector66AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this BTMMateConnector66AllOf.


        :param is_hidden: The is_hidden of this BTMMateConnector66AllOf.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def implicit(self):
        """Gets the implicit of this BTMMateConnector66AllOf.  # noqa: E501


        :return: The implicit of this BTMMateConnector66AllOf.  # noqa: E501
        :rtype: bool
        """
        return self._implicit

    @implicit.setter
    def implicit(self, implicit):
        """Sets the implicit of this BTMMateConnector66AllOf.


        :param implicit: The implicit of this BTMMateConnector66AllOf.  # noqa: E501
        :type: bool
        """

        self._implicit = implicit

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
        if not isinstance(other, BTMMateConnector66AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMMateConnector66AllOf):
            return True

        return self.to_dict() != other.to_dict()
