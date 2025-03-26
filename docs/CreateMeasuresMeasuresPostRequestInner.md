# CreateMeasuresMeasuresPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measure_id** | **int** |  | 
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
from finops_client.models.create_measures_measures_post_request_inner import CreateMeasuresMeasuresPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMeasuresMeasuresPostRequestInner from a JSON string
create_measures_measures_post_request_inner_instance = CreateMeasuresMeasuresPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(CreateMeasuresMeasuresPostRequestInner.to_json())

# convert the object into a dict
create_measures_measures_post_request_inner_dict = create_measures_measures_post_request_inner_instance.to_dict()
# create an instance of CreateMeasuresMeasuresPostRequestInner from a dict
create_measures_measures_post_request_inner_from_dict = CreateMeasuresMeasuresPostRequestInner.from_dict(create_measures_measures_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


