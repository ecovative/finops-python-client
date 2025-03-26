# EntityBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | [optional] 
**time_modified** | **datetime** |  | [optional] 
**edit_sequence** | **int** |  | [optional] 
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
from finops_client.models.entity_base import EntityBase

# TODO update the JSON string below
json = "{}"
# create an instance of EntityBase from a JSON string
entity_base_instance = EntityBase.from_json(json)
# print the JSON string representation of the object
print(EntityBase.to_json())

# convert the object into a dict
entity_base_dict = entity_base_instance.to_dict()
# create an instance of EntityBase from a dict
entity_base_from_dict = EntityBase.from_dict(entity_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


