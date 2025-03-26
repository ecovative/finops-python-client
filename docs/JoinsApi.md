# finops_client.JoinsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_accounts_with_measures_join_accounts_with_measures_get**](JoinsApi.md#read_accounts_with_measures_join_accounts_with_measures_get) | **GET** /join/accounts_with_measures/ | Read Accounts With Measures
[**read_transactions_with_accounts_join_transactions_with_accounts_get**](JoinsApi.md#read_transactions_with_accounts_join_transactions_with_accounts_get) | **GET** /join/transactions_with_accounts/ | Read Transactions With Accounts


# **read_accounts_with_measures_join_accounts_with_measures_get**
> List[AccountWithMeasures] read_accounts_with_measures_join_accounts_with_measures_get(skip=skip, limit=limit, measure_id=measure_id, account_type=account_type, account_ref_list_id=account_ref_list_id, name=name, full_name=full_name, is_active=is_active, is_intercompany=is_intercompany, class_ref_list_id=class_ref_list_id, period=period, measure_type=measure_type, currency=currency, amount=amount, source=source, db_created_by=db_created_by, latest=latest, as_of=as_of, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber)

Read Accounts With Measures

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.account_with_measures import AccountWithMeasures
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.measure_type import MeasureType
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
    api_instance = finops_client.JoinsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    measure_id = [] # List[int] |  (optional) (default to [])
    account_type = [] # List[TypeOfAccount] |  (optional) (default to [])
    account_ref_list_id = [] # List[str] |  (optional) (default to [])
    name = [] # List[str] |  (optional) (default to [])
    full_name = [] # List[str] |  (optional) (default to [])
    is_active = [true] # List[bool] |  (optional) (default to [true])
    is_intercompany = [] # List[bool] |  (optional) (default to [])
    class_ref_list_id = [] # List[str] |  (optional) (default to [])
    period = [] # List[str] |  (optional) (default to [])
    measure_type = [] # List[MeasureType] |  (optional) (default to [])
    currency = [] # List[str] |  (optional) (default to [])
    amount = [] # List[float] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    latest = True # bool |  (optional)
    as_of = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    subscriber = 'subscriber_example' # str |  (optional)

    try:
        # Read Accounts With Measures
        api_response = api_instance.read_accounts_with_measures_join_accounts_with_measures_get(skip=skip, limit=limit, measure_id=measure_id, account_type=account_type, account_ref_list_id=account_ref_list_id, name=name, full_name=full_name, is_active=is_active, is_intercompany=is_intercompany, class_ref_list_id=class_ref_list_id, period=period, measure_type=measure_type, currency=currency, amount=amount, source=source, db_created_by=db_created_by, latest=latest, as_of=as_of, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber)
        print("The response of JoinsApi->read_accounts_with_measures_join_accounts_with_measures_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JoinsApi->read_accounts_with_measures_join_accounts_with_measures_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **measure_id** | [**List[int]**](int.md)|  | [optional] [default to []]
 **account_type** | [**List[TypeOfAccount]**](TypeOfAccount.md)|  | [optional] [default to []]
 **account_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **full_name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **is_active** | [**List[bool]**](bool.md)|  | [optional] [default to [true]]
 **is_intercompany** | [**List[bool]**](bool.md)|  | [optional] [default to []]
 **class_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **period** | [**List[str]**](str.md)|  | [optional] [default to []]
 **measure_type** | [**List[MeasureType]**](MeasureType.md)|  | [optional] [default to []]
 **currency** | [**List[str]**](str.md)|  | [optional] [default to []]
 **amount** | [**List[float]**](float.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **latest** | **bool**|  | [optional] 
 **as_of** | **datetime**|  | [optional] 
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **subscriber** | **str**|  | [optional] 

### Return type

[**List[AccountWithMeasures]**](AccountWithMeasures.md)

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

# **read_transactions_with_accounts_join_transactions_with_accounts_get**
> List[TransactionWithAccounts] read_transactions_with_accounts_join_transactions_with_accounts_get(skip=skip, limit=limit, fq_primary_key=fq_primary_key, txn_type=txn_type, txn_id=txn_id, txn_line_id=txn_line_id, entity_ref_list_id=entity_ref_list_id, entity_ref_full_name=entity_ref_full_name, txn_date=txn_date, account_ref_list_id=account_ref_list_id, account_ref_full_name=account_ref_full_name, class_ref_list_id=class_ref_list_id, class_ref_full_name=class_ref_full_name, ref_number=ref_number, amount=amount, memo=memo, fq_txn_link_key=fq_txn_link_key, fq_journal_entry_link_key=fq_journal_entry_link_key, source=source, list_id=list_id, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, account_type=account_type, name=name, full_name=full_name, statement_level=statement_level, is_active=is_active, is_intercompany=is_intercompany, default_currency=default_currency, cash_flow_classification=cash_flow_classification, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber)

Read Transactions With Accounts

### Example

* Api Key Authentication (APIKeyHeader):

```python
import finops_client
from finops_client.models.accounting_source import AccountingSource
from finops_client.models.cash_flow_classification import CashFlowClassification
from finops_client.models.statement_level import StatementLevel
from finops_client.models.transaction_with_accounts import TransactionWithAccounts
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
    api_instance = finops_client.JoinsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 56 # int |  (optional)
    fq_primary_key = [] # List[Optional[str]] |  (optional) (default to [])
    txn_type = [] # List[Optional[str]] |  (optional) (default to [])
    txn_id = [] # List[Optional[str]] |  (optional) (default to [])
    txn_line_id = [] # List[Optional[str]] |  (optional) (default to [])
    entity_ref_list_id = [] # List[Optional[str]] |  (optional) (default to [])
    entity_ref_full_name = [] # List[Optional[str]] |  (optional) (default to [])
    txn_date = [] # List[Optional[datetime]] |  (optional) (default to [])
    account_ref_list_id = [] # List[str] |  (optional) (default to [])
    account_ref_full_name = [] # List[Optional[str]] |  (optional) (default to [])
    class_ref_list_id = [] # List[str] |  (optional) (default to [])
    class_ref_full_name = [] # List[Optional[str]] |  (optional) (default to [])
    ref_number = [] # List[Optional[str]] |  (optional) (default to [])
    amount = [] # List[float] |  (optional) (default to [])
    memo = [] # List[Optional[str]] |  (optional) (default to [])
    fq_txn_link_key = [] # List[Optional[str]] |  (optional) (default to [])
    fq_journal_entry_link_key = [] # List[Optional[str]] |  (optional) (default to [])
    source = [] # List[AccountingSource] |  (optional) (default to [])
    list_id = [] # List[str] |  (optional) (default to [])
    parent_ref_list_id = [] # List[str] |  (optional) (default to [])
    sublevel = [] # List[int] |  (optional) (default to [])
    account_type = [] # List[TypeOfAccount] |  (optional) (default to [])
    name = [] # List[str] |  (optional) (default to [])
    full_name = [] # List[str] |  (optional) (default to [])
    statement_level = [] # List[StatementLevel] |  (optional) (default to [])
    is_active = [true] # List[bool] |  (optional) (default to [true])
    is_intercompany = [] # List[bool] |  (optional) (default to [])
    default_currency = [] # List[str] |  (optional) (default to [])
    cash_flow_classification = [] # List[CashFlowClassification] |  (optional) (default to [])
    db_created_by = [] # List[str] |  (optional) (default to [])
    date_field = 'date_field_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    subscriber = 'subscriber_example' # str |  (optional)

    try:
        # Read Transactions With Accounts
        api_response = api_instance.read_transactions_with_accounts_join_transactions_with_accounts_get(skip=skip, limit=limit, fq_primary_key=fq_primary_key, txn_type=txn_type, txn_id=txn_id, txn_line_id=txn_line_id, entity_ref_list_id=entity_ref_list_id, entity_ref_full_name=entity_ref_full_name, txn_date=txn_date, account_ref_list_id=account_ref_list_id, account_ref_full_name=account_ref_full_name, class_ref_list_id=class_ref_list_id, class_ref_full_name=class_ref_full_name, ref_number=ref_number, amount=amount, memo=memo, fq_txn_link_key=fq_txn_link_key, fq_journal_entry_link_key=fq_journal_entry_link_key, source=source, list_id=list_id, parent_ref_list_id=parent_ref_list_id, sublevel=sublevel, account_type=account_type, name=name, full_name=full_name, statement_level=statement_level, is_active=is_active, is_intercompany=is_intercompany, default_currency=default_currency, cash_flow_classification=cash_flow_classification, db_created_by=db_created_by, date_field=date_field, start_date=start_date, end_date=end_date, subscriber=subscriber)
        print("The response of JoinsApi->read_transactions_with_accounts_join_transactions_with_accounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JoinsApi->read_transactions_with_accounts_join_transactions_with_accounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] 
 **fq_primary_key** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **txn_type** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **txn_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **txn_line_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **entity_ref_list_id** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **entity_ref_full_name** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **txn_date** | [**List[Optional[datetime]]**](datetime.md)|  | [optional] [default to []]
 **account_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **account_ref_full_name** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **class_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **class_ref_full_name** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **ref_number** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **amount** | [**List[float]**](float.md)|  | [optional] [default to []]
 **memo** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **fq_txn_link_key** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **fq_journal_entry_link_key** | [**List[Optional[str]]**](str.md)|  | [optional] [default to []]
 **source** | [**List[AccountingSource]**](AccountingSource.md)|  | [optional] [default to []]
 **list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **parent_ref_list_id** | [**List[str]**](str.md)|  | [optional] [default to []]
 **sublevel** | [**List[int]**](int.md)|  | [optional] [default to []]
 **account_type** | [**List[TypeOfAccount]**](TypeOfAccount.md)|  | [optional] [default to []]
 **name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **full_name** | [**List[str]**](str.md)|  | [optional] [default to []]
 **statement_level** | [**List[StatementLevel]**](StatementLevel.md)|  | [optional] [default to []]
 **is_active** | [**List[bool]**](bool.md)|  | [optional] [default to [true]]
 **is_intercompany** | [**List[bool]**](bool.md)|  | [optional] [default to []]
 **default_currency** | [**List[str]**](str.md)|  | [optional] [default to []]
 **cash_flow_classification** | [**List[CashFlowClassification]**](CashFlowClassification.md)|  | [optional] [default to []]
 **db_created_by** | [**List[str]**](str.md)|  | [optional] [default to []]
 **date_field** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **subscriber** | **str**|  | [optional] 

### Return type

[**List[TransactionWithAccounts]**](TransactionWithAccounts.md)

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

