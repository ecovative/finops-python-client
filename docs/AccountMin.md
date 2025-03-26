# AccountMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | 
**time_modified** | **datetime** |  | 
**edit_sequence** | **int** |  | 

## Example

```python
from finops_client.models.account_min import AccountMin

# TODO update the JSON string below
json = "{}"
# create an instance of AccountMin from a JSON string
account_min_instance = AccountMin.from_json(json)
# print the JSON string representation of the object
print(AccountMin.to_json())

# convert the object into a dict
account_min_dict = account_min_instance.to_dict()
# create an instance of AccountMin from a dict
account_min_from_dict = AccountMin.from_dict(account_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


