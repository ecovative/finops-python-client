# finops_client.ServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_orphan_txnlines_services_delete_orphan_txnlines_get**](ServicesApi.md#delete_orphan_txnlines_services_delete_orphan_txnlines_get) | **GET** /services/delete_orphan_txnlines/ | Delete Orphan Txnlines
[**get_cash_balance_services_cash_balance_get**](ServicesApi.md#get_cash_balance_services_cash_balance_get) | **GET** /services/cash_balance/ | Get Cash Balance
[**get_cash_consumption_services_get_cash_consumption_get**](ServicesApi.md#get_cash_consumption_services_get_cash_consumption_get) | **GET** /services/get_cash_consumption/ | Get Cash Consumption
[**refresh_actuals_services_refresh_actuals_get**](ServicesApi.md#refresh_actuals_services_refresh_actuals_get) | **GET** /services/refresh_actuals/ | Refresh Actuals
[**stage_estimates_to_actuals_services_stage_estimates_to_actuals_get**](ServicesApi.md#stage_estimates_to_actuals_services_stage_estimates_to_actuals_get) | **GET** /services/stage_estimates_to_actuals/ | Stage Estimates To Actuals
[**sync_transaction_references_services_sync_txn_references_post**](ServicesApi.md#sync_transaction_references_services_sync_txn_references_post) | **POST** /services/sync_txn_references/ | Sync Transaction References


# **delete_orphan_txnlines_services_delete_orphan_txnlines_get**
> object delete_orphan_txnlines_services_delete_orphan_txnlines_get()

Delete Orphan Txnlines

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
    api_instance = finops_client.ServicesApi(api_client)

    try:
        # Delete Orphan Txnlines
        api_response = api_instance.delete_orphan_txnlines_services_delete_orphan_txnlines_get()
        print("The response of ServicesApi->delete_orphan_txnlines_services_delete_orphan_txnlines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_orphan_txnlines_services_delete_orphan_txnlines_get: %s\n" % e)
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

# **get_cash_balance_services_cash_balance_get**
> object get_cash_balance_services_cash_balance_get(var_date, sources=sources, time_of_day=time_of_day)

Get Cash Balance

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
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
    api_instance = finops_client.ServicesApi(api_client)
    var_date = 'var_date_example' # str | 
    sources = [] # List[AccountingSource] |  (optional) (default to [])
    time_of_day = finops_client.TimeOfDay() # TimeOfDay |  (optional)

    try:
        # Get Cash Balance
        api_response = api_instance.get_cash_balance_services_cash_balance_get(var_date, sources=sources, time_of_day=time_of_day)
        print("The response of ServicesApi->get_cash_balance_services_cash_balance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_cash_balance_services_cash_balance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**|  | 
 **sources** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **time_of_day** | [**TimeOfDay**](.md)|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_consumption_services_get_cash_consumption_get**
> object get_cash_consumption_services_get_cash_consumption_get(period_str, sources=sources)

Get Cash Consumption

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.get_cash_consumption_services_get_cash_consumption_get_sources_parameter_inner import GetCashConsumptionServicesGetCashConsumptionGetSourcesParameterInner
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
    api_instance = finops_client.ServicesApi(api_client)
    period_str = 'period_str_example' # str | 
    sources = [finops_client.GetCashConsumptionServicesGetCashConsumptionGetSourcesParameterInner()] # List[GetCashConsumptionServicesGetCashConsumptionGetSourcesParameterInner] |  (optional)

    try:
        # Get Cash Consumption
        api_response = api_instance.get_cash_consumption_services_get_cash_consumption_get(period_str, sources=sources)
        print("The response of ServicesApi->get_cash_consumption_services_get_cash_consumption_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_cash_consumption_services_get_cash_consumption_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_str** | **str**|  | 
 **sources** | [**List[GetCashConsumptionServicesGetCashConsumptionGetSourcesParameterInner]**](GetCashConsumptionServicesGetCashConsumptionGetSourcesParameterInner.md)|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_actuals_services_refresh_actuals_get**
> object refresh_actuals_services_refresh_actuals_get()

Refresh Actuals

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
    api_instance = finops_client.ServicesApi(api_client)

    try:
        # Refresh Actuals
        api_response = api_instance.refresh_actuals_services_refresh_actuals_get()
        print("The response of ServicesApi->refresh_actuals_services_refresh_actuals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->refresh_actuals_services_refresh_actuals_get: %s\n" % e)
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

# **stage_estimates_to_actuals_services_stage_estimates_to_actuals_get**
> object stage_estimates_to_actuals_services_stage_estimates_to_actuals_get(source, period_start, period_end, skip=skip, limit=limit)

Stage Estimates To Actuals

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
    api_instance = finops_client.ServicesApi(api_client)
    source = finops_client.Source() # Source | 
    period_start = 'period_start_example' # str | 
    period_end = 'period_end_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)

    try:
        # Stage Estimates To Actuals
        api_response = api_instance.stage_estimates_to_actuals_services_stage_estimates_to_actuals_get(source, period_start, period_end, skip=skip, limit=limit)
        print("The response of ServicesApi->stage_estimates_to_actuals_services_stage_estimates_to_actuals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->stage_estimates_to_actuals_services_stage_estimates_to_actuals_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | [**Source**](.md)|  | 
 **period_start** | **str**|  | 
 **period_end** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_transaction_references_services_sync_txn_references_post**
> object sync_transaction_references_services_sync_txn_references_post()

Sync Transaction References

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
    api_instance = finops_client.ServicesApi(api_client)

    try:
        # Sync Transaction References
        api_response = api_instance.sync_transaction_references_services_sync_txn_references_post()
        print("The response of ServicesApi->sync_transaction_references_services_sync_txn_references_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->sync_transaction_references_services_sync_txn_references_post: %s\n" % e)
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

