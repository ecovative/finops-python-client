# finops_client.ReportsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get**](ReportsApi.md#get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get) | **GET** /reports/get_actuals_by_class_and_account/ | Get Actuals By Class And Account


# **get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get**
> List[PeriodAmount] get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get(period_str=period_str, start_date=start_date, end_date=end_date, class_full_name=class_full_name, account_full_name=account_full_name, account_type=account_type, source=source, account_list=account_list, classcode_list=classcode_list, skip=skip, limit=limit)

Get Actuals By Class And Account

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.period_amount import PeriodAmount
from finops_client.models.type_of_account import TypeOfAccount
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
    api_instance = finops_client.ReportsApi(api_client)
    period_str = 'period_str_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    class_full_name = 'class_full_name_example' # str |  (optional)
    account_full_name = 'account_full_name_example' # str |  (optional)
    account_type = [] # List[TypeOfAccount] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    account_list = [] # List[Optional[str]] |  (optional) (default to [])
    classcode_list = [] # List[Optional[str]] |  (optional) (default to [])
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)

    try:
        # Get Actuals By Class And Account
        api_response = api_instance.get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get(period_str=period_str, start_date=start_date, end_date=end_date, class_full_name=class_full_name, account_full_name=account_full_name, account_type=account_type, source=source, account_list=account_list, classcode_list=classcode_list, skip=skip, limit=limit)
        print("The response of ReportsApi->get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_actuals_by_class_and_account_reports_get_actuals_by_class_and_account_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_str** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **class_full_name** | **str**|  | [optional] 
 **account_full_name** | **str**|  | [optional] 
 **account_type** | [**List[TypeOfAccount]**](TypeOfAccount.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **account_list** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **classcode_list** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 

### Return type

[**List[PeriodAmount]**](PeriodAmount.md)

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

