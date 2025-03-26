# PeriodAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**AccountingSource**](AccountingSource.md) |  | 
**account_type** | [**TypeOfAccount**](TypeOfAccount.md) |  | 
**class_full_name** | **str** |  | [optional] 
**account_full_name** | **str** |  | 
**period** | **str** |  | 
**total_amount** | **float** |  | 

## Example

```python
from finops_client.models.period_amount import PeriodAmount

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodAmount from a JSON string
period_amount_instance = PeriodAmount.from_json(json)
# print the JSON string representation of the object
print(PeriodAmount.to_json())

# convert the object into a dict
period_amount_dict = period_amount_instance.to_dict()
# create an instance of PeriodAmount from a dict
period_amount_from_dict = PeriodAmount.from_dict(period_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


