# TransactionWithAccounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | [optional] 
**time_modified** | **datetime** |  | [optional] 
**edit_sequence** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**parent_ref_list_id** | **str** |  | [optional] 
**parent_ref_full_name** | **str** |  | [optional] 
**sublevel** | **int** |  | [optional] 
**account_type** | [**TypeOfAccount**](TypeOfAccount.md) |  | [optional] 
**special_account_type** | **str** |  | [optional] 
**is_tax_account** | **bool** |  | [optional] 
**account_number** | **int** |  | [optional] 
**bank_number** | **str** |  | [optional] 
**desc** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**open_balance** | **float** |  | [optional] 
**total_balance** | **float** |  | [optional] 
**open_balance_date** | **datetime** |  | [optional] 
**sales_tax_code_ref_list_id** | **str** |  | [optional] 
**sales_tax_code_ref_full_name** | **str** |  | [optional] 
**tax_code_ref_list_id** | **str** |  | [optional] 
**tax_code_ref_full_name** | **str** |  | [optional] 
**tax_line_info_ret_tax_line_id** | **str** |  | [optional] 
**tax_line_info_ret_tax_line_name** | **str** |  | [optional] 
**cash_flow_classification** | [**CashFlowClassification**](CashFlowClassification.md) |  | [optional] 
**currency_ref_list_id** | **str** |  | [optional] 
**currency_ref_full_name** | **str** |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**statement_level** | [**StatementLevel**](StatementLevel.md) |  | [optional] 
**default_currency** | **str** |  | [optional] 
**is_intercompany** | **bool** |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 
**fq_txn_link_key** | **str** |  | [optional] 
**class_ref_list_id** | **str** |  | [optional] 
**txn_type** | [**TransactionType**](TransactionType.md) |  | [optional] 
**txn_id** | **str** |  | [optional] 
**txn_line_id** | **str** |  | [optional] 
**entity_ref_list_id** | **str** |  | [optional] 
**entity_ref_full_name** | **str** |  | [optional] 
**account_ref_list_id** | **str** |  | [optional] 
**account_ref_full_name** | **str** |  | [optional] 
**class_ref_full_name** | **str** |  | [optional] 
**txn_date** | **date** |  | [optional] 
**ref_number** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**amount_in_home_currency** | **float** |  | [optional] 
**memo** | **str** |  | [optional] 
**fq_journal_entry_link_key** | **str** |  | [optional] 
**fq_primary_key** | **str** |  | [optional] 

## Example

```python
from finops_client.models.transaction_with_accounts import TransactionWithAccounts

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionWithAccounts from a JSON string
transaction_with_accounts_instance = TransactionWithAccounts.from_json(json)
# print the JSON string representation of the object
print(TransactionWithAccounts.to_json())

# convert the object into a dict
transaction_with_accounts_dict = transaction_with_accounts_instance.to_dict()
# create an instance of TransactionWithAccounts from a dict
transaction_with_accounts_from_dict = TransactionWithAccounts.from_dict(transaction_with_accounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


