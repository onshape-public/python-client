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


class BTWebhookParams(object):
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
        'id': 'str',
        'options': 'BTWebhookOptions',
        'project_id': 'str',
        'folder_id': 'str',
        'url': 'str',
        'user_id': 'str',
        'version_id': 'str',
        'document_id': 'str',
        'company_id': 'str',
        'client_id': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'data': 'str',
        'filter': 'str',
        'events': 'list[str]',
        'part_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'options': 'options',
        'project_id': 'projectId',
        'folder_id': 'folderId',
        'url': 'url',
        'user_id': 'userId',
        'version_id': 'versionId',
        'document_id': 'documentId',
        'company_id': 'companyId',
        'client_id': 'clientId',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'data': 'data',
        'filter': 'filter',
        'events': 'events',
        'part_id': 'partId'
    }

    def __init__(self, id=None, options=None, project_id=None, folder_id=None, url=None, user_id=None, version_id=None, document_id=None, company_id=None, client_id=None, workspace_id=None, element_id=None, data=None, filter=None, events=None, part_id=None):  # noqa: E501
        """BTWebhookParams - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._options = None
        self._project_id = None
        self._folder_id = None
        self._url = None
        self._user_id = None
        self._version_id = None
        self._document_id = None
        self._company_id = None
        self._client_id = None
        self._workspace_id = None
        self._element_id = None
        self._data = None
        self._filter = None
        self._events = None
        self._part_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if options is not None:
            self.options = options
        if project_id is not None:
            self.project_id = project_id
        if folder_id is not None:
            self.folder_id = folder_id
        if url is not None:
            self.url = url
        if user_id is not None:
            self.user_id = user_id
        if version_id is not None:
            self.version_id = version_id
        if document_id is not None:
            self.document_id = document_id
        if company_id is not None:
            self.company_id = company_id
        if client_id is not None:
            self.client_id = client_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if data is not None:
            self.data = data
        if filter is not None:
            self.filter = filter
        if events is not None:
            self.events = events
        if part_id is not None:
            self.part_id = part_id

    @property
    def id(self):
        """Gets the id of this BTWebhookParams.  # noqa: E501


        :return: The id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BTWebhookParams.


        :param id: The id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def options(self):
        """Gets the options of this BTWebhookParams.  # noqa: E501


        :return: The options of this BTWebhookParams.  # noqa: E501
        :rtype: BTWebhookOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this BTWebhookParams.


        :param options: The options of this BTWebhookParams.  # noqa: E501
        :type: BTWebhookOptions
        """

        self._options = options

    @property
    def project_id(self):
        """Gets the project_id of this BTWebhookParams.  # noqa: E501


        :return: The project_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BTWebhookParams.


        :param project_id: The project_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def folder_id(self):
        """Gets the folder_id of this BTWebhookParams.  # noqa: E501


        :return: The folder_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this BTWebhookParams.


        :param folder_id: The folder_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def url(self):
        """Gets the url of this BTWebhookParams.  # noqa: E501


        :return: The url of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BTWebhookParams.


        :param url: The url of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user_id(self):
        """Gets the user_id of this BTWebhookParams.  # noqa: E501


        :return: The user_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BTWebhookParams.


        :param user_id: The user_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def version_id(self):
        """Gets the version_id of this BTWebhookParams.  # noqa: E501


        :return: The version_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this BTWebhookParams.


        :param version_id: The version_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

    @property
    def document_id(self):
        """Gets the document_id of this BTWebhookParams.  # noqa: E501


        :return: The document_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTWebhookParams.


        :param document_id: The document_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def company_id(self):
        """Gets the company_id of this BTWebhookParams.  # noqa: E501


        :return: The company_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this BTWebhookParams.


        :param company_id: The company_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def client_id(self):
        """Gets the client_id of this BTWebhookParams.  # noqa: E501


        :return: The client_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this BTWebhookParams.


        :param client_id: The client_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTWebhookParams.  # noqa: E501


        :return: The workspace_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTWebhookParams.


        :param workspace_id: The workspace_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTWebhookParams.  # noqa: E501


        :return: The element_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTWebhookParams.


        :param element_id: The element_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def data(self):
        """Gets the data of this BTWebhookParams.  # noqa: E501


        :return: The data of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this BTWebhookParams.


        :param data: The data of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def filter(self):
        """Gets the filter of this BTWebhookParams.  # noqa: E501


        :return: The filter of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this BTWebhookParams.


        :param filter: The filter of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def events(self):
        """Gets the events of this BTWebhookParams.  # noqa: E501


        :return: The events of this BTWebhookParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this BTWebhookParams.


        :param events: The events of this BTWebhookParams.  # noqa: E501
        :type: list[str]
        """

        self._events = events

    @property
    def part_id(self):
        """Gets the part_id of this BTWebhookParams.  # noqa: E501


        :return: The part_id of this BTWebhookParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTWebhookParams.


        :param part_id: The part_id of this BTWebhookParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

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
        if not isinstance(other, BTWebhookParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
