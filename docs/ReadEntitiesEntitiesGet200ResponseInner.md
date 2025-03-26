# ReadEntitiesEntitiesGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | 
**time_modified** | **datetime** |  | 
**edit_sequence** | **int** |  | 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**parent_ref_list_id** | **str** |  | [optional] 
**sublevel** | **int** |  | [optional] 
**class_ref_list_id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**type** | [**EntityType**](EntityType.md) |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.read_entities_entities_get200_response_inner import ReadEntitiesEntitiesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadEntitiesEntitiesGet200ResponseInner from a JSON string
read_entities_entities_get200_response_inner_instance = ReadEntitiesEntitiesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ReadEntitiesEntitiesGet200ResponseInner.to_json())

# convert the object into a dict
read_entities_entities_get200_response_inner_dict = read_entities_entities_get200_response_inner_instance.to_dict()
# create an instance of ReadEntitiesEntitiesGet200ResponseInner from a dict
read_entities_entities_get200_response_inner_from_dict = ReadEntitiesEntitiesGet200ResponseInner.from_dict(read_entities_entities_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


