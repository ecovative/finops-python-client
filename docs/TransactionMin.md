# TransactionMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fq_txn_link_key** | **str** |  | 
**time_modified** | **datetime** |  | 
**class_ref_list_id** | **str** |  | [optional] 

## Example

```python
from finops_client.models.transaction_min import TransactionMin

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMin from a JSON string
transaction_min_instance = TransactionMin.from_json(json)
# print the JSON string representation of the object
print(TransactionMin.to_json())

# convert the object into a dict
transaction_min_dict = transaction_min_instance.to_dict()
# create an instance of TransactionMin from a dict
transaction_min_from_dict = TransactionMin.from_dict(transaction_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


