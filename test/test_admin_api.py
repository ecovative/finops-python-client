# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from finops_client.api.admin_api import AdminApi


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdminApi()

    def tearDown(self) -> None:
        pass

    def test_get_active_users_admin_get_active_users_get(self) -> None:
        """Test case for get_active_users_admin_get_active_users_get

        Get Active Users
        """
        pass

    def test_get_db_instance_name_admin_get_db_instance_name_get(self) -> None:
        """Test case for get_db_instance_name_admin_get_db_instance_name_get

        Get Db Instance Name
        """
        pass


if __name__ == '__main__':
    unittest.main()
