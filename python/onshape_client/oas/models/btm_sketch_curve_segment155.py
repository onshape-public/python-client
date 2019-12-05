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


class BTMSketchCurveSegment155(object):
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
        'start_point_id': 'str',
        'end_point_id': 'str',
        'start_param': 'float',
        'end_param': 'float'
    }

    attribute_map = {
        'start_point_id': 'startPointId',
        'end_point_id': 'endPointId',
        'start_param': 'startParam',
        'end_param': 'endParam'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, start_point_id=None, end_point_id=None, start_param=None, end_param=None, local_vars_configuration=None):  # noqa: E501
        """BTMSketchCurveSegment155 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_point_id = None
        self._end_point_id = None
        self._start_param = None
        self._end_param = None
        self.discriminator = 'bt_type'

        if start_point_id is not None:
            self.start_point_id = start_point_id
        if end_point_id is not None:
            self.end_point_id = end_point_id
        if start_param is not None:
            self.start_param = start_param
        if end_param is not None:
            self.end_param = end_param

    @property
    def start_point_id(self):
        """Gets the start_point_id of this BTMSketchCurveSegment155.  # noqa: E501


        :return: The start_point_id of this BTMSketchCurveSegment155.  # noqa: E501
        :rtype: str
        """
        return self._start_point_id

    @start_point_id.setter
    def start_point_id(self, start_point_id):
        """Sets the start_point_id of this BTMSketchCurveSegment155.


        :param start_point_id: The start_point_id of this BTMSketchCurveSegment155.  # noqa: E501
        :type: str
        """

        self._start_point_id = start_point_id

    @property
    def end_point_id(self):
        """Gets the end_point_id of this BTMSketchCurveSegment155.  # noqa: E501


        :return: The end_point_id of this BTMSketchCurveSegment155.  # noqa: E501
        :rtype: str
        """
        return self._end_point_id

    @end_point_id.setter
    def end_point_id(self, end_point_id):
        """Sets the end_point_id of this BTMSketchCurveSegment155.


        :param end_point_id: The end_point_id of this BTMSketchCurveSegment155.  # noqa: E501
        :type: str
        """

        self._end_point_id = end_point_id

    @property
    def start_param(self):
        """Gets the start_param of this BTMSketchCurveSegment155.  # noqa: E501


        :return: The start_param of this BTMSketchCurveSegment155.  # noqa: E501
        :rtype: float
        """
        return self._start_param

    @start_param.setter
    def start_param(self, start_param):
        """Sets the start_param of this BTMSketchCurveSegment155.


        :param start_param: The start_param of this BTMSketchCurveSegment155.  # noqa: E501
        :type: float
        """

        self._start_param = start_param

    @property
    def end_param(self):
        """Gets the end_param of this BTMSketchCurveSegment155.  # noqa: E501


        :return: The end_param of this BTMSketchCurveSegment155.  # noqa: E501
        :rtype: float
        """
        return self._end_param

    @end_param.setter
    def end_param(self, end_param):
        """Sets the end_param of this BTMSketchCurveSegment155.


        :param end_param: The end_param of this BTMSketchCurveSegment155.  # noqa: E501
        :type: float
        """

        self._end_param = end_param

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, BTMSketchCurveSegment155):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BTMSketchCurveSegment155):
            return True

        return self.to_dict() != other.to_dict()
