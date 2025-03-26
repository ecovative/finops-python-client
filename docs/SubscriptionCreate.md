# SubscriptionCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] 
**account_ref_list_id** | **str** |  | 
**user_email** | **str** |  | 
**db_created_by** | **str** |  | 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.subscription_create import SubscriptionCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCreate from a JSON string
subscription_create_instance = SubscriptionCreate.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCreate.to_json())

# convert the object into a dict
subscription_create_dict = subscription_create_instance.to_dict()
# create an instance of SubscriptionCreate from a dict
subscription_create_from_dict = SubscriptionCreate.from_dict(subscription_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


