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
    from onshape_client.oas.models import bt_custom_property_definition_params
except ImportError:
    bt_custom_property_definition_params = sys.modules['onshape_client.oas.models.bt_custom_property_definition_params']
try:
    from onshape_client.oas.models import bt_material_params
except ImportError:
    bt_material_params = sys.modules['onshape_client.oas.models.bt_material_params']
try:
    from onshape_client.oas.models import bt_name_value_pair
except ImportError:
    bt_name_value_pair = sys.modules['onshape_client.oas.models.bt_name_value_pair']
try:
    from onshape_client.oas.models import bt_part_appearance_params
except ImportError:
    bt_part_appearance_params = sys.modules['onshape_client.oas.models.bt_part_appearance_params']


class BTWorkspacePartParams(ModelNormal):
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
            'configuration': (str,),  # noqa: E501
            'project': (str,),  # noqa: E501
            'element_id': (str,),  # noqa: E501
            'connection_id': (str,),  # noqa: E501
            'vendor': (str,),  # noqa: E501
            'product_line': (str,),  # noqa: E501
            'title1': (str,),  # noqa: E501
            'title2': (str,),  # noqa: E501
            'title3': (str,),  # noqa: E501
            'material': (bt_material_params.BTMaterialParams,),  # noqa: E501
            'appearance': (bt_part_appearance_params.BTPartAppearanceParams,),  # noqa: E501
            'custom_properties': ([bt_name_value_pair.BTNameValuePair],),  # noqa: E501
            'custom_property_definitions': ([bt_custom_property_definition_params.BTCustomPropertyDefinitionParams],),  # noqa: E501
            'apply_update_to_all_configurations': (bool,),  # noqa: E501
            'part_number': (str,),  # noqa: E501
            'part_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'revision': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'configuration': 'configuration',  # noqa: E501
        'project': 'project',  # noqa: E501
        'element_id': 'elementId',  # noqa: E501
        'connection_id': 'connectionId',  # noqa: E501
        'vendor': 'vendor',  # noqa: E501
        'product_line': 'productLine',  # noqa: E501
        'title1': 'title1',  # noqa: E501
        'title2': 'title2',  # noqa: E501
        'title3': 'title3',  # noqa: E501
        'material': 'material',  # noqa: E501
        'appearance': 'appearance',  # noqa: E501
        'custom_properties': 'customProperties',  # noqa: E501
        'custom_property_definitions': 'customPropertyDefinitions',  # noqa: E501
        'apply_update_to_all_configurations': 'applyUpdateToAllConfigurations',  # noqa: E501
        'part_number': 'partNumber',  # noqa: E501
        'part_id': 'partId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'revision': 'revision',  # noqa: E501
        'description': 'description',  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """bt_workspace_part_params.BTWorkspacePartParams - a model defined in OpenAPI


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
            configuration (str): [optional]  # noqa: E501
            project (str): [optional]  # noqa: E501
            element_id (str): [optional]  # noqa: E501
            connection_id (str): [optional]  # noqa: E501
            vendor (str): [optional]  # noqa: E501
            product_line (str): [optional]  # noqa: E501
            title1 (str): [optional]  # noqa: E501
            title2 (str): [optional]  # noqa: E501
            title3 (str): [optional]  # noqa: E501
            material (bt_material_params.BTMaterialParams): [optional]  # noqa: E501
            appearance (bt_part_appearance_params.BTPartAppearanceParams): [optional]  # noqa: E501
            custom_properties ([bt_name_value_pair.BTNameValuePair]): [optional]  # noqa: E501
            custom_property_definitions ([bt_custom_property_definition_params.BTCustomPropertyDefinitionParams]): [optional]  # noqa: E501
            apply_update_to_all_configurations (bool): [optional]  # noqa: E501
            part_number (str): [optional]  # noqa: E501
            part_id (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            revision (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)
