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

from onshape_client.models.users_get_user_settings_current_logged_in_user_response200_view_manipulation_mouse_key_mapping_pan2_d_mapping import UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan2DMapping  # noqa: F401,E501
from onshape_client.models.users_get_user_settings_current_logged_in_user_response200_view_manipulation_mouse_key_mapping_pan3_d_mapping import UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan3DMapping  # noqa: F401,E501
from onshape_client.models.users_get_user_settings_current_logged_in_user_response200_view_manipulation_mouse_key_mapping_rotate3_d_mapping import UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingRotate3DMapping  # noqa: F401,E501
from onshape_client.models.users_get_user_settings_current_logged_in_user_response200_view_manipulation_mouse_key_mapping_zoom2_d_mapping import UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom2DMapping  # noqa: F401,E501
from onshape_client.models.users_get_user_settings_current_logged_in_user_response200_view_manipulation_mouse_key_mapping_zoom3_d_mapping import UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom3DMapping  # noqa: F401,E501


class UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping(object):
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
        'zoom2_d_mapping': 'list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom2DMapping]',
        'zoom3_d_mapping': 'list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom3DMapping]',
        'rotate3_d_mapping': 'list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingRotate3DMapping]',
        'pan3_d_mapping': 'list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan3DMapping]',
        'pan2_d_mapping': 'list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan2DMapping]'
    }

    attribute_map = {
        'zoom2_d_mapping': 'zoom2DMapping',
        'zoom3_d_mapping': 'zoom3DMapping',
        'rotate3_d_mapping': 'rotate3DMapping',
        'pan3_d_mapping': 'pan3DMapping',
        'pan2_d_mapping': 'pan2DMapping'
    }

    def __init__(self, zoom2_d_mapping=None, zoom3_d_mapping=None, rotate3_d_mapping=None, pan3_d_mapping=None, pan2_d_mapping=None):  # noqa: E501
        """UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping - a model defined in Swagger"""  # noqa: E501

        self._zoom2_d_mapping = None
        self._zoom3_d_mapping = None
        self._rotate3_d_mapping = None
        self._pan3_d_mapping = None
        self._pan2_d_mapping = None
        self.discriminator = None

        if zoom2_d_mapping is not None:
            self.zoom2_d_mapping = zoom2_d_mapping
        if zoom3_d_mapping is not None:
            self.zoom3_d_mapping = zoom3_d_mapping
        if rotate3_d_mapping is not None:
            self.rotate3_d_mapping = rotate3_d_mapping
        if pan3_d_mapping is not None:
            self.pan3_d_mapping = pan3_d_mapping
        if pan2_d_mapping is not None:
            self.pan2_d_mapping = pan2_d_mapping

    @property
    def zoom2_d_mapping(self):
        """Gets the zoom2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501

        Array of sets of button and key             presses that zoom in 2D  # noqa: E501

        :return: The zoom2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :rtype: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom2DMapping]
        """
        return self._zoom2_d_mapping

    @zoom2_d_mapping.setter
    def zoom2_d_mapping(self, zoom2_d_mapping):
        """Sets the zoom2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.

        Array of sets of button and key             presses that zoom in 2D  # noqa: E501

        :param zoom2_d_mapping: The zoom2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :type: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom2DMapping]
        """

        self._zoom2_d_mapping = zoom2_d_mapping

    @property
    def zoom3_d_mapping(self):
        """Gets the zoom3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501

        Array of sets of button and key             presses that zoom in 3D  # noqa: E501

        :return: The zoom3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :rtype: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom3DMapping]
        """
        return self._zoom3_d_mapping

    @zoom3_d_mapping.setter
    def zoom3_d_mapping(self, zoom3_d_mapping):
        """Sets the zoom3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.

        Array of sets of button and key             presses that zoom in 3D  # noqa: E501

        :param zoom3_d_mapping: The zoom3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :type: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingZoom3DMapping]
        """

        self._zoom3_d_mapping = zoom3_d_mapping

    @property
    def rotate3_d_mapping(self):
        """Gets the rotate3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501

        Array of sets of button and key             presses that rotate in 3D  # noqa: E501

        :return: The rotate3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :rtype: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingRotate3DMapping]
        """
        return self._rotate3_d_mapping

    @rotate3_d_mapping.setter
    def rotate3_d_mapping(self, rotate3_d_mapping):
        """Sets the rotate3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.

        Array of sets of button and key             presses that rotate in 3D  # noqa: E501

        :param rotate3_d_mapping: The rotate3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :type: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingRotate3DMapping]
        """

        self._rotate3_d_mapping = rotate3_d_mapping

    @property
    def pan3_d_mapping(self):
        """Gets the pan3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501

        Array of sets of button and key             presses that pan in 3D  # noqa: E501

        :return: The pan3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :rtype: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan3DMapping]
        """
        return self._pan3_d_mapping

    @pan3_d_mapping.setter
    def pan3_d_mapping(self, pan3_d_mapping):
        """Sets the pan3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.

        Array of sets of button and key             presses that pan in 3D  # noqa: E501

        :param pan3_d_mapping: The pan3_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :type: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan3DMapping]
        """

        self._pan3_d_mapping = pan3_d_mapping

    @property
    def pan2_d_mapping(self):
        """Gets the pan2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501

        Array of sets of button and key             presses that pan in 2D  # noqa: E501

        :return: The pan2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :rtype: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan2DMapping]
        """
        return self._pan2_d_mapping

    @pan2_d_mapping.setter
    def pan2_d_mapping(self, pan2_d_mapping):
        """Sets the pan2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.

        Array of sets of button and key             presses that pan in 2D  # noqa: E501

        :param pan2_d_mapping: The pan2_d_mapping of this UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping.  # noqa: E501
        :type: list[UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMappingPan2DMapping]
        """

        self._pan2_d_mapping = pan2_d_mapping

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
        if not isinstance(other, UsersGetUserSettingsCurrentLoggedInUserResponse200ViewManipulationMouseKeyMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
