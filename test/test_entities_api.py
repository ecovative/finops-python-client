# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from finops_client.api.entities_api import EntitiesApi


class TestEntitiesApi(unittest.TestCase):
    """EntitiesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EntitiesApi()

    def tearDown(self) -> None:
        pass

    def test_create_entities_entities_post(self) -> None:
        """Test case for create_entities_entities_post

        Create Entities
        """
        pass

    def test_delete_entities_entities_delete_post(self) -> None:
        """Test case for delete_entities_entities_delete_post

        Delete Entities
        """
        pass

    def test_read_entities_entities_get(self) -> None:
        """Test case for read_entities_entities_get

        Read Entities
        """
        pass

    def test_read_entity_entities_list_id_get(self) -> None:
        """Test case for read_entity_entities_list_id_get

        Read Entity
        """
        pass

    def test_update_entities_entities_patch(self) -> None:
        """Test case for update_entities_entities_patch

        Update Entities
        """
        pass


if __name__ == '__main__':
    unittest.main()
