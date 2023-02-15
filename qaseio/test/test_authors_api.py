"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by: https://openapi-generator.tech
"""


import unittest

import qaseio
from qaseio.api.authors_api import AuthorsApi  # noqa: E501


class TestAuthorsApi(unittest.TestCase):
    """AuthorsApi unit test stubs"""

    def setUp(self):
        self.api = AuthorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_author(self):
        """Test case for get_author

        Get a specific author.  # noqa: E501
        """
        pass

    def test_get_authors(self):
        """Test case for get_authors

        Get all authors.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
