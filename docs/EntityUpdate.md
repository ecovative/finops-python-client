# EntityUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | 
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
from finops_client.models.entity_update import EntityUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityUpdate from a JSON string
entity_update_instance = EntityUpdate.from_json(json)
# print the JSON string representation of the object
print(EntityUpdate.to_json())

# convert the object into a dict
entity_update_dict = entity_update_instance.to_dict()
# create an instance of EntityUpdate from a dict
entity_update_from_dict = EntityUpdate.from_dict(entity_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


