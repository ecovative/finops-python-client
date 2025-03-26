# UserRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** |  | [optional] 
**app_role** | [**AppRole**](AppRole.md) |  | [optional] 
**last_time_logged_in** | **datetime** |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 
**subscriptions** | [**List[SubscriptionBase]**](SubscriptionBase.md) |  | [optional] [default to []]

## Example

```python
from finops_client.models.user_read import UserRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserRead from a JSON string
user_read_instance = UserRead.from_json(json)
# print the JSON string representation of the object
print(UserRead.to_json())

# convert the object into a dict
user_read_dict = user_read_instance.to_dict()
# create an instance of UserRead from a dict
user_read_from_dict = UserRead.from_dict(user_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


