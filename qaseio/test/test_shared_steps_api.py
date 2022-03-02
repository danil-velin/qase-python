# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import qaseio
from qaseio.api.shared_steps_api import SharedStepsApi  # noqa: E501
from qaseio.rest import ApiException


class TestSharedStepsApi(unittest.TestCase):
    """SharedStepsApi unit test stubs"""

    def setUp(self):
        self.api = SharedStepsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_shared_step(self):
        """Test case for create_shared_step

        Create a new shared step.  # noqa: E501
        """
        pass

    def test_delete_shared_step(self):
        """Test case for delete_shared_step

        Delete shared step.  # noqa: E501
        """
        pass

    def test_get_shared_step(self):
        """Test case for get_shared_step

        Get a specific shared step.  # noqa: E501
        """
        pass

    def test_get_shared_steps(self):
        """Test case for get_shared_steps

        Get all shared steps.  # noqa: E501
        """
        pass

    def test_update_shared_step(self):
        """Test case for update_shared_step

        Update shared step.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
