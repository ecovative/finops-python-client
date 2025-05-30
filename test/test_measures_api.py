# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from finops_client.api.measures_api import MeasuresApi


class TestMeasuresApi(unittest.TestCase):
    """MeasuresApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MeasuresApi()

    def tearDown(self) -> None:
        pass

    def test_create_measures_measures_post(self) -> None:
        """Test case for create_measures_measures_post

        Create Measures
        """
        pass

    def test_delete_measures_measures_delete_post(self) -> None:
        """Test case for delete_measures_measures_delete_post

        Delete Measures
        """
        pass

    def test_read_measure_measures_measure_id_get(self) -> None:
        """Test case for read_measure_measures_measure_id_get

        Read Measure
        """
        pass

    def test_read_measures_measures_get(self) -> None:
        """Test case for read_measures_measures_get

        Read Measures
        """
        pass

    def test_update_measures_measures_patch(self) -> None:
        """Test case for update_measures_measures_patch

        Update Measures
        """
        pass


if __name__ == '__main__':
    unittest.main()
