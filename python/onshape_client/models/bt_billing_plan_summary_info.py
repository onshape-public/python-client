# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTBillingPlanSummaryInfo(object):
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
        'hidden': 'bool',
        'onshape_plan': 'bool',
        'description': 'str',
        'company_plan': 'bool',
        'application_id': 'str',
        'deprecated': 'bool',
        'plan_type': 'int',
        'consumable_quantity': 'int',
        'amount_cents': 'int',
        'interval': 'str',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'hidden': 'hidden',
        'onshape_plan': 'onshapePlan',
        'description': 'description',
        'company_plan': 'companyPlan',
        'application_id': 'applicationId',
        'deprecated': 'deprecated',
        'plan_type': 'planType',
        'consumable_quantity': 'consumableQuantity',
        'amount_cents': 'amountCents',
        'interval': 'interval',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, hidden=None, onshape_plan=None, description=None, company_plan=None, application_id=None, deprecated=None, plan_type=None, consumable_quantity=None, amount_cents=None, interval=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTBillingPlanSummaryInfo - a model defined in OpenAPI"""  # noqa: E501

        self._hidden = None
        self._onshape_plan = None
        self._description = None
        self._company_plan = None
        self._application_id = None
        self._deprecated = None
        self._plan_type = None
        self._consumable_quantity = None
        self._amount_cents = None
        self._interval = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if hidden is not None:
            self.hidden = hidden
        if onshape_plan is not None:
            self.onshape_plan = onshape_plan
        if description is not None:
            self.description = description
        if company_plan is not None:
            self.company_plan = company_plan
        if application_id is not None:
            self.application_id = application_id
        if deprecated is not None:
            self.deprecated = deprecated
        if plan_type is not None:
            self.plan_type = plan_type
        if consumable_quantity is not None:
            self.consumable_quantity = consumable_quantity
        if amount_cents is not None:
            self.amount_cents = amount_cents
        if interval is not None:
            self.interval = interval
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def hidden(self):
        """Gets the hidden of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The hidden of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this BTBillingPlanSummaryInfo.


        :param hidden: The hidden of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def onshape_plan(self):
        """Gets the onshape_plan of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The onshape_plan of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._onshape_plan

    @onshape_plan.setter
    def onshape_plan(self, onshape_plan):
        """Sets the onshape_plan of this BTBillingPlanSummaryInfo.


        :param onshape_plan: The onshape_plan of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._onshape_plan = onshape_plan

    @property
    def description(self):
        """Gets the description of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The description of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BTBillingPlanSummaryInfo.


        :param description: The description of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def company_plan(self):
        """Gets the company_plan of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The company_plan of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._company_plan

    @company_plan.setter
    def company_plan(self, company_plan):
        """Sets the company_plan of this BTBillingPlanSummaryInfo.


        :param company_plan: The company_plan of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._company_plan = company_plan

    @property
    def application_id(self):
        """Gets the application_id of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The application_id of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this BTBillingPlanSummaryInfo.


        :param application_id: The application_id of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def deprecated(self):
        """Gets the deprecated of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The deprecated of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this BTBillingPlanSummaryInfo.


        :param deprecated: The deprecated of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def plan_type(self):
        """Gets the plan_type of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The plan_type of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._plan_type

    @plan_type.setter
    def plan_type(self, plan_type):
        """Sets the plan_type of this BTBillingPlanSummaryInfo.


        :param plan_type: The plan_type of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: int
        """

        self._plan_type = plan_type

    @property
    def consumable_quantity(self):
        """Gets the consumable_quantity of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The consumable_quantity of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._consumable_quantity

    @consumable_quantity.setter
    def consumable_quantity(self, consumable_quantity):
        """Sets the consumable_quantity of this BTBillingPlanSummaryInfo.


        :param consumable_quantity: The consumable_quantity of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: int
        """

        self._consumable_quantity = consumable_quantity

    @property
    def amount_cents(self):
        """Gets the amount_cents of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The amount_cents of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: int
        """
        return self._amount_cents

    @amount_cents.setter
    def amount_cents(self, amount_cents):
        """Sets the amount_cents of this BTBillingPlanSummaryInfo.


        :param amount_cents: The amount_cents of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: int
        """

        self._amount_cents = amount_cents

    @property
    def interval(self):
        """Gets the interval of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The interval of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this BTBillingPlanSummaryInfo.


        :param interval: The interval of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def name(self):
        """Gets the name of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The name of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTBillingPlanSummaryInfo.


        :param name: The name of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The id of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTBillingPlanSummaryInfo.


        :param id: The id of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The href of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTBillingPlanSummaryInfo.


        :param href: The href of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTBillingPlanSummaryInfo.  # noqa: E501


        :return: The view_ref of this BTBillingPlanSummaryInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTBillingPlanSummaryInfo.


        :param view_ref: The view_ref of this BTBillingPlanSummaryInfo.  # noqa: E501
        :type: str
        """

        self._view_ref = view_ref

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
        if not isinstance(other, BTBillingPlanSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
