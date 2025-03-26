# ReadTransactionsTransactionsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fq_txn_link_key** | **str** |  | 
**time_modified** | **datetime** |  | 
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
**currency_ref_list_id** | **str** |  | [optional] 
**currency_ref_full_name** | **str** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**amount_in_home_currency** | **float** |  | [optional] 
**memo** | **str** |  | [optional] 
**fq_journal_entry_link_key** | **str** |  | [optional] 
**fq_primary_key** | **str** |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.read_transactions_transactions_get200_response_inner import ReadTransactionsTransactionsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadTransactionsTransactionsGet200ResponseInner from a JSON string
read_transactions_transactions_get200_response_inner_instance = ReadTransactionsTransactionsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ReadTransactionsTransactionsGet200ResponseInner.to_json())

# convert the object into a dict
read_transactions_transactions_get200_response_inner_dict = read_transactions_transactions_get200_response_inner_instance.to_dict()
# create an instance of ReadTransactionsTransactionsGet200ResponseInner from a dict
read_transactions_transactions_get200_response_inner_from_dict = ReadTransactionsTransactionsGet200ResponseInner.from_dict(read_transactions_transactions_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


