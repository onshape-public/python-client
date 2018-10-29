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


class ReleaseManagementGetCompanyReleaseWorkflowResponse200(object):
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
        'using_auto_part_numbering_scheme': 'bool',
        'using_managed_workflow': 'bool',
        'obsoletion_workflow_id': 'str',
        'release_workflow_id': 'str'
    }

    attribute_map = {
        'using_auto_part_numbering_scheme': 'usingAutoPartNumberingScheme',
        'using_managed_workflow': 'usingManagedWorkflow',
        'obsoletion_workflow_id': 'obsoletionWorkflowId',
        'release_workflow_id': 'releaseWorkflowId'
    }

    def __init__(self, using_auto_part_numbering_scheme=None, using_managed_workflow=None, obsoletion_workflow_id=None, release_workflow_id=None):  # noqa: E501
        """ReleaseManagementGetCompanyReleaseWorkflowResponse200 - a model defined in Swagger"""  # noqa: E501

        self._using_auto_part_numbering_scheme = None
        self._using_managed_workflow = None
        self._obsoletion_workflow_id = None
        self._release_workflow_id = None
        self.discriminator = None

        if using_auto_part_numbering_scheme is not None:
            self.using_auto_part_numbering_scheme = using_auto_part_numbering_scheme
        if using_managed_workflow is not None:
            self.using_managed_workflow = using_managed_workflow
        if obsoletion_workflow_id is not None:
            self.obsoletion_workflow_id = obsoletion_workflow_id
        if release_workflow_id is not None:
            self.release_workflow_id = release_workflow_id

    @property
    def using_auto_part_numbering_scheme(self):
        """Gets the using_auto_part_numbering_scheme of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501

        Whether Sequential part number generation is being             used  # noqa: E501

        :return: The using_auto_part_numbering_scheme of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._using_auto_part_numbering_scheme

    @using_auto_part_numbering_scheme.setter
    def using_auto_part_numbering_scheme(self, using_auto_part_numbering_scheme):
        """Sets the using_auto_part_numbering_scheme of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.

        Whether Sequential part number generation is being             used  # noqa: E501

        :param using_auto_part_numbering_scheme: The using_auto_part_numbering_scheme of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :type: bool
        """

        self._using_auto_part_numbering_scheme = using_auto_part_numbering_scheme

    @property
    def using_managed_workflow(self):
        """Gets the using_managed_workflow of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501

        Whether managed workflow is in use for this document  # noqa: E501

        :return: The using_managed_workflow of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :rtype: bool
        """
        return self._using_managed_workflow

    @using_managed_workflow.setter
    def using_managed_workflow(self, using_managed_workflow):
        """Sets the using_managed_workflow of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.

        Whether managed workflow is in use for this document  # noqa: E501

        :param using_managed_workflow: The using_managed_workflow of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :type: bool
        """

        self._using_managed_workflow = using_managed_workflow

    @property
    def obsoletion_workflow_id(self):
        """Gets the obsoletion_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501

        The workflow ID for obsoleting existing revisions  # noqa: E501

        :return: The obsoletion_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :rtype: str
        """
        return self._obsoletion_workflow_id

    @obsoletion_workflow_id.setter
    def obsoletion_workflow_id(self, obsoletion_workflow_id):
        """Sets the obsoletion_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.

        The workflow ID for obsoleting existing revisions  # noqa: E501

        :param obsoletion_workflow_id: The obsoletion_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :type: str
        """

        self._obsoletion_workflow_id = obsoletion_workflow_id

    @property
    def release_workflow_id(self):
        """Gets the release_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501

        The workflow ID for creating new releases  # noqa: E501

        :return: The release_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :rtype: str
        """
        return self._release_workflow_id

    @release_workflow_id.setter
    def release_workflow_id(self, release_workflow_id):
        """Sets the release_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.

        The workflow ID for creating new releases  # noqa: E501

        :param release_workflow_id: The release_workflow_id of this ReleaseManagementGetCompanyReleaseWorkflowResponse200.  # noqa: E501
        :type: str
        """

        self._release_workflow_id = release_workflow_id

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
        if not isinstance(other, ReleaseManagementGetCompanyReleaseWorkflowResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
