# finops_client.MeasuresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_measures_measures_post**](MeasuresApi.md#create_measures_measures_post) | **POST** /measures/ | Create Measures
[**delete_measures_measures_delete_post**](MeasuresApi.md#delete_measures_measures_delete_post) | **POST** /measures/delete/ | Delete Measures
[**read_measure_measures_measure_id_get**](MeasuresApi.md#read_measure_measures_measure_id_get) | **GET** /measures/{MeasureID}/ | Read Measure
[**read_measures_measures_get**](MeasuresApi.md#read_measures_measures_get) | **GET** /measures/ | Read Measures
[**update_measures_measures_patch**](MeasuresApi.md#update_measures_measures_patch) | **PATCH** /measures/ | Update Measures


# **create_measures_measures_post**
> List[int] create_measures_measures_post(create_measures_measures_post_request_inner)

Create Measures

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.create_measures_measures_post_request_inner import CreateMeasuresMeasuresPostRequestInner
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
    api_instance = finops_client.MeasuresApi(api_client)
    create_measures_measures_post_request_inner = [finops_client.CreateMeasuresMeasuresPostRequestInner()] # List[CreateMeasuresMeasuresPostRequestInner] | 

    try:
        # Create Measures
        api_response = api_instance.create_measures_measures_post(create_measures_measures_post_request_inner)
        print("The response of MeasuresApi->create_measures_measures_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasuresApi->create_measures_measures_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_measures_measures_post_request_inner** | [**List[CreateMeasuresMeasuresPostRequestInner]**](CreateMeasuresMeasuresPostRequestInner.md)|  | 

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

# **delete_measures_measures_delete_post**
> List[MeasureBase] delete_measures_measures_delete_post(request_body)

Delete Measures

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.measure_base import MeasureBase
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
    api_instance = finops_client.MeasuresApi(api_client)
    request_body = [56] # List[int] | 

    try:
        # Delete Measures
        api_response = api_instance.delete_measures_measures_delete_post(request_body)
        print("The response of MeasuresApi->delete_measures_measures_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasuresApi->delete_measures_measures_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

[**List[MeasureBase]**](MeasureBase.md)

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

# **read_measure_measures_measure_id_get**
> MeasureRead read_measure_measures_measure_id_get(measure_id)

Read Measure

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.measure_read import MeasureRead
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
    api_instance = finops_client.MeasuresApi(api_client)
    measure_id = 56 # int | 

    try:
        # Read Measure
        api_response = api_instance.read_measure_measures_measure_id_get(measure_id)
        print("The response of MeasuresApi->read_measure_measures_measure_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasuresApi->read_measure_measures_measure_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_id** | **int**|  | 

### Return type

[**MeasureRead**](MeasureRead.md)

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

# **read_measures_measures_get**
> List[MeasureBase] read_measures_measures_get(skip=skip, limit=limit, measure_id=measure_id, account_ref_list_id=account_ref_list_id, class_ref_list_id=class_ref_list_id, period=period, measure_type=measure_type, currency=currency, amount=amount, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber, latest=latest, as_of=as_of)

Read Measures

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.measure_base import MeasureBase
from finops_client.models.measure_type import MeasureType
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
    api_instance = finops_client.MeasuresApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    measure_id = [] # List[int] |  (optional) (default to [])
    account_ref_list_id = [] # List[Optional[str]] |  (optional) (default to [])
    class_ref_list_id = [] # List[str] |  (optional) (default to [])
    period = [] # List[Optional[str]] |  (optional) (default to [])
    measure_type = [] # List[MeasureType] |  (optional) (default to [])
    currency = [] # List[Optional[str]] |  (optional) (default to [])
    amount = [] # List[float] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    subscriber = 'subscriber_example' # str |  (optional)
    latest = True # bool |  (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Read Measures
        api_response = api_instance.read_measures_measures_get(skip=skip, limit=limit, measure_id=measure_id, account_ref_list_id=account_ref_list_id, class_ref_list_id=class_ref_list_id, period=period, measure_type=measure_type, currency=currency, amount=amount, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber, latest=latest, as_of=as_of)
        print("The response of MeasuresApi->read_measures_measures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasuresApi->read_measures_measures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **measure_id** | [**List[int]**](int.md)|  | [optional] [default to []]
 **account_ref_list_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **class_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **period** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **measure_type** | [**List[MeasureType]**](MeasureType.md)|  | [optional] [default to []]
 **currency** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **amount** | [**List[float]**](float.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **subscriber** | **str**|  | [optional] 
 **latest** | **bool**|  | [optional] 
 **as_of** | **datetime**|  | [optional] 

### Return type

[**List[MeasureBase]**](MeasureBase.md)

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

# **update_measures_measures_patch**
> List[MeasureBase] update_measures_measures_patch(measure_update)

Update Measures

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.measure_base import MeasureBase
from finops_client.models.measure_update import MeasureUpdate
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
    api_instance = finops_client.MeasuresApi(api_client)
    measure_update = [finops_client.MeasureUpdate()] # List[MeasureUpdate] | 

    try:
        # Update Measures
        api_response = api_instance.update_measures_measures_patch(measure_update)
        print("The response of MeasuresApi->update_measures_measures_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeasuresApi->update_measures_measures_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_update** | [**List[MeasureUpdate]**](MeasureUpdate.md)|  | 

### Return type

[**List[MeasureBase]**](MeasureBase.md)

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

