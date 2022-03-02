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

class TestCaseListResponseResult(object):
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
        'total': 'int',
        'filtered': 'int',
        'count': 'int',
        'entities': 'list[TestCase]'
    }

    attribute_map = {
        'total': 'total',
        'filtered': 'filtered',
        'count': 'count',
        'entities': 'entities'
    }

    def __init__(self, total=None, filtered=None, count=None, entities=None):  # noqa: E501
        """TestCaseListResponseResult - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._filtered = None
        self._count = None
        self._entities = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if filtered is not None:
            self.filtered = filtered
        if count is not None:
            self.count = count
        if entities is not None:
            self.entities = entities

    @property
    def total(self):
        """Gets the total of this TestCaseListResponseResult.  # noqa: E501


        :return: The total of this TestCaseListResponseResult.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TestCaseListResponseResult.


        :param total: The total of this TestCaseListResponseResult.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def filtered(self):
        """Gets the filtered of this TestCaseListResponseResult.  # noqa: E501


        :return: The filtered of this TestCaseListResponseResult.  # noqa: E501
        :rtype: int
        """
        return self._filtered

    @filtered.setter
    def filtered(self, filtered):
        """Sets the filtered of this TestCaseListResponseResult.


        :param filtered: The filtered of this TestCaseListResponseResult.  # noqa: E501
        :type: int
        """

        self._filtered = filtered

    @property
    def count(self):
        """Gets the count of this TestCaseListResponseResult.  # noqa: E501


        :return: The count of this TestCaseListResponseResult.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TestCaseListResponseResult.


        :param count: The count of this TestCaseListResponseResult.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def entities(self):
        """Gets the entities of this TestCaseListResponseResult.  # noqa: E501


        :return: The entities of this TestCaseListResponseResult.  # noqa: E501
        :rtype: list[TestCase]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this TestCaseListResponseResult.


        :param entities: The entities of this TestCaseListResponseResult.  # noqa: E501
        :type: list[TestCase]
        """

        self._entities = entities

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
        if issubclass(TestCaseListResponseResult, dict):
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
        if not isinstance(other, TestCaseListResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
