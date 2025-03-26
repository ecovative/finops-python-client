# finops_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_users_admin_get_active_users_get**](AdminApi.md#get_active_users_admin_get_active_users_get) | **GET** /admin/get_active_users/ | Get Active Users
[**get_db_instance_name_admin_get_db_instance_name_get**](AdminApi.md#get_db_instance_name_admin_get_db_instance_name_get) | **GET** /admin/get_db_instance_name/ | Get Db Instance Name


# **get_active_users_admin_get_active_users_get**
> List[Optional[str]] get_active_users_admin_get_active_users_get()

Get Active Users

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
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
    api_instance = finops_client.AdminApi(api_client)

    try:
        # Get Active Users
        api_response = api_instance.get_active_users_admin_get_active_users_get()
        print("The response of AdminApi->get_active_users_admin_get_active_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_active_users_admin_get_active_users_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Optional[str]]**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_db_instance_name_admin_get_db_instance_name_get**
> object get_db_instance_name_admin_get_db_instance_name_get()

Get Db Instance Name

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
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
    api_instance = finops_client.AdminApi(api_client)

    try:
        # Get Db Instance Name
        api_response = api_instance.get_db_instance_name_admin_get_db_instance_name_get()
        print("The response of AdminApi->get_db_instance_name_admin_get_db_instance_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_db_instance_name_admin_get_db_instance_name_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

