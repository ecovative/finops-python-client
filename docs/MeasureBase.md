# MeasureBase


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

## Example

```python
from finops_client.models.measure_base import MeasureBase

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureBase from a JSON string
measure_base_instance = MeasureBase.from_json(json)
# print the JSON string representation of the object
print(MeasureBase.to_json())

# convert the object into a dict
measure_base_dict = measure_base_instance.to_dict()
# create an instance of MeasureBase from a dict
measure_base_from_dict = MeasureBase.from_dict(measure_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


