# finops_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_users_users_post**](UsersApi.md#create_users_users_post) | **POST** /users/ | Create Users
[**delete_users_users_delete_post**](UsersApi.md#delete_users_users_delete_post) | **POST** /users/delete/ | Delete Users
[**read_user_users_user_email_get**](UsersApi.md#read_user_users_user_email_get) | **GET** /users/{UserEmail}/ | Read User
[**read_users_users_get**](UsersApi.md#read_users_users_get) | **GET** /users/ | Read Users
[**update_users_users_patch**](UsersApi.md#update_users_users_patch) | **PATCH** /users/ | Update Users


# **create_users_users_post**
> List[UserBase] create_users_users_post(create_users_users_post_request_inner)

Create Users

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.create_users_users_post_request_inner import CreateUsersUsersPostRequestInner
from finops_client.models.user_base import UserBase
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
    api_instance = finops_client.UsersApi(api_client)
    create_users_users_post_request_inner = [finops_client.CreateUsersUsersPostRequestInner()] # List[CreateUsersUsersPostRequestInner] | 

    try:
        # Create Users
        api_response = api_instance.create_users_users_post(create_users_users_post_request_inner)
        print("The response of UsersApi->create_users_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_users_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_users_users_post_request_inner** | [**List[CreateUsersUsersPostRequestInner]**](CreateUsersUsersPostRequestInner.md)|  | 

### Return type

[**List[UserBase]**](UserBase.md)

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

# **delete_users_users_delete_post**
> List[UserBase] delete_users_users_delete_post(request_body)

Delete Users

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.user_base import UserBase
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
    api_instance = finops_client.UsersApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Delete Users
        api_response = api_instance.delete_users_users_delete_post(request_body)
        print("The response of UsersApi->delete_users_users_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_users_users_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**List[UserBase]**](UserBase.md)

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

# **read_user_users_user_email_get**
> UserRead read_user_users_user_email_get(user_email)

Read User

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.user_read import UserRead
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
    api_instance = finops_client.UsersApi(api_client)
    user_email = 'user_email_example' # str | 

    try:
        # Read User
        api_response = api_instance.read_user_users_user_email_get(user_email)
        print("The response of UsersApi->read_user_users_user_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->read_user_users_user_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_email** | **str**|  | 

### Return type

[**UserRead**](UserRead.md)

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

# **read_users_users_get**
> List[UserBase] read_users_users_get(skip=skip, limit=limit, user_email=user_email, app_role=app_role, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date)

Read Users

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.app_role import AppRole
from finops_client.models.user_base import UserBase
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
    api_instance = finops_client.UsersApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    user_email = [] # List[str] |  (optional) (default to [])
    app_role = [] # List[AppRole] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Read Users
        api_response = api_instance.read_users_users_get(skip=skip, limit=limit, user_email=user_email, app_role=app_role, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date)
        print("The response of UsersApi->read_users_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->read_users_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **user_email** | [**List[str]**](str.md)|  | [optional] [default to []]
 **app_role** | [**List[AppRole]**](AppRole.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

### Return type

[**List[UserBase]**](UserBase.md)

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

# **update_users_users_patch**
> List[UserBase] update_users_users_patch(user_update)

Update Users

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.user_base import UserBase
from finops_client.models.user_update import UserUpdate
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
    api_instance = finops_client.UsersApi(api_client)
    user_update = [finops_client.UserUpdate()] # List[UserUpdate] | 

    try:
        # Update Users
        api_response = api_instance.update_users_users_patch(user_update)
        print("The response of UsersApi->update_users_users_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_users_users_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_update** | [**List[UserUpdate]**](UserUpdate.md)|  | 

### Return type

[**List[UserBase]**](UserBase.md)

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

