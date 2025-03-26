# CreateUsersUsersPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** |  | 
**app_role** | [**AppRole**](AppRole.md) |  | [optional] 
**last_time_logged_in** | **datetime** |  | [optional] 
**db_created_by** | **str** |  | 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.create_users_users_post_request_inner import CreateUsersUsersPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUsersUsersPostRequestInner from a JSON string
create_users_users_post_request_inner_instance = CreateUsersUsersPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateUsersUsersPostRequestInner.to_json())

# convert the object into a dict
create_users_users_post_request_inner_dict = create_users_users_post_request_inner_instance.to_dict()
# create an instance of CreateUsersUsersPostRequestInner from a dict
create_users_users_post_request_inner_from_dict = CreateUsersUsersPostRequestInner.from_dict(create_users_users_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


