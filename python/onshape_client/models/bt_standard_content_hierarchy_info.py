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


class BTStandardContentHierarchyInfo(object):
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
        'type': 'str',
        'existing_versions': 'list[VersionSpecs]',
        'category': 'str',
        'default_workspace': 'str',
        'standard': 'str',
        'document_type': 'int',
        'types': 'str',
        'production_version_id': 'str',
        'test_version_id': 'str',
        'name': 'str',
        'id': 'str',
        'href': 'str',
        'view_ref': 'str'
    }

    attribute_map = {
        'type': 'type',
        'existing_versions': 'existingVersions',
        'category': 'category',
        'default_workspace': 'defaultWorkspace',
        'standard': 'standard',
        'document_type': 'documentType',
        'types': 'types',
        'production_version_id': 'productionVersionId',
        'test_version_id': 'testVersionId',
        'name': 'name',
        'id': 'id',
        'href': 'href',
        'view_ref': 'viewRef'
    }

    def __init__(self, type=None, existing_versions=None, category=None, default_workspace=None, standard=None, document_type=None, types=None, production_version_id=None, test_version_id=None, name=None, id=None, href=None, view_ref=None):  # noqa: E501
        """BTStandardContentHierarchyInfo - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._existing_versions = None
        self._category = None
        self._default_workspace = None
        self._standard = None
        self._document_type = None
        self._types = None
        self._production_version_id = None
        self._test_version_id = None
        self._name = None
        self._id = None
        self._href = None
        self._view_ref = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if existing_versions is not None:
            self.existing_versions = existing_versions
        if category is not None:
            self.category = category
        if default_workspace is not None:
            self.default_workspace = default_workspace
        if standard is not None:
            self.standard = standard
        if document_type is not None:
            self.document_type = document_type
        if types is not None:
            self.types = types
        if production_version_id is not None:
            self.production_version_id = production_version_id
        if test_version_id is not None:
            self.test_version_id = test_version_id
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if href is not None:
            self.href = href
        if view_ref is not None:
            self.view_ref = view_ref

    @property
    def type(self):
        """Gets the type of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The type of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTStandardContentHierarchyInfo.


        :param type: The type of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def existing_versions(self):
        """Gets the existing_versions of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The existing_versions of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: list[VersionSpecs]
        """
        return self._existing_versions

    @existing_versions.setter
    def existing_versions(self, existing_versions):
        """Sets the existing_versions of this BTStandardContentHierarchyInfo.


        :param existing_versions: The existing_versions of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: list[VersionSpecs]
        """

        self._existing_versions = existing_versions

    @property
    def category(self):
        """Gets the category of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The category of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this BTStandardContentHierarchyInfo.


        :param category: The category of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def default_workspace(self):
        """Gets the default_workspace of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The default_workspace of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_workspace

    @default_workspace.setter
    def default_workspace(self, default_workspace):
        """Sets the default_workspace of this BTStandardContentHierarchyInfo.


        :param default_workspace: The default_workspace of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._default_workspace = default_workspace

    @property
    def standard(self):
        """Gets the standard of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The standard of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this BTStandardContentHierarchyInfo.


        :param standard: The standard of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._standard = standard

    @property
    def document_type(self):
        """Gets the document_type of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The document_type of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: int
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this BTStandardContentHierarchyInfo.


        :param document_type: The document_type of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: int
        """

        self._document_type = document_type

    @property
    def types(self):
        """Gets the types of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The types of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this BTStandardContentHierarchyInfo.


        :param types: The types of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._types = types

    @property
    def production_version_id(self):
        """Gets the production_version_id of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The production_version_id of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._production_version_id

    @production_version_id.setter
    def production_version_id(self, production_version_id):
        """Sets the production_version_id of this BTStandardContentHierarchyInfo.


        :param production_version_id: The production_version_id of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._production_version_id = production_version_id

    @property
    def test_version_id(self):
        """Gets the test_version_id of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The test_version_id of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._test_version_id

    @test_version_id.setter
    def test_version_id(self, test_version_id):
        """Sets the test_version_id of this BTStandardContentHierarchyInfo.


        :param test_version_id: The test_version_id of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._test_version_id = test_version_id

    @property
    def name(self):
        """Gets the name of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The name of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTStandardContentHierarchyInfo.


        :param name: The name of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The id of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTStandardContentHierarchyInfo.


        :param id: The id of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def href(self):
        """Gets the href of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The href of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this BTStandardContentHierarchyInfo.


        :param href: The href of this BTStandardContentHierarchyInfo.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def view_ref(self):
        """Gets the view_ref of this BTStandardContentHierarchyInfo.  # noqa: E501


        :return: The view_ref of this BTStandardContentHierarchyInfo.  # noqa: E501
        :rtype: str
        """
        return self._view_ref

    @view_ref.setter
    def view_ref(self, view_ref):
        """Sets the view_ref of this BTStandardContentHierarchyInfo.


        :param view_ref: The view_ref of this BTStandardContentHierarchyInfo.  # noqa: E501
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
        if not isinstance(other, BTStandardContentHierarchyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
