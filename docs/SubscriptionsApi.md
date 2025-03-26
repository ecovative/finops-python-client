# finops_client.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscriptions_subscriptions_post**](SubscriptionsApi.md#create_subscriptions_subscriptions_post) | **POST** /subscriptions/ | Create Subscriptions
[**delete_subscriptions_subscriptions_delete_post**](SubscriptionsApi.md#delete_subscriptions_subscriptions_delete_post) | **POST** /subscriptions/delete/ | Delete Subscriptions
[**read_subscription_subscriptions_subscription_id_get**](SubscriptionsApi.md#read_subscription_subscriptions_subscription_id_get) | **GET** /subscriptions/{SubscriptionID}/ | Read Subscription
[**read_subscriptions_subscriptions_get**](SubscriptionsApi.md#read_subscriptions_subscriptions_get) | **GET** /subscriptions/ | Read Subscriptions
[**update_subscriptions_subscriptions_patch**](SubscriptionsApi.md#update_subscriptions_subscriptions_patch) | **PATCH** /subscriptions/ | Update Subscriptions


# **create_subscriptions_subscriptions_post**
> List[int] create_subscriptions_subscriptions_post(create_subscriptions_subscriptions_post_request_inner)

Create Subscriptions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.create_subscriptions_subscriptions_post_request_inner import CreateSubscriptionsSubscriptionsPostRequestInner
from finops_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = finops_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with finops_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finops_client.SubscriptionsApi(api_client)
    create_subscriptions_subscriptions_post_request_inner = [finops_client.CreateSubscriptionsSubscriptionsPostRequestInner()] # List[CreateSubscriptionsSubscriptionsPostRequestInner] | 

    try:
        # Create Subscriptions
        api_response = api_instance.create_subscriptions_subscriptions_post(create_subscriptions_subscriptions_post_request_inner)
        print("The response of SubscriptionsApi->create_subscriptions_subscriptions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->create_subscriptions_subscriptions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_subscriptions_subscriptions_post_request_inner** | [**List[CreateSubscriptionsSubscriptionsPostRequestInner]**](CreateSubscriptionsSubscriptionsPostRequestInner.md)|  | 

### Return type

**List[int]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriptions_subscriptions_delete_post**
> List[SubscriptionBase] delete_subscriptions_subscriptions_delete_post(request_body)

Delete Subscriptions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.subscription_base import SubscriptionBase
from finops_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = finops_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with finops_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finops_client.SubscriptionsApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Delete Subscriptions
        api_response = api_instance.delete_subscriptions_subscriptions_delete_post(request_body)
        print("The response of SubscriptionsApi->delete_subscriptions_subscriptions_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete_subscriptions_subscriptions_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

[**List[SubscriptionBase]**](SubscriptionBase.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_subscription_subscriptions_subscription_id_get**
> SubscriptionRead read_subscription_subscriptions_subscription_id_get(subscription_id)

Read Subscription

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.subscription_read import SubscriptionRead
from finops_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = finops_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with finops_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finops_client.SubscriptionsApi(api_client)
    subscription_id = 56 # int | 

    try:
        # Read Subscription
        api_response = api_instance.read_subscription_subscriptions_subscription_id_get(subscription_id)
        print("The response of SubscriptionsApi->read_subscription_subscriptions_subscription_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->read_subscription_subscriptions_subscription_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 

### Return type

[**SubscriptionRead**](SubscriptionRead.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_subscriptions_subscriptions_get**
> List[SubscriptionBase] read_subscriptions_subscriptions_get(skip=skip, limit=limit, subscription_id=subscription_id, account_ref_list_id=account_ref_list_id, user_email=user_email, db_created_by=db_created_by)

Read Subscriptions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.subscription_base import SubscriptionBase
from finops_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = finops_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with finops_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finops_client.SubscriptionsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    subscription_id = [] # List[Optional[str]] |  (optional) (default to [])
    account_ref_list_id = [] # List[str] |  (optional) (default to [])
    user_email = [] # List[Optional[str]] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])

    try:
        # Read Subscriptions
        api_response = api_instance.read_subscriptions_subscriptions_get(skip=skip, limit=limit, subscription_id=subscription_id, account_ref_list_id=account_ref_list_id, user_email=user_email, db_created_by=db_created_by)
        print("The response of SubscriptionsApi->read_subscriptions_subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->read_subscriptions_subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **subscription_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **account_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **user_email** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]

### Return type

[**List[SubscriptionBase]**](SubscriptionBase.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscriptions_subscriptions_patch**
> List[SubscriptionBase] update_subscriptions_subscriptions_patch(subscription_update)

Update Subscriptions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.subscription_base import SubscriptionBase
from finops_client.models.subscription_update import SubscriptionUpdate
from finops_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = finops_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with finops_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finops_client.SubscriptionsApi(api_client)
    subscription_update = [finops_client.SubscriptionUpdate()] # List[SubscriptionUpdate] | 

    try:
        # Update Subscriptions
        api_response = api_instance.update_subscriptions_subscriptions_patch(subscription_update)
        print("The response of SubscriptionsApi->update_subscriptions_subscriptions_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->update_subscriptions_subscriptions_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_update** | [**List[SubscriptionUpdate]**](SubscriptionUpdate.md)|  | 

### Return type

[**List[SubscriptionBase]**](SubscriptionBase.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

