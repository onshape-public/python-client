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


class ThumbnailsGetDocumentThumbnailResponse200Sizes(object):
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
        'view_orientation': 'str',
        'href': 'str',
        'media_type': 'str',
        'size': 'str'
    }

    attribute_map = {
        'view_orientation': 'viewOrientation',
        'href': 'href',
        'media_type': 'mediaType',
        'size': 'size'
    }

    def __init__(self, view_orientation=None, href=None, media_type=None, size=None):  # noqa: E501
        """ThumbnailsGetDocumentThumbnailResponse200Sizes - a model defined in Swagger"""  # noqa: E501

        self._view_orientation = None
        self._href = None
        self._media_type = None
        self._size = None
        self.discriminator = None

        if view_orientation is not None:
            self.view_orientation = view_orientation
        if href is not None:
            self.href = href
        if media_type is not None:
            self.media_type = media_type
        if size is not None:
            self.size = size

    @property
    def view_orientation(self):
        """Gets the view_orientation of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501

        View orientation at which thumbnail is rendered, example trimetric  # noqa: E501

        :return: The view_orientation of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :rtype: str
        """
        return self._view_orientation

    @view_orientation.setter
    def view_orientation(self, view_orientation):
        """Sets the view_orientation of this ThumbnailsGetDocumentThumbnailResponse200Sizes.

        View orientation at which thumbnail is rendered, example trimetric  # noqa: E501

        :param view_orientation: The view_orientation of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :type: str
        """

        self._view_orientation = view_orientation

    @property
    def href(self):
        """Gets the href of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501

        URI for thumbnail  # noqa: E501

        :return: The href of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ThumbnailsGetDocumentThumbnailResponse200Sizes.

        URI for thumbnail  # noqa: E501

        :param href: The href of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def media_type(self):
        """Gets the media_type of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501

        Media type for thumbnail, typically image/png  # noqa: E501

        :return: The media_type of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ThumbnailsGetDocumentThumbnailResponse200Sizes.

        Media type for thumbnail, typically image/png  # noqa: E501

        :param media_type: The media_type of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def size(self):
        """Gets the size of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501

        Size o this thumbnail, typically one of 70x40, 300x170, 300x300, or 600x340  # noqa: E501

        :return: The size of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ThumbnailsGetDocumentThumbnailResponse200Sizes.

        Size o this thumbnail, typically one of 70x40, 300x170, 300x300, or 600x340  # noqa: E501

        :param size: The size of this ThumbnailsGetDocumentThumbnailResponse200Sizes.  # noqa: E501
        :type: str
        """

        self._size = size

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
        if not isinstance(other, ThumbnailsGetDocumentThumbnailResponse200Sizes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
