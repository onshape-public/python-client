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


class BTMSketchCurve4AllOf(object):
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
        'geometry': 'BTCurveGeometry114',
        'center_id': 'str',
        'internal_ids': 'list[str]'
    }

    attribute_map = {
        'geometry': 'geometry',
        'center_id': 'centerId',
        'internal_ids': 'internalIds'
    }

    def __init__(self, geometry=None, center_id=None, internal_ids=None, local_vars_configuration=None):  # noqa: E501
        """BTMSketchCurve4AllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geometry = None
        self._center_id = None
        self._internal_ids = None
        self.discriminator = None

        if geometry is not None:
            self.geometry = geometry
        if center_id is not None:
            self.center_id = center_id
        if internal_ids is not None:
            self.internal_ids = internal_ids

    @property
    def geometry(self):
        """Gets the geometry of this BTMSketchCurve4AllOf.  # noqa: E501


        :return: The geometry of this BTMSketchCurve4AllOf.  # noqa: E501
        :rtype: BTCurveGeometry114
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this BTMSketchCurve4AllOf.


        :param geometry: The geometry of this BTMSketchCurve4AllOf.  # noqa: E501
        :type: BTCurveGeometry114
        """

        self._geometry = geometry

    @property
    def center_id(self):
        """Gets the center_id of this BTMSketchCurve4AllOf.  # noqa: E501


        :return: The center_id of this BTMSketchCurve4AllOf.  # noqa: E501
        :rtype: str
        """
        return self._center_id

    @center_id.setter
    def center_id(self, center_id):
        """Sets the center_id of this BTMSketchCurve4AllOf.


        :param center_id: The center_id of this BTMSketchCurve4AllOf.  # noqa: E501
        :type: str
        """

        self._center_id = center_id

    @property
    def internal_ids(self):
        """Gets the internal_ids of this BTMSketchCurve4AllOf.  # noqa: E501


        :return: The internal_ids of this BTMSketchCurve4AllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._internal_ids

    @internal_ids.setter
    def internal_ids(self, internal_ids):
        """Sets the internal_ids of this BTMSketchCurve4AllOf.


        :param internal_ids: The internal_ids of this BTMSketchCurve4AllOf.  # noqa: E501
        :type: list[str]
        """

        self._internal_ids = internal_ids

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
        if not isinstance(other, BTMSketchCurve4AllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMSketchCurve4AllOf):
            return True

        return self.to_dict() != other.to_dict()
