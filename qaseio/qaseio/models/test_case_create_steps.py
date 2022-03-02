# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TestCaseCreateSteps(object):
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
        'action': 'str',
        'expected_result': 'str',
        'data': 'str',
        'position': 'int',
        'attachments': 'AttachmentHashList'
    }

    attribute_map = {
        'action': 'action',
        'expected_result': 'expected_result',
        'data': 'data',
        'position': 'position',
        'attachments': 'attachments'
    }

    def __init__(self, action=None, expected_result=None, data=None, position=None, attachments=None):  # noqa: E501
        """TestCaseCreateSteps - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._expected_result = None
        self._data = None
        self._position = None
        self._attachments = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if expected_result is not None:
            self.expected_result = expected_result
        if data is not None:
            self.data = data
        if position is not None:
            self.position = position
        if attachments is not None:
            self.attachments = attachments

    @property
    def action(self):
        """Gets the action of this TestCaseCreateSteps.  # noqa: E501


        :return: The action of this TestCaseCreateSteps.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TestCaseCreateSteps.


        :param action: The action of this TestCaseCreateSteps.  # noqa: E501
        :type: str
        """

        self._action = action

    @property
    def expected_result(self):
        """Gets the expected_result of this TestCaseCreateSteps.  # noqa: E501


        :return: The expected_result of this TestCaseCreateSteps.  # noqa: E501
        :rtype: str
        """
        return self._expected_result

    @expected_result.setter
    def expected_result(self, expected_result):
        """Sets the expected_result of this TestCaseCreateSteps.


        :param expected_result: The expected_result of this TestCaseCreateSteps.  # noqa: E501
        :type: str
        """

        self._expected_result = expected_result

    @property
    def data(self):
        """Gets the data of this TestCaseCreateSteps.  # noqa: E501


        :return: The data of this TestCaseCreateSteps.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TestCaseCreateSteps.


        :param data: The data of this TestCaseCreateSteps.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def position(self):
        """Gets the position of this TestCaseCreateSteps.  # noqa: E501


        :return: The position of this TestCaseCreateSteps.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TestCaseCreateSteps.


        :param position: The position of this TestCaseCreateSteps.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def attachments(self):
        """Gets the attachments of this TestCaseCreateSteps.  # noqa: E501


        :return: The attachments of this TestCaseCreateSteps.  # noqa: E501
        :rtype: AttachmentHashList
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this TestCaseCreateSteps.


        :param attachments: The attachments of this TestCaseCreateSteps.  # noqa: E501
        :type: AttachmentHashList
        """

        self._attachments = attachments

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
        if issubclass(TestCaseCreateSteps, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TestCaseCreateSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
