# finops_client.TransactionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transactions_transactions_post**](TransactionsApi.md#create_transactions_transactions_post) | **POST** /transactions/ | Create Transactions
[**delete_transactions_transactions_delete_post**](TransactionsApi.md#delete_transactions_transactions_delete_post) | **POST** /transactions/delete/ | Delete Transactions
[**read_transaction_transactions_fq_txn_link_key_get**](TransactionsApi.md#read_transaction_transactions_fq_txn_link_key_get) | **GET** /transactions/{FQTxnLinkKey}/ | Read Transaction
[**read_transactions_transactions_get**](TransactionsApi.md#read_transactions_transactions_get) | **GET** /transactions/ | Read Transactions
[**update_transactions_transactions_patch**](TransactionsApi.md#update_transactions_transactions_patch) | **PATCH** /transactions/ | Update Transactions


# **create_transactions_transactions_post**
> List[Optional[str]] create_transactions_transactions_post(transaction_update)

Create Transactions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.transaction_update import TransactionUpdate
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
    api_instance = finops_client.TransactionsApi(api_client)
    transaction_update = [finops_client.TransactionUpdate()] # List[TransactionUpdate] | 

    try:
        # Create Transactions
        api_response = api_instance.create_transactions_transactions_post(transaction_update)
        print("The response of TransactionsApi->create_transactions_transactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_transactions_transactions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_update** | [**List[TransactionUpdate]**](TransactionUpdate.md)|  | 

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

# **delete_transactions_transactions_delete_post**
> List[TransactionBase] delete_transactions_transactions_delete_post(request_body)

Delete Transactions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.transaction_base import TransactionBase
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
    api_instance = finops_client.TransactionsApi(api_client)
    request_body = ['request_body_example'] # List[Optional[str]] | 

    try:
        # Delete Transactions
        api_response = api_instance.delete_transactions_transactions_delete_post(request_body)
        print("The response of TransactionsApi->delete_transactions_transactions_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transactions_transactions_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[Optional[str]]**](str.md)|  | 

### Return type

[**List[TransactionBase]**](TransactionBase.md)

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

# **read_transaction_transactions_fq_txn_link_key_get**
> TransactionRead read_transaction_transactions_fq_txn_link_key_get(fq_txn_link_key)

Read Transaction

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.transaction_read import TransactionRead
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
    api_instance = finops_client.TransactionsApi(api_client)
    fq_txn_link_key = 'fq_txn_link_key_example' # str | 

    try:
        # Read Transaction
        api_response = api_instance.read_transaction_transactions_fq_txn_link_key_get(fq_txn_link_key)
        print("The response of TransactionsApi->read_transaction_transactions_fq_txn_link_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->read_transaction_transactions_fq_txn_link_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fq_txn_link_key** | **str**|  | 

### Return type

[**TransactionRead**](TransactionRead.md)

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

# **read_transactions_transactions_get**
> List[ReadTransactionsTransactionsGet200ResponseInner] read_transactions_transactions_get(skip=skip, limit=limit, fq_primary_key=fq_primary_key, txn_type=txn_type, txn_id=txn_id, txn_line_id=txn_line_id, entity_ref_list_id=entity_ref_list_id, entity_ref_full_name=entity_ref_full_name, txn_date=txn_date, account_ref_list_id=account_ref_list_id, account_ref_full_name=account_ref_full_name, class_ref_list_id=class_ref_list_id, class_ref_full_name=class_ref_full_name, ref_number=ref_number, amount=amount, memo=memo, fq_txn_link_key=fq_txn_link_key, fq_journal_entry_link_key=fq_journal_entry_link_key, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber, minimal=minimal)

Read Transactions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.read_transactions_transactions_get200_response_inner import ReadTransactionsTransactionsGet200ResponseInner
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
    api_instance = finops_client.TransactionsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    fq_primary_key = [] # List[str] |  (optional) (default to [])
    txn_type = [] # List[str] |  (optional) (default to [])
    txn_id = [] # List[str] |  (optional) (default to [])
    txn_line_id = [] # List[str] |  (optional) (default to [])
    entity_ref_list_id = [] # List[str] |  (optional) (default to [])
    entity_ref_full_name = [] # List[str] |  (optional) (default to [])
    txn_date = [] # List[datetime] |  (optional) (default to [])
    account_ref_list_id = [] # List[str] |  (optional) (default to [])
    account_ref_full_name = [] # List[str] |  (optional) (default to [])
    class_ref_list_id = [] # List[str] |  (optional) (default to [])
    class_ref_full_name = [] # List[str] |  (optional) (default to [])
    ref_number = [] # List[str] |  (optional) (default to [])
    amount = [] # List[float] |  (optional) (default to [])
    memo = [] # List[str] |  (optional) (default to [])
    fq_txn_link_key = [] # List[str] |  (optional) (default to [])
    fq_journal_entry_link_key = [] # List[str] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    subscriber = 'subscriber_example' # str |  (optional)
    minimal = True # bool |  (optional)

    try:
        # Read Transactions
        api_response = api_instance.read_transactions_transactions_get(skip=skip, limit=limit, fq_primary_key=fq_primary_key, txn_type=txn_type, txn_id=txn_id, txn_line_id=txn_line_id, entity_ref_list_id=entity_ref_list_id, entity_ref_full_name=entity_ref_full_name, txn_date=txn_date, account_ref_list_id=account_ref_list_id, account_ref_full_name=account_ref_full_name, class_ref_list_id=class_ref_list_id, class_ref_full_name=class_ref_full_name, ref_number=ref_number, amount=amount, memo=memo, fq_txn_link_key=fq_txn_link_key, fq_journal_entry_link_key=fq_journal_entry_link_key, source=source, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber, minimal=minimal)
        print("The response of TransactionsApi->read_transactions_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->read_transactions_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **fq_primary_key** | [**List[str]**](str.md)|  | [optional] [default to []]
 **txn_type** | [**List[str]**](str.md)|  | [optional] [default to []]
 **txn_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **txn_line_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **entity_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **entity_ref_full_name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **txn_date** | [**List[datetime]**](datetime.md)|  | [optional] [default to []]
 **account_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **account_ref_full_name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **class_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **class_ref_full_name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **ref_number** | [**List[str]**](str.md)|  | [optional] [default to []]
 **amount** | [**List[float]**](float.md)|  | [optional] [default to []]
 **memo** | [**List[str]**](str.md)|  | [optional] [default to []]
 **fq_txn_link_key** | [**List[str]**](str.md)|  | [optional] [default to []]
 **fq_journal_entry_link_key** | [**List[str]**](str.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **subscriber** | **str**|  | [optional] 
 **minimal** | **bool**|  | [optional] 

### Return type

[**List[ReadTransactionsTransactionsGet200ResponseInner]**](ReadTransactionsTransactionsGet200ResponseInner.md)

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

# **update_transactions_transactions_patch**
> List[TransactionBase] update_transactions_transactions_patch(transaction_update)

Update Transactions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.transaction_base import TransactionBase
from finops_client.models.transaction_update import TransactionUpdate
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
    api_instance = finops_client.TransactionsApi(api_client)
    transaction_update = [finops_client.TransactionUpdate()] # List[TransactionUpdate] | 

    try:
        # Update Transactions
        api_response = api_instance.update_transactions_transactions_patch(transaction_update)
        print("The response of TransactionsApi->update_transactions_transactions_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transactions_transactions_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_update** | [**List[TransactionUpdate]**](TransactionUpdate.md)|  | 

### Return type

[**List[TransactionBase]**](TransactionBase.md)

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

