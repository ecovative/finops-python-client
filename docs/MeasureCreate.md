# MeasureCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measure_id** | **int** |  | [optional] 
**account_ref_list_id** | **str** |  | 
**class_ref_list_id** | **str** |  | [optional] 
**period** | **str** |  | 
**measure_type** | [**MeasureType**](MeasureType.md) |  | 
**currency** | **str** |  | 
**amount** | **float** |  | 
**source** | [**AccountingSource**](AccountingSource.md) |  | 
**db_created_by** | **str** |  | 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.measure_create import MeasureCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureCreate from a JSON string
measure_create_instance = MeasureCreate.from_json(json)
# print the JSON string representation of the object
print(MeasureCreate.to_json())

# convert the object into a dict
measure_create_dict = measure_create_instance.to_dict()
# create an instance of MeasureCreate from a dict
measure_create_from_dict = MeasureCreate.from_dict(measure_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


