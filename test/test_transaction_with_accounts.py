# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from finops_client.models.transaction_with_accounts import TransactionWithAccounts

class TestTransactionWithAccounts(unittest.TestCase):
    """TransactionWithAccounts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionWithAccounts:
        """Test TransactionWithAccounts
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionWithAccounts`
        """
        model = TransactionWithAccounts()
        if include_optional:
            return TransactionWithAccounts(
                list_id = '',
                time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                edit_sequence = 56,
                name = '',
                full_name = '',
                is_active = True,
                parent_ref_list_id = '',
                parent_ref_full_name = '',
                sublevel = 56,
                account_type = 'Income',
                special_account_type = '',
                is_tax_account = True,
                account_number = 56,
                bank_number = '',
                desc = '',
                description = '',
                open_balance = 1.337,
                total_balance = 1.337,
                open_balance_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sales_tax_code_ref_list_id = '',
                sales_tax_code_ref_full_name = '',
                tax_code_ref_list_id = '',
                tax_code_ref_full_name = '',
                tax_line_info_ret_tax_line_id = '',
                tax_line_info_ret_tax_line_name = '',
                cash_flow_classification = 'Operating',
                currency_ref_list_id = '',
                currency_ref_full_name = '',
                time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                source = 'ESS-BV',
                statement_level = 'Ordinary Income/Expense',
                default_currency = 'AED',
                is_intercompany = True,
                db_created_by = '',
                db_time_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                db_time_modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                fq_txn_link_key = '',
                class_ref_list_id = '',
                txn_type = 'Bill',
                txn_id = '',
                txn_line_id = '',
                entity_ref_list_id = '',
                entity_ref_full_name = '',
                account_ref_list_id = '',
                account_ref_full_name = '',
                class_ref_full_name = '',
                txn_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                ref_number = '',
                amount = 1.337,
                exchange_rate = 1.337,
                amount_in_home_currency = 1.337,
                memo = '',
                fq_journal_entry_link_key = '',
                fq_primary_key = ''
            )
        else:
            return TransactionWithAccounts(
        )
        """

    def testTransactionWithAccounts(self):
        """Test TransactionWithAccounts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
