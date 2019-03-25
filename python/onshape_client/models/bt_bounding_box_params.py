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


class BTBoundingBoxParams(object):
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
        'document_id': 'str',
        'workspace_id': 'str',
        'element_id': 'str',
        'sketch_id': 'str',
        'element_microversion_id': 'str',
        'include_hidden': 'bool',
        'part_query': 'str',
        'part_id': 'str',
        'include_wire_bodies': 'bool',
        'display_state_id': 'str'
    }

    attribute_map = {
        'document_id': 'documentId',
        'workspace_id': 'workspaceId',
        'element_id': 'elementId',
        'sketch_id': 'sketchId',
        'element_microversion_id': 'elementMicroversionId',
        'include_hidden': 'includeHidden',
        'part_query': 'partQuery',
        'part_id': 'partId',
        'include_wire_bodies': 'includeWireBodies',
        'display_state_id': 'displayStateId'
    }

    def __init__(self, document_id=None, workspace_id=None, element_id=None, sketch_id=None, element_microversion_id=None, include_hidden=None, part_query=None, part_id=None, include_wire_bodies=None, display_state_id=None):  # noqa: E501
        """BTBoundingBoxParams - a model defined in OpenAPI"""  # noqa: E501

        self._document_id = None
        self._workspace_id = None
        self._element_id = None
        self._sketch_id = None
        self._element_microversion_id = None
        self._include_hidden = None
        self._part_query = None
        self._part_id = None
        self._include_wire_bodies = None
        self._display_state_id = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if element_id is not None:
            self.element_id = element_id
        if sketch_id is not None:
            self.sketch_id = sketch_id
        if element_microversion_id is not None:
            self.element_microversion_id = element_microversion_id
        if include_hidden is not None:
            self.include_hidden = include_hidden
        if part_query is not None:
            self.part_query = part_query
        if part_id is not None:
            self.part_id = part_id
        if include_wire_bodies is not None:
            self.include_wire_bodies = include_wire_bodies
        if display_state_id is not None:
            self.display_state_id = display_state_id

    @property
    def document_id(self):
        """Gets the document_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The document_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BTBoundingBoxParams.


        :param document_id: The document_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The workspace_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this BTBoundingBoxParams.


        :param workspace_id: The workspace_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def element_id(self):
        """Gets the element_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The element_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._element_id

    @element_id.setter
    def element_id(self, element_id):
        """Sets the element_id of this BTBoundingBoxParams.


        :param element_id: The element_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._element_id = element_id

    @property
    def sketch_id(self):
        """Gets the sketch_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The sketch_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._sketch_id

    @sketch_id.setter
    def sketch_id(self, sketch_id):
        """Sets the sketch_id of this BTBoundingBoxParams.


        :param sketch_id: The sketch_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._sketch_id = sketch_id

    @property
    def element_microversion_id(self):
        """Gets the element_microversion_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The element_microversion_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._element_microversion_id

    @element_microversion_id.setter
    def element_microversion_id(self, element_microversion_id):
        """Sets the element_microversion_id of this BTBoundingBoxParams.


        :param element_microversion_id: The element_microversion_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._element_microversion_id = element_microversion_id

    @property
    def include_hidden(self):
        """Gets the include_hidden of this BTBoundingBoxParams.  # noqa: E501


        :return: The include_hidden of this BTBoundingBoxParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_hidden

    @include_hidden.setter
    def include_hidden(self, include_hidden):
        """Sets the include_hidden of this BTBoundingBoxParams.


        :param include_hidden: The include_hidden of this BTBoundingBoxParams.  # noqa: E501
        :type: bool
        """

        self._include_hidden = include_hidden

    @property
    def part_query(self):
        """Gets the part_query of this BTBoundingBoxParams.  # noqa: E501


        :return: The part_query of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._part_query

    @part_query.setter
    def part_query(self, part_query):
        """Sets the part_query of this BTBoundingBoxParams.


        :param part_query: The part_query of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._part_query = part_query

    @property
    def part_id(self):
        """Gets the part_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The part_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._part_id

    @part_id.setter
    def part_id(self, part_id):
        """Sets the part_id of this BTBoundingBoxParams.


        :param part_id: The part_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._part_id = part_id

    @property
    def include_wire_bodies(self):
        """Gets the include_wire_bodies of this BTBoundingBoxParams.  # noqa: E501


        :return: The include_wire_bodies of this BTBoundingBoxParams.  # noqa: E501
        :rtype: bool
        """
        return self._include_wire_bodies

    @include_wire_bodies.setter
    def include_wire_bodies(self, include_wire_bodies):
        """Sets the include_wire_bodies of this BTBoundingBoxParams.


        :param include_wire_bodies: The include_wire_bodies of this BTBoundingBoxParams.  # noqa: E501
        :type: bool
        """

        self._include_wire_bodies = include_wire_bodies

    @property
    def display_state_id(self):
        """Gets the display_state_id of this BTBoundingBoxParams.  # noqa: E501


        :return: The display_state_id of this BTBoundingBoxParams.  # noqa: E501
        :rtype: str
        """
        return self._display_state_id

    @display_state_id.setter
    def display_state_id(self, display_state_id):
        """Sets the display_state_id of this BTBoundingBoxParams.


        :param display_state_id: The display_state_id of this BTBoundingBoxParams.  # noqa: E501
        :type: str
        """

        self._display_state_id = display_state_id

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
        if not isinstance(other, BTBoundingBoxParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
