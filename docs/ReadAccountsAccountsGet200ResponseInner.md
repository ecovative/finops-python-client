# ReadAccountsAccountsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | 
**time_modified** | **datetime** |  | 
**edit_sequence** | **int** |  | 
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

## Example

```python
from finops_client.models.read_accounts_accounts_get200_response_inner import ReadAccountsAccountsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadAccountsAccountsGet200ResponseInner from a JSON string
read_accounts_accounts_get200_response_inner_instance = ReadAccountsAccountsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ReadAccountsAccountsGet200ResponseInner.to_json())

# convert the object into a dict
read_accounts_accounts_get200_response_inner_dict = read_accounts_accounts_get200_response_inner_instance.to_dict()
# create an instance of ReadAccountsAccountsGet200ResponseInner from a dict
read_accounts_accounts_get200_response_inner_from_dict = ReadAccountsAccountsGet200ResponseInner.from_dict(read_accounts_accounts_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


