# finops_client.AccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_accounts_accounts_post**](AccountsApi.md#create_accounts_accounts_post) | **POST** /accounts/ | Create Accounts
[**delete_accounts_accounts_delete_post**](AccountsApi.md#delete_accounts_accounts_delete_post) | **POST** /accounts/delete/ | Delete Accounts
[**read_account_accounts_list_id_get**](AccountsApi.md#read_account_accounts_list_id_get) | **GET** /accounts/{ListID}/ | Read Account
[**read_accounts_accounts_get**](AccountsApi.md#read_accounts_accounts_get) | **GET** /accounts/ | Read Accounts
[**update_accounts_accounts_patch**](AccountsApi.md#update_accounts_accounts_patch) | **PATCH** /accounts/ | Update Accounts


# **create_accounts_accounts_post**
> List[AccountBase] create_accounts_accounts_post(account_update)

Create Accounts

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.account_base import AccountBase
from finops_client.models.account_update import AccountUpdate
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
    api_instance = finops_client.AccountsApi(api_client)
    account_update = [finops_client.AccountUpdate()] # List[AccountUpdate] | 

    try:
        # Create Accounts
        api_response = api_instance.create_accounts_accounts_post(account_update)
        print("The response of AccountsApi->create_accounts_accounts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_accounts_accounts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_update** | [**List[AccountUpdate]**](AccountUpdate.md)|  | 

### Return type

[**List[AccountBase]**](AccountBase.md)

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

# **delete_accounts_accounts_delete_post**
> List[AccountBase] delete_accounts_accounts_delete_post(request_body, tags=tags)

Delete Accounts

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.account_base import AccountBase
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
    api_instance = finops_client.AccountsApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 
    tags = None # object |  (optional)

    try:
        # Delete Accounts
        api_response = api_instance.delete_accounts_accounts_delete_post(request_body, tags=tags)
        print("The response of AccountsApi->delete_accounts_accounts_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_accounts_accounts_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 
 **tags** | [**object**](.md)|  | [optional] 

### Return type

[**List[AccountBase]**](AccountBase.md)

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

# **read_account_accounts_list_id_get**
> AccountRead read_account_accounts_list_id_get(list_id)

Read Account

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.account_read import AccountRead
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
    api_instance = finops_client.AccountsApi(api_client)
    list_id = 'list_id_example' # str | 

    try:
        # Read Account
        api_response = api_instance.read_account_accounts_list_id_get(list_id)
        print("The response of AccountsApi->read_account_accounts_list_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->read_account_accounts_list_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**|  | 

### Return type

[**AccountRead**](AccountRead.md)

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

# **read_accounts_accounts_get**
> List[ReadAccountsAccountsGet200ResponseInner] read_accounts_accounts_get(skip=skip, limit=limit, list_id=list_id, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, account_type=account_type, name=name, full_name=full_name, source=source, statement_level=statement_level, is_active=is_active, is_intercompany=is_intercompany, default_currency=default_currency, cash_flow_classification=cash_flow_classification, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber, minimal=minimal)

Read Accounts

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.cash_flow_classification import CashFlowClassification
from finops_client.models.read_accounts_accounts_get200_response_inner import ReadAccountsAccountsGet200ResponseInner
from finops_client.models.statement_level import StatementLevel
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
    api_instance = finops_client.AccountsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    list_id = [] # List[str] |  (optional) (default to [])
    parent_ref_list_id = [] # List[Optional[str]] |  (optional) (default to [])
    sublevel = [] # List[int] |  (optional) (default to [])
    account_type = [] # List[TypeOfAccount] |  (optional) (default to [])
    name = [] # List[Optional[str]] |  (optional) (default to [])
    full_name = [] # List[Optional[str]] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    statement_level = [] # List[StatementLevel] |  (optional) (default to [])
    is_active = [true] # List[bool] |  (optional) (default to [true])
    is_intercompany = [] # List[Optional[bool]] |  (optional) (default to [])
    default_currency = [] # List[Optional[str]] |  (optional) (default to [])
    cash_flow_classification = [] # List[CashFlowClassification] |  (optional) (default to [])
    db_created_by = [] # List[Optional[str]] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    subscriber = 'subscriber_example' # str |  (optional)
    minimal = True # bool |  (optional)

    try:
        # Read Accounts
        api_response = api_instance.read_accounts_accounts_get(skip=skip, limit=limit, list_id=list_id, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, account_type=account_type, name=name, full_name=full_name, source=source, statement_level=statement_level, is_active=is_active, is_intercompany=is_intercompany, default_currency=default_currency, cash_flow_classification=cash_flow_classification, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber, minimal=minimal)
        print("The response of AccountsApi->read_accounts_accounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->read_accounts_accounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **parent_ref_list_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **sublevel** | [**List[int]**](int.md)|  | [optional] [default to []]
 **account_type** | [**List[TypeOfAccount]**](TypeOfAccount.md)|  | [optional] [default to []]
 **name** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **full_name** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **statement_level** | [**List[StatementLevel]**](StatementLevel.md)|  | [optional] [default to []]
 **is_active** | [**List[bool]**](bool.md)|  | [optional] [default to [true]]
 **is_intercompany** | [**List[Optional[bool]]**](bool.md)|  | [optional] [default to []]
 **default_currency** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **cash_flow_classification** | [**List[CashFlowClassification]**](CashFlowClassification.md)|  | [optional] [default to []]
 **db_created_by** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **subscriber** | **str**|  | [optional] 
 **minimal** | **bool**|  | [optional] 

### Return type

[**List[ReadAccountsAccountsGet200ResponseInner]**](ReadAccountsAccountsGet200ResponseInner.md)

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

# **update_accounts_accounts_patch**
> List[AccountBase] update_accounts_accounts_patch(account_update)

Update Accounts

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.account_base import AccountBase
from finops_client.models.account_update import AccountUpdate
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
    api_instance = finops_client.AccountsApi(api_client)
    account_update = [finops_client.AccountUpdate()] # List[AccountUpdate] | 

    try:
        # Update Accounts
        api_response = api_instance.update_accounts_accounts_patch(account_update)
        print("The response of AccountsApi->update_accounts_accounts_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_accounts_accounts_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_update** | [**List[AccountUpdate]**](AccountUpdate.md)|  | 

### Return type

[**List[AccountBase]**](AccountBase.md)

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

