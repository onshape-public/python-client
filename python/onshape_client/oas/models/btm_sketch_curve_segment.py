# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.106.24625.56a35b263da3
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401

from onshape_client.oas.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)
try:
    from onshape_client.oas.models import bt_curve_geometry
except ImportError:
    bt_curve_geometry = sys.modules['onshape_client.oas.models.bt_curve_geometry']
try:
    from onshape_client.oas.models import btm_parameter
except ImportError:
    btm_parameter = sys.modules['onshape_client.oas.models.btm_parameter']
try:
    from onshape_client.oas.models import btm_sketch_curve
except ImportError:
    btm_sketch_curve = sys.modules['onshape_client.oas.models.btm_sketch_curve']
try:
    from onshape_client.oas.models import btm_sketch_curve_segment
except ImportError:
    btm_sketch_curve_segment = sys.modules['onshape_client.oas.models.btm_sketch_curve_segment']
try:
    from onshape_client.oas.models import btm_sketch_curve_segment_all_of
except ImportError:
    btm_sketch_curve_segment_all_of = sys.modules['onshape_client.oas.models.btm_sketch_curve_segment_all_of']


class BTMSketchCurveSegment(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      openapi_types (dict): The key is attribute name
          and the value is attribute type.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    @staticmethod
    @property
    def openapi_types():
        return {
        'end_point_id': (str,),  # noqa: E501
        'start_param': (float,),  # noqa: E501
        'end_param': (float,),  # noqa: E501
        'start_point_id': (str,),  # noqa: E501
        'control_box_ids': ([str],),  # noqa: E501
        'is_construction': (bool,),  # noqa: E501
        'parameters': ([btm_parameter.BTMParameter],),  # noqa: E501
        'entity_id_and_replace_in_dependent_fields': (str,),  # noqa: E501
        'namespace': (str,),  # noqa: E501
        'node_id': (str,),  # noqa: E501
        'import_microversion': (str,),  # noqa: E501
        'entity_id': (str,),  # noqa: E501
        'bt_type': (str,),  # noqa: E501
        'geometry': (bt_curve_geometry.BTCurveGeometry,),  # noqa: E501
        'center_id': (str,),  # noqa: E501
        'internal_ids': ([str],),  # noqa: E501
    }

    validations = {
    }

    additional_properties_type = None

    @staticmethod
    def discriminator():
        return {
            'bt_type': {
                'BTMSketchCurveSegment': btm_sketch_curve_segment.BTMSketchCurveSegment,
            },
        }


    attribute_map = {
        'end_point_id': 'endPointId',  # noqa: E501
        'start_param': 'startParam',  # noqa: E501
        'end_param': 'endParam',  # noqa: E501
        'start_point_id': 'startPointId',  # noqa: E501
        'control_box_ids': 'controlBoxIds',  # noqa: E501
        'is_construction': 'isConstruction',  # noqa: E501
        'parameters': 'parameters',  # noqa: E501
        'entity_id_and_replace_in_dependent_fields': 'entityIdAndReplaceInDependentFields',  # noqa: E501
        'namespace': 'namespace',  # noqa: E501
        'node_id': 'nodeId',  # noqa: E501
        'import_microversion': 'importMicroversion',  # noqa: E501
        'entity_id': 'entityId',  # noqa: E501
        'bt_type': 'btType',  # noqa: E501
        'geometry': 'geometry',  # noqa: E501
        'center_id': 'centerId',  # noqa: E501
        'internal_ids': 'internalIds',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """btm_sketch_curve_segment.BTMSketchCurveSegment - a model defined in OpenAPI


        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            end_point_id (str): [optional]  # noqa: E501
            start_param (float): [optional]  # noqa: E501
            end_param (float): [optional]  # noqa: E501
            start_point_id (str): [optional]  # noqa: E501
            control_box_ids ([str]): [optional]  # noqa: E501
            is_construction (bool): [optional]  # noqa: E501
            parameters ([btm_parameter.BTMParameter]): [optional]  # noqa: E501
            entity_id_and_replace_in_dependent_fields (str): [optional]  # noqa: E501
            namespace (str): [optional]  # noqa: E501
            node_id (str): [optional]  # noqa: E501
            import_microversion (str): [optional]  # noqa: E501
            entity_id (str): [optional]  # noqa: E501
            bt_type (str): [optional]  # noqa: E501
            geometry (bt_curve_geometry.BTCurveGeometry): [optional]  # noqa: E501
            center_id (str): [optional]  # noqa: E501
            internal_ids ([str]): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_from_server': _from_server,
            '_configuration': _configuration,
        }
        model_args = {
        }
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)

    @staticmethod
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        return {
          'anyOf': [
          ],
          'allOf': [
              btm_sketch_curve.BTMSketchCurve,
              btm_sketch_curve_segment_all_of.BTMSketchCurveSegmentAllOf,
          ],
          'oneOf': [
          ],
        }

    @classmethod
    def get_discriminator_class(cls, from_server, data):
        """Returns the child class specified by the discriminator"""
        discriminator = cls.discriminator()
        discr_propertyname_py = list(discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if from_server:
            class_name = data[discr_propertyname_js]
        else:
            class_name = data[discr_propertyname_py]
        class_name_to_discr_class = discriminator[discr_propertyname_py]
        return class_name_to_discr_class.get(class_name)
