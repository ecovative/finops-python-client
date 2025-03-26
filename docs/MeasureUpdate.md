# MeasureUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measure_id** | **int** |  | 
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
from finops_client.models.measure_update import MeasureUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureUpdate from a JSON string
measure_update_instance = MeasureUpdate.from_json(json)
# print the JSON string representation of the object
print(MeasureUpdate.to_json())

# convert the object into a dict
measure_update_dict = measure_update_instance.to_dict()
# create an instance of MeasureUpdate from a dict
measure_update_from_dict = MeasureUpdate.from_dict(measure_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


