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


class OAuthFlows(object):
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
        'implicit': 'OAuthFlow',
        'password': 'OAuthFlow',
        'client_credentials': 'OAuthFlow',
        'authorization_code': 'OAuthFlow',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'implicit': 'implicit',
        'password': 'password',
        'client_credentials': 'clientCredentials',
        'authorization_code': 'authorizationCode',
        'extensions': 'extensions'
    }

    def __init__(self, implicit=None, password=None, client_credentials=None, authorization_code=None, extensions=None, local_vars_configuration=None):  # noqa: E501
        """OAuthFlows - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._implicit = None
        self._password = None
        self._client_credentials = None
        self._authorization_code = None
        self._extensions = None
        self.discriminator = None

        if implicit is not None:
            self.implicit = implicit
        if password is not None:
            self.password = password
        if client_credentials is not None:
            self.client_credentials = client_credentials
        if authorization_code is not None:
            self.authorization_code = authorization_code
        if extensions is not None:
            self.extensions = extensions

    @property
    def implicit(self):
        """Gets the implicit of this OAuthFlows.  # noqa: E501


        :return: The implicit of this OAuthFlows.  # noqa: E501
        :rtype: OAuthFlow
        """
        return self._implicit

    @implicit.setter
    def implicit(self, implicit):
        """Sets the implicit of this OAuthFlows.


        :param implicit: The implicit of this OAuthFlows.  # noqa: E501
        :type: OAuthFlow
        """

        self._implicit = implicit

    @property
    def password(self):
        """Gets the password of this OAuthFlows.  # noqa: E501


        :return: The password of this OAuthFlows.  # noqa: E501
        :rtype: OAuthFlow
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OAuthFlows.


        :param password: The password of this OAuthFlows.  # noqa: E501
        :type: OAuthFlow
        """

        self._password = password

    @property
    def client_credentials(self):
        """Gets the client_credentials of this OAuthFlows.  # noqa: E501


        :return: The client_credentials of this OAuthFlows.  # noqa: E501
        :rtype: OAuthFlow
        """
        return self._client_credentials

    @client_credentials.setter
    def client_credentials(self, client_credentials):
        """Sets the client_credentials of this OAuthFlows.


        :param client_credentials: The client_credentials of this OAuthFlows.  # noqa: E501
        :type: OAuthFlow
        """

        self._client_credentials = client_credentials

    @property
    def authorization_code(self):
        """Gets the authorization_code of this OAuthFlows.  # noqa: E501


        :return: The authorization_code of this OAuthFlows.  # noqa: E501
        :rtype: OAuthFlow
        """
        return self._authorization_code

    @authorization_code.setter
    def authorization_code(self, authorization_code):
        """Sets the authorization_code of this OAuthFlows.


        :param authorization_code: The authorization_code of this OAuthFlows.  # noqa: E501
        :type: OAuthFlow
        """

        self._authorization_code = authorization_code

    @property
    def extensions(self):
        """Gets the extensions of this OAuthFlows.  # noqa: E501


        :return: The extensions of this OAuthFlows.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this OAuthFlows.


        :param extensions: The extensions of this OAuthFlows.  # noqa: E501
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
        if not isinstance(other, OAuthFlows):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuthFlows):
            return True

        return self.to_dict() != other.to_dict()
