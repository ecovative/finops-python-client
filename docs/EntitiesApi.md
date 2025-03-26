# finops_client.EntitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entities_entities_post**](EntitiesApi.md#create_entities_entities_post) | **POST** /entities/ | Create Entities
[**delete_entities_entities_delete_post**](EntitiesApi.md#delete_entities_entities_delete_post) | **POST** /entities/delete | Delete Entities
[**read_entities_entities_get**](EntitiesApi.md#read_entities_entities_get) | **GET** /entities/ | Read Entities
[**read_entity_entities_list_id_get**](EntitiesApi.md#read_entity_entities_list_id_get) | **GET** /entities/{ListID} | Read Entity
[**update_entities_entities_patch**](EntitiesApi.md#update_entities_entities_patch) | **PATCH** /entities/ | Update Entities


# **create_entities_entities_post**
> List[Optional[str]] create_entities_entities_post(entity_update)

Create Entities

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.entity_update import EntityUpdate
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
    api_instance = finops_client.EntitiesApi(api_client)
    entity_update = [finops_client.EntityUpdate()] # List[EntityUpdate] | 

    try:
        # Create Entities
        api_response = api_instance.create_entities_entities_post(entity_update)
        print("The response of EntitiesApi->create_entities_entities_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->create_entities_entities_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_update** | [**List[EntityUpdate]**](EntityUpdate.md)|  | 

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

# **delete_entities_entities_delete_post**
> List[EntityBase] delete_entities_entities_delete_post(request_body)

Delete Entities

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.entity_base import EntityBase
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
    api_instance = finops_client.EntitiesApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Delete Entities
        api_response = api_instance.delete_entities_entities_delete_post(request_body)
        print("The response of EntitiesApi->delete_entities_entities_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->delete_entities_entities_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**List[EntityBase]**](EntityBase.md)

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

# **read_entities_entities_get**
> List[ReadEntitiesEntitiesGet200ResponseInner] read_entities_entities_get(skip=skip, limit=limit, list_id=list_id, name=name, full_name=full_name, is_active=is_active, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, class_ref_list_id=class_ref_list_id, company_name=company_name, type=type, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, minimal=minimal)

Read Entities

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.entity_type import EntityType
from finops_client.models.read_entities_entities_get200_response_inner import ReadEntitiesEntitiesGet200ResponseInner
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
    api_instance = finops_client.EntitiesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    list_id = [] # List[str] |  (optional) (default to [])
    name = [] # List[str] |  (optional) (default to [])
    full_name = [] # List[str] |  (optional) (default to [])
    is_active = [true] # List[bool] |  (optional) (default to [true])
    parent_ref_list_id = [] # List[str] |  (optional) (default to [])
    sublevel = [] # List[int] |  (optional) (default to [])
    class_ref_list_id = [] # List[Optional[str]] |  (optional) (default to [])
    company_name = [] # List[Optional[str]] |  (optional) (default to [])
    type = [] # List[EntityType] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    minimal = True # bool |  (optional)

    try:
        # Read Entities
        api_response = api_instance.read_entities_entities_get(skip=skip, limit=limit, list_id=list_id, name=name, full_name=full_name, is_active=is_active, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, class_ref_list_id=class_ref_list_id, company_name=company_name, type=type, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, minimal=minimal)
        print("The response of EntitiesApi->read_entities_entities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->read_entities_entities_get: %s\n" % e)
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
 **class_ref_list_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **company_name** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **type** | [**List[EntityType]**](EntityType.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **minimal** | **bool**|  | [optional] 

### Return type

[**List[ReadEntitiesEntitiesGet200ResponseInner]**](ReadEntitiesEntitiesGet200ResponseInner.md)

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

# **read_entity_entities_list_id_get**
> ClassCodeRead read_entity_entities_list_id_get(list_id)

Read Entity

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
    api_instance = finops_client.EntitiesApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Read Entity
        api_response = api_instance.read_entity_entities_list_id_get(list_id)
        print("The response of EntitiesApi->read_entity_entities_list_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->read_entity_entities_list_id_get: %s\n" % e)
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

# **update_entities_entities_patch**
> List[EntityBase] update_entities_entities_patch(entity_update)

Update Entities

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.entity_base import EntityBase
from finops_client.models.entity_update import EntityUpdate
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
    api_instance = finops_client.EntitiesApi(api_client)
    entity_update = [finops_client.EntityUpdate()] # List[EntityUpdate] | 

    try:
        # Update Entities
        api_response = api_instance.update_entities_entities_patch(entity_update)
        print("The response of EntitiesApi->update_entities_entities_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitiesApi->update_entities_entities_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_update** | [**List[EntityUpdate]**](EntityUpdate.md)|  | 

### Return type

[**List[EntityBase]**](EntityBase.md)

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

