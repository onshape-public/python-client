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


class BTDocumentElementInfo(object):
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
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'length_units': 'str',
        'angle_units': 'str',
        'mass_units': 'str',
        'filename': 'str',
        'microversion_id': 'str',
        'thumbnail_info': 'BTThumbnailInfo',
        'element_type': 'str',
        'data_type': 'str',
        'foreign_data_id': 'str',
        'thumbnails': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'length_units': 'lengthUnits',
        'angle_units': 'angleUnits',
        'mass_units': 'massUnits',
        'filename': 'filename',
        'microversion_id': 'microversionId',
        'thumbnail_info': 'thumbnailInfo',
        'element_type': 'elementType',
        'data_type': 'dataType',
        'foreign_data_id': 'foreignDataId',
        'thumbnails': 'thumbnails'
    }

    def __init__(self, name=None, id=None, type=None, length_units=None, angle_units=None, mass_units=None, filename=None, microversion_id=None, thumbnail_info=None, element_type=None, data_type=None, foreign_data_id=None, thumbnails=None):  # noqa: E501
        """BTDocumentElementInfo - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._id = None
        self._type = None
        self._length_units = None
        self._angle_units = None
        self._mass_units = None
        self._filename = None
        self._microversion_id = None
        self._thumbnail_info = None
        self._element_type = None
        self._data_type = None
        self._foreign_data_id = None
        self._thumbnails = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if length_units is not None:
            self.length_units = length_units
        if angle_units is not None:
            self.angle_units = angle_units
        if mass_units is not None:
            self.mass_units = mass_units
        if filename is not None:
            self.filename = filename
        if microversion_id is not None:
            self.microversion_id = microversion_id
        if thumbnail_info is not None:
            self.thumbnail_info = thumbnail_info
        if element_type is not None:
            self.element_type = element_type
        if data_type is not None:
            self.data_type = data_type
        if foreign_data_id is not None:
            self.foreign_data_id = foreign_data_id
        if thumbnails is not None:
            self.thumbnails = thumbnails

    @property
    def name(self):
        """Gets the name of this BTDocumentElementInfo.  # noqa: E501


        :return: The name of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTDocumentElementInfo.


        :param name: The name of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTDocumentElementInfo.  # noqa: E501


        :return: The id of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTDocumentElementInfo.


        :param id: The id of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this BTDocumentElementInfo.  # noqa: E501


        :return: The type of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTDocumentElementInfo.


        :param type: The type of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def length_units(self):
        """Gets the length_units of this BTDocumentElementInfo.  # noqa: E501


        :return: The length_units of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._length_units

    @length_units.setter
    def length_units(self, length_units):
        """Sets the length_units of this BTDocumentElementInfo.


        :param length_units: The length_units of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._length_units = length_units

    @property
    def angle_units(self):
        """Gets the angle_units of this BTDocumentElementInfo.  # noqa: E501


        :return: The angle_units of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._angle_units

    @angle_units.setter
    def angle_units(self, angle_units):
        """Sets the angle_units of this BTDocumentElementInfo.


        :param angle_units: The angle_units of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._angle_units = angle_units

    @property
    def mass_units(self):
        """Gets the mass_units of this BTDocumentElementInfo.  # noqa: E501


        :return: The mass_units of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._mass_units

    @mass_units.setter
    def mass_units(self, mass_units):
        """Sets the mass_units of this BTDocumentElementInfo.


        :param mass_units: The mass_units of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._mass_units = mass_units

    @property
    def filename(self):
        """Gets the filename of this BTDocumentElementInfo.  # noqa: E501


        :return: The filename of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this BTDocumentElementInfo.


        :param filename: The filename of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def microversion_id(self):
        """Gets the microversion_id of this BTDocumentElementInfo.  # noqa: E501


        :return: The microversion_id of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._microversion_id

    @microversion_id.setter
    def microversion_id(self, microversion_id):
        """Sets the microversion_id of this BTDocumentElementInfo.


        :param microversion_id: The microversion_id of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._microversion_id = microversion_id

    @property
    def thumbnail_info(self):
        """Gets the thumbnail_info of this BTDocumentElementInfo.  # noqa: E501


        :return: The thumbnail_info of this BTDocumentElementInfo.  # noqa: E501
        :rtype: BTThumbnailInfo
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """Sets the thumbnail_info of this BTDocumentElementInfo.


        :param thumbnail_info: The thumbnail_info of this BTDocumentElementInfo.  # noqa: E501
        :type: BTThumbnailInfo
        """

        self._thumbnail_info = thumbnail_info

    @property
    def element_type(self):
        """Gets the element_type of this BTDocumentElementInfo.  # noqa: E501


        :return: The element_type of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """Sets the element_type of this BTDocumentElementInfo.


        :param element_type: The element_type of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["PARTSTUDIO", "ASSEMBLY", "DRAWING", "FEATURESTUDIO", "BLOB", "APPLICATION", "TABLE", "BILLOFMATERIALS", "UNKNOWN"]  # noqa: E501
        if element_type not in allowed_values:
            raise ValueError(
                "Invalid value for `element_type` ({0}), must be one of {1}"  # noqa: E501
                .format(element_type, allowed_values)
            )

        self._element_type = element_type

    @property
    def data_type(self):
        """Gets the data_type of this BTDocumentElementInfo.  # noqa: E501


        :return: The data_type of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this BTDocumentElementInfo.


        :param data_type: The data_type of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def foreign_data_id(self):
        """Gets the foreign_data_id of this BTDocumentElementInfo.  # noqa: E501


        :return: The foreign_data_id of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._foreign_data_id

    @foreign_data_id.setter
    def foreign_data_id(self, foreign_data_id):
        """Sets the foreign_data_id of this BTDocumentElementInfo.


        :param foreign_data_id: The foreign_data_id of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._foreign_data_id = foreign_data_id

    @property
    def thumbnails(self):
        """Gets the thumbnails of this BTDocumentElementInfo.  # noqa: E501


        :return: The thumbnails of this BTDocumentElementInfo.  # noqa: E501
        :rtype: str
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """Sets the thumbnails of this BTDocumentElementInfo.


        :param thumbnails: The thumbnails of this BTDocumentElementInfo.  # noqa: E501
        :type: str
        """

        self._thumbnails = thumbnails

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
        if not isinstance(other, BTDocumentElementInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
