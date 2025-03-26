# AccountWithMeasures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measure_id** | **int** |  | [optional] 
**account_ref_list_id** | **str** |  | [optional] 
**class_ref_list_id** | **str** |  | [optional] 
**period** | **str** |  | [optional] 
**measure_type** | [**MeasureType**](MeasureType.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 
**list_id** | **str** |  | [optional] 
**time_modified** | **datetime** |  | [optional] 
**edit_sequence** | **int** |  | [optional] 
**full_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**account_type** | [**TypeOfAccount**](TypeOfAccount.md) |  | [optional] 
**statement_level** | [**StatementLevel**](StatementLevel.md) |  | [optional] 
**default_currency** | **str** |  | [optional] 
**is_intercompany** | **bool** |  | [optional] 

## Example

```python
from finops_client.models.account_with_measures import AccountWithMeasures

# TODO update the JSON string below
json = "{}"
# create an instance of AccountWithMeasures from a JSON string
account_with_measures_instance = AccountWithMeasures.from_json(json)
# print the JSON string representation of the object
print(AccountWithMeasures.to_json())

# convert the object into a dict
account_with_measures_dict = account_with_measures_instance.to_dict()
# create an instance of AccountWithMeasures from a dict
account_with_measures_from_dict = AccountWithMeasures.from_dict(account_with_measures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


