# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.93
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTNamedViewInfo(object):
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
        'view_matrix': 'list[float]',
        'perspective': 'bool',
        'angle': 'float',
        'camera_viewport': 'list[float]',
        'section_planes': 'list[BTSectionPlaneInfo]'
    }

    attribute_map = {
        'view_matrix': 'viewMatrix',
        'perspective': 'perspective',
        'angle': 'angle',
        'camera_viewport': 'cameraViewport',
        'section_planes': 'sectionPlanes'
    }

    def __init__(self, view_matrix=None, perspective=None, angle=None, camera_viewport=None, section_planes=None):  # noqa: E501
        """BTNamedViewInfo - a model defined in OpenAPI"""  # noqa: E501

        self._view_matrix = None
        self._perspective = None
        self._angle = None
        self._camera_viewport = None
        self._section_planes = None
        self.discriminator = None

        if view_matrix is not None:
            self.view_matrix = view_matrix
        if perspective is not None:
            self.perspective = perspective
        if angle is not None:
            self.angle = angle
        if camera_viewport is not None:
            self.camera_viewport = camera_viewport
        if section_planes is not None:
            self.section_planes = section_planes

    @property
    def view_matrix(self):
        """Gets the view_matrix of this BTNamedViewInfo.  # noqa: E501


        :return: The view_matrix of this BTNamedViewInfo.  # noqa: E501
        :rtype: list[float]
        """
        return self._view_matrix

    @view_matrix.setter
    def view_matrix(self, view_matrix):
        """Sets the view_matrix of this BTNamedViewInfo.


        :param view_matrix: The view_matrix of this BTNamedViewInfo.  # noqa: E501
        :type: list[float]
        """

        self._view_matrix = view_matrix

    @property
    def perspective(self):
        """Gets the perspective of this BTNamedViewInfo.  # noqa: E501


        :return: The perspective of this BTNamedViewInfo.  # noqa: E501
        :rtype: bool
        """
        return self._perspective

    @perspective.setter
    def perspective(self, perspective):
        """Sets the perspective of this BTNamedViewInfo.


        :param perspective: The perspective of this BTNamedViewInfo.  # noqa: E501
        :type: bool
        """

        self._perspective = perspective

    @property
    def angle(self):
        """Gets the angle of this BTNamedViewInfo.  # noqa: E501


        :return: The angle of this BTNamedViewInfo.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this BTNamedViewInfo.


        :param angle: The angle of this BTNamedViewInfo.  # noqa: E501
        :type: float
        """

        self._angle = angle

    @property
    def camera_viewport(self):
        """Gets the camera_viewport of this BTNamedViewInfo.  # noqa: E501


        :return: The camera_viewport of this BTNamedViewInfo.  # noqa: E501
        :rtype: list[float]
        """
        return self._camera_viewport

    @camera_viewport.setter
    def camera_viewport(self, camera_viewport):
        """Sets the camera_viewport of this BTNamedViewInfo.


        :param camera_viewport: The camera_viewport of this BTNamedViewInfo.  # noqa: E501
        :type: list[float]
        """

        self._camera_viewport = camera_viewport

    @property
    def section_planes(self):
        """Gets the section_planes of this BTNamedViewInfo.  # noqa: E501


        :return: The section_planes of this BTNamedViewInfo.  # noqa: E501
        :rtype: list[BTSectionPlaneInfo]
        """
        return self._section_planes

    @section_planes.setter
    def section_planes(self, section_planes):
        """Sets the section_planes of this BTNamedViewInfo.


        :param section_planes: The section_planes of this BTNamedViewInfo.  # noqa: E501
        :type: list[BTSectionPlaneInfo]
        """

        self._section_planes = section_planes

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
        if not isinstance(other, BTNamedViewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
