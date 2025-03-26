# MeasureRead


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
**account** | [**AccountBase**](AccountBase.md) |  | [optional] 
**class_code** | [**ClassCodeBase**](ClassCodeBase.md) |  | [optional] 

## Example

```python
from finops_client.models.measure_read import MeasureRead

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureRead from a JSON string
measure_read_instance = MeasureRead.from_json(json)
# print the JSON string representation of the object
print(MeasureRead.to_json())

# convert the object into a dict
measure_read_dict = measure_read_instance.to_dict()
# create an instance of MeasureRead from a dict
measure_read_from_dict = MeasureRead.from_dict(measure_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


