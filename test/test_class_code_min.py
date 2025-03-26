# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from finops_client.models.class_code_min import ClassCodeMin

class TestClassCodeMin(unittest.TestCase):
    """ClassCodeMin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClassCodeMin:
        """Test ClassCodeMin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClassCodeMin`
        """
        model = ClassCodeMin()
        if include_optional:
            return ClassCodeMin(
                list_id = '',
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                edit_sequence = 56
            )
        else:
            return ClassCodeMin(
                list_id = '',
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                edit_sequence = 56,
        )
        """

    def testClassCodeMin(self):
        """Test ClassCodeMin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
