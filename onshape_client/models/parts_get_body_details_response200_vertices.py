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


class PartsGetBodyDetailsResponse200Vertices(object):
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
        'id': 'str',
        'point': 'list[float]'
    }

    attribute_map = {
        'id': 'id',
        'point': 'point'
    }

    def __init__(self, id=None, point=None):  # noqa: E501
        """PartsGetBodyDetailsResponse200Vertices - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._point = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if point is not None:
            self.point = point

    @property
    def id(self):
        """Gets the id of this PartsGetBodyDetailsResponse200Vertices.  # noqa: E501

        Vertex ID  # noqa: E501

        :return: The id of this PartsGetBodyDetailsResponse200Vertices.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartsGetBodyDetailsResponse200Vertices.

        Vertex ID  # noqa: E501

        :param id: The id of this PartsGetBodyDetailsResponse200Vertices.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def point(self):
        """Gets the point of this PartsGetBodyDetailsResponse200Vertices.  # noqa: E501

        Location of vertex  # noqa: E501

        :return: The point of this PartsGetBodyDetailsResponse200Vertices.  # noqa: E501
        :rtype: list[float]
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this PartsGetBodyDetailsResponse200Vertices.

        Location of vertex  # noqa: E501

        :param point: The point of this PartsGetBodyDetailsResponse200Vertices.  # noqa: E501
        :type: list[float]
        """

        self._point = point

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
        if not isinstance(other, PartsGetBodyDetailsResponse200Vertices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
