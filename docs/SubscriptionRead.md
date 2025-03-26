# SubscriptionRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] 
**account_ref_list_id** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 
**account** | [**AccountBase**](AccountBase.md) |  | [optional] 

## Example

```python
from finops_client.models.subscription_read import SubscriptionRead

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRead from a JSON string
subscription_read_instance = SubscriptionRead.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRead.to_json())

# convert the object into a dict
subscription_read_dict = subscription_read_instance.to_dict()
# create an instance of SubscriptionRead from a dict
subscription_read_from_dict = SubscriptionRead.from_dict(subscription_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


