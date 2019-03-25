# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTLoginParams(object):
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
        'password': 'str',
        'email': 'str',
        'remember_totp': 'bool',
        'web_client_capabilities': 'BTWebClientCapabilitiesParams',
        'renderer_performance_measurement': 'BTWebRendererPerformanceMeasurementParams',
        'device_id': 'str',
        'random_token': 'str',
        'totp': 'str',
        'enable_totp': 'bool'
    }

    attribute_map = {
        'password': 'password',
        'email': 'email',
        'remember_totp': 'rememberTotp',
        'web_client_capabilities': 'webClientCapabilities',
        'renderer_performance_measurement': 'rendererPerformanceMeasurement',
        'device_id': 'deviceId',
        'random_token': 'randomToken',
        'totp': 'totp',
        'enable_totp': 'enableTotp'
    }

    def __init__(self, password=None, email=None, remember_totp=None, web_client_capabilities=None, renderer_performance_measurement=None, device_id=None, random_token=None, totp=None, enable_totp=None):  # noqa: E501
        """BTLoginParams - a model defined in OpenAPI"""  # noqa: E501

        self._password = None
        self._email = None
        self._remember_totp = None
        self._web_client_capabilities = None
        self._renderer_performance_measurement = None
        self._device_id = None
        self._random_token = None
        self._totp = None
        self._enable_totp = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if remember_totp is not None:
            self.remember_totp = remember_totp
        if web_client_capabilities is not None:
            self.web_client_capabilities = web_client_capabilities
        if renderer_performance_measurement is not None:
            self.renderer_performance_measurement = renderer_performance_measurement
        if device_id is not None:
            self.device_id = device_id
        if random_token is not None:
            self.random_token = random_token
        if totp is not None:
            self.totp = totp
        if enable_totp is not None:
            self.enable_totp = enable_totp

    @property
    def password(self):
        """Gets the password of this BTLoginParams.  # noqa: E501


        :return: The password of this BTLoginParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this BTLoginParams.


        :param password: The password of this BTLoginParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this BTLoginParams.  # noqa: E501


        :return: The email of this BTLoginParams.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BTLoginParams.


        :param email: The email of this BTLoginParams.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def remember_totp(self):
        """Gets the remember_totp of this BTLoginParams.  # noqa: E501


        :return: The remember_totp of this BTLoginParams.  # noqa: E501
        :rtype: bool
        """
        return self._remember_totp

    @remember_totp.setter
    def remember_totp(self, remember_totp):
        """Sets the remember_totp of this BTLoginParams.


        :param remember_totp: The remember_totp of this BTLoginParams.  # noqa: E501
        :type: bool
        """

        self._remember_totp = remember_totp

    @property
    def web_client_capabilities(self):
        """Gets the web_client_capabilities of this BTLoginParams.  # noqa: E501


        :return: The web_client_capabilities of this BTLoginParams.  # noqa: E501
        :rtype: BTWebClientCapabilitiesParams
        """
        return self._web_client_capabilities

    @web_client_capabilities.setter
    def web_client_capabilities(self, web_client_capabilities):
        """Sets the web_client_capabilities of this BTLoginParams.


        :param web_client_capabilities: The web_client_capabilities of this BTLoginParams.  # noqa: E501
        :type: BTWebClientCapabilitiesParams
        """

        self._web_client_capabilities = web_client_capabilities

    @property
    def renderer_performance_measurement(self):
        """Gets the renderer_performance_measurement of this BTLoginParams.  # noqa: E501


        :return: The renderer_performance_measurement of this BTLoginParams.  # noqa: E501
        :rtype: BTWebRendererPerformanceMeasurementParams
        """
        return self._renderer_performance_measurement

    @renderer_performance_measurement.setter
    def renderer_performance_measurement(self, renderer_performance_measurement):
        """Sets the renderer_performance_measurement of this BTLoginParams.


        :param renderer_performance_measurement: The renderer_performance_measurement of this BTLoginParams.  # noqa: E501
        :type: BTWebRendererPerformanceMeasurementParams
        """

        self._renderer_performance_measurement = renderer_performance_measurement

    @property
    def device_id(self):
        """Gets the device_id of this BTLoginParams.  # noqa: E501


        :return: The device_id of this BTLoginParams.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this BTLoginParams.


        :param device_id: The device_id of this BTLoginParams.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def random_token(self):
        """Gets the random_token of this BTLoginParams.  # noqa: E501


        :return: The random_token of this BTLoginParams.  # noqa: E501
        :rtype: str
        """
        return self._random_token

    @random_token.setter
    def random_token(self, random_token):
        """Sets the random_token of this BTLoginParams.


        :param random_token: The random_token of this BTLoginParams.  # noqa: E501
        :type: str
        """

        self._random_token = random_token

    @property
    def totp(self):
        """Gets the totp of this BTLoginParams.  # noqa: E501


        :return: The totp of this BTLoginParams.  # noqa: E501
        :rtype: str
        """
        return self._totp

    @totp.setter
    def totp(self, totp):
        """Sets the totp of this BTLoginParams.


        :param totp: The totp of this BTLoginParams.  # noqa: E501
        :type: str
        """

        self._totp = totp

    @property
    def enable_totp(self):
        """Gets the enable_totp of this BTLoginParams.  # noqa: E501


        :return: The enable_totp of this BTLoginParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_totp

    @enable_totp.setter
    def enable_totp(self, enable_totp):
        """Sets the enable_totp of this BTLoginParams.


        :param enable_totp: The enable_totp of this BTLoginParams.  # noqa: E501
        :type: bool
        """

        self._enable_totp = enable_totp

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
        if not isinstance(other, BTLoginParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
