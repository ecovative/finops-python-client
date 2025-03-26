# finops_client.ClassCodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_class_codes_class_codes_post**](ClassCodesApi.md#create_class_codes_class_codes_post) | **POST** /class_codes/ | Create Class Codes
[**delete_class_codes_class_codes_delete_post**](ClassCodesApi.md#delete_class_codes_class_codes_delete_post) | **POST** /class_codes/delete/ | Delete Class Codes
[**read_class_code_class_codes_list_id_get**](ClassCodesApi.md#read_class_code_class_codes_list_id_get) | **GET** /class_codes/{ListID} | Read Class Code
[**read_class_codes_class_codes_get**](ClassCodesApi.md#read_class_codes_class_codes_get) | **GET** /class_codes/ | Read Class Codes
[**update_class_codes_class_codes_patch**](ClassCodesApi.md#update_class_codes_class_codes_patch) | **PATCH** /class_codes/ | Update Class Codes


# **create_class_codes_class_codes_post**
> List[Optional[str]] create_class_codes_class_codes_post(class_code_create)

Create Class Codes

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.class_code_create import ClassCodeCreate
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
    api_instance = finops_client.ClassCodesApi(api_client)
    class_code_create = [finops_client.ClassCodeCreate()] # List[ClassCodeCreate] | 

    try:
        # Create Class Codes
        api_response = api_instance.create_class_codes_class_codes_post(class_code_create)
        print("The response of ClassCodesApi->create_class_codes_class_codes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassCodesApi->create_class_codes_class_codes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_code_create** | [**List[ClassCodeCreate]**](ClassCodeCreate.md)|  | 

### Return type

**List[Optional[str]]**

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

# **delete_class_codes_class_codes_delete_post**
> List[ClassCodeBase] delete_class_codes_class_codes_delete_post(request_body)

Delete Class Codes

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.class_code_base import ClassCodeBase
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
    api_instance = finops_client.ClassCodesApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Delete Class Codes
        api_response = api_instance.delete_class_codes_class_codes_delete_post(request_body)
        print("The response of ClassCodesApi->delete_class_codes_class_codes_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassCodesApi->delete_class_codes_class_codes_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**List[ClassCodeBase]**](ClassCodeBase.md)

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

# **read_class_code_class_codes_list_id_get**
> ClassCodeRead read_class_code_class_codes_list_id_get(list_id)

Read Class Code

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.class_code_read import ClassCodeRead
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
    api_instance = finops_client.ClassCodesApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Read Class Code
        api_response = api_instance.read_class_code_class_codes_list_id_get(list_id)
        print("The response of ClassCodesApi->read_class_code_class_codes_list_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassCodesApi->read_class_code_class_codes_list_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

[**ClassCodeRead**](ClassCodeRead.md)

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

# **read_class_codes_class_codes_get**
> List[ReadClassCodesClassCodesGet200ResponseInner] read_class_codes_class_codes_get(skip=skip, limit=limit, list_id=list_id, name=name, full_name=full_name, is_active=is_active, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, minimal=minimal)

Read Class Codes

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.read_class_codes_class_codes_get200_response_inner import ReadClassCodesClassCodesGet200ResponseInner
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
    api_instance = finops_client.ClassCodesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    list_id = [] # List[str] |  (optional) (default to [])
    name = [] # List[str] |  (optional) (default to [])
    full_name = [] # List[str] |  (optional) (default to [])
    is_active = [true] # List[bool] |  (optional) (default to [true])
    parent_ref_list_id = [] # List[str] |  (optional) (default to [])
    sublevel = [] # List[int] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    minimal = True # bool |  (optional)

    try:
        # Read Class Codes
        api_response = api_instance.read_class_codes_class_codes_get(skip=skip, limit=limit, list_id=list_id, name=name, full_name=full_name, is_active=is_active, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, minimal=minimal)
        print("The response of ClassCodesApi->read_class_codes_class_codes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassCodesApi->read_class_codes_class_codes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **full_name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **is_active** | [**List[bool]**](bool.md)|  | [optional] [default to [true]]
 **parent_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **sublevel** | [**List[int]**](int.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **minimal** | **bool**|  | [optional] 

### Return type

[**List[ReadClassCodesClassCodesGet200ResponseInner]**](ReadClassCodesClassCodesGet200ResponseInner.md)

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

# **update_class_codes_class_codes_patch**
> List[ClassCodeBase] update_class_codes_class_codes_patch(class_code_update)

Update Class Codes

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.class_code_base import ClassCodeBase
from finops_client.models.class_code_update import ClassCodeUpdate
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
    api_instance = finops_client.ClassCodesApi(api_client)
    class_code_update = [finops_client.ClassCodeUpdate()] # List[ClassCodeUpdate] | 

    try:
        # Update Class Codes
        api_response = api_instance.update_class_codes_class_codes_patch(class_code_update)
        print("The response of ClassCodesApi->update_class_codes_class_codes_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassCodesApi->update_class_codes_class_codes_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_code_update** | [**List[ClassCodeUpdate]**](ClassCodeUpdate.md)|  | 

### Return type

[**List[ClassCodeBase]**](ClassCodeBase.md)

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

