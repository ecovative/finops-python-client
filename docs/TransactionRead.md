# TransactionRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fq_txn_link_key** | **str** |  | [optional] 
**time_modified** | **datetime** |  | [optional] 
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
**account** | [**AccountBase**](AccountBase.md) |  | [optional] 
**entity** | [**EntityBase**](EntityBase.md) |  | [optional] 
**class_code** | [**ClassCodeBase**](ClassCodeBase.md) |  | [optional] 

## Example

```python
from finops_client.models.transaction_read import TransactionRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRead from a JSON string
transaction_read_instance = TransactionRead.from_json(json)
# print the JSON string representation of the object
print(TransactionRead.to_json())

# convert the object into a dict
transaction_read_dict = transaction_read_instance.to_dict()
# create an instance of TransactionRead from a dict
transaction_read_from_dict = TransactionRead.from_dict(transaction_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


