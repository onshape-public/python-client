# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.108
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
    from onshape_client.oas.models import bt_explosion_step_feature3008_all_of
except ImportError:
    bt_explosion_step_feature3008_all_of = sys.modules['onshape_client.oas.models.bt_explosion_step_feature3008_all_of']
try:
    from onshape_client.oas.models import bt_parameter_spec6
except ImportError:
    bt_parameter_spec6 = sys.modules['onshape_client.oas.models.bt_parameter_spec6']
try:
    from onshape_client.oas.models import btm_parameter1
except ImportError:
    btm_parameter1 = sys.modules['onshape_client.oas.models.btm_parameter1']


class BTParameterSpecBoolean170(ModelComposed):
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
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('ui_hints',): {
            'OPPOSITE_DIRECTION': "OPPOSITE_DIRECTION",
            'ALWAYS_HIDDEN': "ALWAYS_HIDDEN",
            'SHOW_CREATE_SELECTION': "SHOW_CREATE_SELECTION",
            'CONTROL_VISIBILITY': "CONTROL_VISIBILITY",
            'NO_PREVIEW_PROVIDED': "NO_PREVIEW_PROVIDED",
            'REMEMBER_PREVIOUS_VALUE': "REMEMBER_PREVIOUS_VALUE",
            'DISPLAY_SHORT': "DISPLAY_SHORT",
            'ALLOW_FEATURE_SELECTION': "ALLOW_FEATURE_SELECTION",
            'MATE_CONNECTOR_AXIS_TYPE': "MATE_CONNECTOR_AXIS_TYPE",
            'PRIMARY_AXIS': "PRIMARY_AXIS",
            'SHOW_EXPRESSION': "SHOW_EXPRESSION",
            'OPPOSITE_DIRECTION_CIRCULAR': "OPPOSITE_DIRECTION_CIRCULAR",
            'SHOW_LABEL': "SHOW_LABEL",
            'HORIZONTAL_ENUM': "HORIZONTAL_ENUM",
            'UNCONFIGURABLE': "UNCONFIGURABLE",
            'MATCH_LAST_ARRAY_ITEM': "MATCH_LAST_ARRAY_ITEM",
            'COLLAPSE_ARRAY_ITEMS': "COLLAPSE_ARRAY_ITEMS",
            'INITIAL_FOCUS_ON_EDIT': "INITIAL_FOCUS_ON_EDIT",
            'INITIAL_FOCUS': "INITIAL_FOCUS",
            'DISPLAY_CURRENT_VALUE_ONLY': "DISPLAY_CURRENT_VALUE_ONLY",
            'READ_ONLY': "READ_ONLY",
            'PREVENT_CREATING_NEW_MATE_CONNECTORS': "PREVENT_CREATING_NEW_MATE_CONNECTORS",
            'FIRST_IN_ROW': "FIRST_IN_ROW",
            'ALLOW_QUERY_ORDER': "ALLOW_QUERY_ORDER",
            'PREVENT_ARRAY_REORDER': "PREVENT_ARRAY_REORDER",
            'UNKNOWN': "UNKNOWN",
        },
    }

    validations = {
    }

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'bt_type': (str,),  # noqa: E501
            'localized_name': (str,),  # noqa: E501
            'localizable_name': (str,),  # noqa: E501
            'additional_localized_strings': (int,),  # noqa: E501
            'strings_to_localize': ([str],),  # noqa: E501
            'parameter_name': (str,),  # noqa: E501
            'parameter_id': (str,),  # noqa: E501
            'icon_uri': (str,),  # noqa: E501
            'visibility_condition': (bool, date, datetime, dict, float, int, list, str,),  # noqa: E501
            'ui_hint': (str,),  # noqa: E501
            'ui_hints': ([str],),  # noqa: E501
            'column_name': (str,),  # noqa: E501
            'default_value': (btm_parameter1.BTMParameter1,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'bt_type': 'btType',  # noqa: E501
        'localized_name': 'localizedName',  # noqa: E501
        'localizable_name': 'localizableName',  # noqa: E501
        'additional_localized_strings': 'additionalLocalizedStrings',  # noqa: E501
        'strings_to_localize': 'stringsToLocalize',  # noqa: E501
        'parameter_name': 'parameterName',  # noqa: E501
        'parameter_id': 'parameterId',  # noqa: E501
        'icon_uri': 'iconUri',  # noqa: E501
        'visibility_condition': 'visibilityCondition',  # noqa: E501
        'ui_hint': 'uiHint',  # noqa: E501
        'ui_hints': 'uiHints',  # noqa: E501
        'column_name': 'columnName',  # noqa: E501
        'default_value': 'defaultValue',  # noqa: E501
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
        """bt_parameter_spec_boolean170.BTParameterSpecBoolean170 - a model defined in OpenAPI


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
            bt_type (str): [optional]  # noqa: E501
            localized_name (str): [optional]  # noqa: E501
            localizable_name (str): [optional]  # noqa: E501
            additional_localized_strings (int): [optional]  # noqa: E501
            strings_to_localize ([str]): [optional]  # noqa: E501
            parameter_name (str): [optional]  # noqa: E501
            parameter_id (str): [optional]  # noqa: E501
            icon_uri (str): [optional]  # noqa: E501
            visibility_condition (bool, date, datetime, dict, float, int, list, str): [optional]  # noqa: E501
            ui_hint (str): [optional]  # noqa: E501
            ui_hints ([str]): [optional]  # noqa: E501
            column_name (str): [optional]  # noqa: E501
            default_value (btm_parameter1.BTMParameter1): [optional]  # noqa: E501
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
              bt_explosion_step_feature3008_all_of.BTExplosionStepFeature3008AllOf,
              bt_parameter_spec6.BTParameterSpec6,
          ],
          'oneOf': [
          ],
        }
