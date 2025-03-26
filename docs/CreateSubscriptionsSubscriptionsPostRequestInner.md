# CreateSubscriptionsSubscriptionsPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | 
**account_ref_list_id** | **str** |  | 
**user_email** | **str** |  | 
**db_created_by** | **str** |  | 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.create_subscriptions_subscriptions_post_request_inner import CreateSubscriptionsSubscriptionsPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionsSubscriptionsPostRequestInner from a JSON string
create_subscriptions_subscriptions_post_request_inner_instance = CreateSubscriptionsSubscriptionsPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionsSubscriptionsPostRequestInner.to_json())

# convert the object into a dict
create_subscriptions_subscriptions_post_request_inner_dict = create_subscriptions_subscriptions_post_request_inner_instance.to_dict()
# create an instance of CreateSubscriptionsSubscriptionsPostRequestInner from a dict
create_subscriptions_subscriptions_post_request_inner_from_dict = CreateSubscriptionsSubscriptionsPostRequestInner.from_dict(create_subscriptions_subscriptions_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


