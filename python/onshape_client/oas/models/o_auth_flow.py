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


class OAuthFlow(object):
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
        'authorization_url': 'str',
        'token_url': 'str',
        'refresh_url': 'str',
        'scopes': 'dict(str, str)',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'authorization_url': 'authorizationUrl',
        'token_url': 'tokenUrl',
        'refresh_url': 'refreshUrl',
        'scopes': 'scopes',
        'extensions': 'extensions'
    }

    def __init__(self, authorization_url=None, token_url=None, refresh_url=None, scopes=None, extensions=None, local_vars_configuration=None):  # noqa: E501
        """OAuthFlow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authorization_url = None
        self._token_url = None
        self._refresh_url = None
        self._scopes = None
        self._extensions = None
        self.discriminator = None

        if authorization_url is not None:
            self.authorization_url = authorization_url
        if token_url is not None:
            self.token_url = token_url
        if refresh_url is not None:
            self.refresh_url = refresh_url
        if scopes is not None:
            self.scopes = scopes
        if extensions is not None:
            self.extensions = extensions

    @property
    def authorization_url(self):
        """Gets the authorization_url of this OAuthFlow.  # noqa: E501


        :return: The authorization_url of this OAuthFlow.  # noqa: E501
        :rtype: str
        """
        return self._authorization_url

    @authorization_url.setter
    def authorization_url(self, authorization_url):
        """Sets the authorization_url of this OAuthFlow.


        :param authorization_url: The authorization_url of this OAuthFlow.  # noqa: E501
        :type: str
        """

        self._authorization_url = authorization_url

    @property
    def token_url(self):
        """Gets the token_url of this OAuthFlow.  # noqa: E501


        :return: The token_url of this OAuthFlow.  # noqa: E501
        :rtype: str
        """
        return self._token_url

    @token_url.setter
    def token_url(self, token_url):
        """Sets the token_url of this OAuthFlow.


        :param token_url: The token_url of this OAuthFlow.  # noqa: E501
        :type: str
        """

        self._token_url = token_url

    @property
    def refresh_url(self):
        """Gets the refresh_url of this OAuthFlow.  # noqa: E501


        :return: The refresh_url of this OAuthFlow.  # noqa: E501
        :rtype: str
        """
        return self._refresh_url

    @refresh_url.setter
    def refresh_url(self, refresh_url):
        """Sets the refresh_url of this OAuthFlow.


        :param refresh_url: The refresh_url of this OAuthFlow.  # noqa: E501
        :type: str
        """

        self._refresh_url = refresh_url

    @property
    def scopes(self):
        """Gets the scopes of this OAuthFlow.  # noqa: E501


        :return: The scopes of this OAuthFlow.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this OAuthFlow.


        :param scopes: The scopes of this OAuthFlow.  # noqa: E501
        :type: dict(str, str)
        """

        self._scopes = scopes

    @property
    def extensions(self):
        """Gets the extensions of this OAuthFlow.  # noqa: E501


        :return: The extensions of this OAuthFlow.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this OAuthFlow.


        :param extensions: The extensions of this OAuthFlow.  # noqa: E501
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
        if not isinstance(other, OAuthFlow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OAuthFlow):
            return True

        return self.to_dict() != other.to_dict()
