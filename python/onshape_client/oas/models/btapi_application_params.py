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


class BTAPIApplicationParams(ModelNormal):
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
            'hidden_from_plus_menu_': (bool,),  # noqa: E501
            'base_href': (str,),  # noqa: E501
            'supports_collaboration': (bool,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'internal_grant_on_demand': (bool,),  # noqa: E501
            'company_id': (str,),  # noqa: E501
            'scope_names': ([str],),  # noqa: E501
            'developer_id': (str,),  # noqa: E501
            'redirect_ur_ls': ([str],),  # noqa: E501
            'ui_spec': (str,),  # noqa: E501
            'supports_merge': (bool,),  # noqa: E501
            'plans_supported': ([str],),  # noqa: E501
            'emebedded_onshape_auth_type': (int,),  # noqa: E501
            'emebedded_external_auth_type': (int,),  # noqa: E501
            'admin_team_id': (str,),  # noqa: E501
            'hidden_from_plus_menu': (bool,),  # noqa: E501
            'store_entry_is_public': (bool,),  # noqa: E501
            'developer_email': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'state': (int,),  # noqa: E501
            'primary_format': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'hidden_from_plus_menu_': 'hiddenFromPlusMenu_',  # noqa: E501
        'base_href': 'baseHref',  # noqa: E501
        'supports_collaboration': 'supportsCollaboration',  # noqa: E501
        'client_id': 'clientId',  # noqa: E501
        'internal_grant_on_demand': 'internalGrantOnDemand',  # noqa: E501
        'company_id': 'companyId',  # noqa: E501
        'scope_names': 'scopeNames',  # noqa: E501
        'developer_id': 'developerId',  # noqa: E501
        'redirect_ur_ls': 'redirectURLs',  # noqa: E501
        'ui_spec': 'uiSpec',  # noqa: E501
        'supports_merge': 'supportsMerge',  # noqa: E501
        'plans_supported': 'plansSupported',  # noqa: E501
        'emebedded_onshape_auth_type': 'emebeddedOnshapeAuthType',  # noqa: E501
        'emebedded_external_auth_type': 'emebeddedExternalAuthType',  # noqa: E501
        'admin_team_id': 'adminTeamId',  # noqa: E501
        'hidden_from_plus_menu': 'hiddenFromPlusMenu',  # noqa: E501
        'store_entry_is_public': 'storeEntryIsPublic',  # noqa: E501
        'developer_email': 'developerEmail',  # noqa: E501
        'description': 'description',  # noqa: E501
        'name': 'name',  # noqa: E501
        'state': 'state',  # noqa: E501
        'primary_format': 'primaryFormat',  # noqa: E501
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
        """btapi_application_params.BTAPIApplicationParams - a model defined in OpenAPI


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
            hidden_from_plus_menu_ (bool): [optional]  # noqa: E501
            base_href (str): [optional]  # noqa: E501
            supports_collaboration (bool): [optional]  # noqa: E501
            client_id (str): [optional]  # noqa: E501
            internal_grant_on_demand (bool): [optional]  # noqa: E501
            company_id (str): [optional]  # noqa: E501
            scope_names ([str]): [optional]  # noqa: E501
            developer_id (str): [optional]  # noqa: E501
            redirect_ur_ls ([str]): [optional]  # noqa: E501
            ui_spec (str): [optional]  # noqa: E501
            supports_merge (bool): [optional]  # noqa: E501
            plans_supported ([str]): [optional]  # noqa: E501
            emebedded_onshape_auth_type (int): [optional]  # noqa: E501
            emebedded_external_auth_type (int): [optional]  # noqa: E501
            admin_team_id (str): [optional]  # noqa: E501
            hidden_from_plus_menu (bool): [optional]  # noqa: E501
            store_entry_is_public (bool): [optional]  # noqa: E501
            developer_email (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            state (int): [optional]  # noqa: E501
            primary_format (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)
