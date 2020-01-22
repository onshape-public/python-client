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
    from onshape_client.oas.models import bt_billing_plan_summary_info
except ImportError:
    bt_billing_plan_summary_info = sys.modules['onshape_client.oas.models.bt_billing_plan_summary_info']
try:
    from onshape_client.oas.models import btapi_application_summary_info
except ImportError:
    btapi_application_summary_info = sys.modules['onshape_client.oas.models.btapi_application_summary_info']
try:
    from onshape_client.oas.models import line_item
except ImportError:
    line_item = sys.modules['onshape_client.oas.models.line_item']


class BTPaymentHistoryInfo(ModelNormal):
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
            'onshape_plan': (bool,),  # noqa: E501
            'card_type': (str,),  # noqa: E501
            'discount': (int,),  # noqa: E501
            'account_last4': (str,),  # noqa: E501
            'invoice_id_for_refund': (str,),  # noqa: E501
            'line_items': ([line_item.LineItem],),  # noqa: E501
            'application': (btapi_application_summary_info.BTAPIApplicationSummaryInfo,),  # noqa: E501
            'amount_cents': (int,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'period_start': (datetime,),  # noqa: E501
            'period_end': (datetime,),  # noqa: E501
            'seats': (int,),  # noqa: E501
            'campaign_name': (str,),  # noqa: E501
            'refund': (bool,),  # noqa: E501
            'starting_balance_cents': (int,),  # noqa: E501
            'ending_balance_cents': (int,),  # noqa: E501
            'subtotal_cents': (int,),  # noqa: E501
            'prev_seats': (int,),  # noqa: E501
            'proration': (bool,),  # noqa: E501
            'coupon_amount_off_cents': (int,),  # noqa: E501
            'coupon_percent_off': (int,),  # noqa: E501
            'previous_plan': (bt_billing_plan_summary_info.BTBillingPlanSummaryInfo,),  # noqa: E501
            'zuora_invoice': (bool,),  # noqa: E501
            'actual_amount_cents': (int,),  # noqa: E501
            'posted_at': (datetime,),  # noqa: E501
            'campaign_code': (str,),  # noqa: E501
            'credits': (int,),  # noqa: E501
            'plan': (bt_billing_plan_summary_info.BTBillingPlanSummaryInfo,),  # noqa: E501
            'href': (str,),  # noqa: E501
            'view_ref': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'onshape_plan': 'onshapePlan',  # noqa: E501
        'card_type': 'cardType',  # noqa: E501
        'discount': 'discount',  # noqa: E501
        'account_last4': 'accountLast4',  # noqa: E501
        'invoice_id_for_refund': 'invoiceIdForRefund',  # noqa: E501
        'line_items': 'lineItems',  # noqa: E501
        'application': 'application',  # noqa: E501
        'amount_cents': 'amountCents',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'period_start': 'periodStart',  # noqa: E501
        'period_end': 'periodEnd',  # noqa: E501
        'seats': 'seats',  # noqa: E501
        'campaign_name': 'campaignName',  # noqa: E501
        'refund': 'refund',  # noqa: E501
        'starting_balance_cents': 'startingBalanceCents',  # noqa: E501
        'ending_balance_cents': 'endingBalanceCents',  # noqa: E501
        'subtotal_cents': 'subtotalCents',  # noqa: E501
        'prev_seats': 'prevSeats',  # noqa: E501
        'proration': 'proration',  # noqa: E501
        'coupon_amount_off_cents': 'couponAmountOffCents',  # noqa: E501
        'coupon_percent_off': 'couponPercentOff',  # noqa: E501
        'previous_plan': 'previousPlan',  # noqa: E501
        'zuora_invoice': 'zuoraInvoice',  # noqa: E501
        'actual_amount_cents': 'actualAmountCents',  # noqa: E501
        'posted_at': 'postedAt',  # noqa: E501
        'campaign_code': 'campaignCode',  # noqa: E501
        'credits': 'credits',  # noqa: E501
        'plan': 'plan',  # noqa: E501
        'href': 'href',  # noqa: E501
        'view_ref': 'viewRef',  # noqa: E501
        'name': 'name',  # noqa: E501
        'id': 'id',  # noqa: E501
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
        """bt_payment_history_info.BTPaymentHistoryInfo - a model defined in OpenAPI


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
            onshape_plan (bool): [optional]  # noqa: E501
            card_type (str): [optional]  # noqa: E501
            discount (int): [optional]  # noqa: E501
            account_last4 (str): [optional]  # noqa: E501
            invoice_id_for_refund (str): [optional]  # noqa: E501
            line_items ([line_item.LineItem]): [optional]  # noqa: E501
            application (btapi_application_summary_info.BTAPIApplicationSummaryInfo): [optional]  # noqa: E501
            amount_cents (int): [optional]  # noqa: E501
            created_at (datetime): [optional]  # noqa: E501
            period_start (datetime): [optional]  # noqa: E501
            period_end (datetime): [optional]  # noqa: E501
            seats (int): [optional]  # noqa: E501
            campaign_name (str): [optional]  # noqa: E501
            refund (bool): [optional]  # noqa: E501
            starting_balance_cents (int): [optional]  # noqa: E501
            ending_balance_cents (int): [optional]  # noqa: E501
            subtotal_cents (int): [optional]  # noqa: E501
            prev_seats (int): [optional]  # noqa: E501
            proration (bool): [optional]  # noqa: E501
            coupon_amount_off_cents (int): [optional]  # noqa: E501
            coupon_percent_off (int): [optional]  # noqa: E501
            previous_plan (bt_billing_plan_summary_info.BTBillingPlanSummaryInfo): [optional]  # noqa: E501
            zuora_invoice (bool): [optional]  # noqa: E501
            actual_amount_cents (int): [optional]  # noqa: E501
            posted_at (datetime): [optional]  # noqa: E501
            campaign_code (str): [optional]  # noqa: E501
            credits (int): [optional]  # noqa: E501
            plan (bt_billing_plan_summary_info.BTBillingPlanSummaryInfo): [optional]  # noqa: E501
            href (str): [optional]  # noqa: E501
            view_ref (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)
