# ClassCodeUpdate


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
**parent_ref_full_name** | **str** |  | [optional] 
**sublevel** | **int** |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.class_code_update import ClassCodeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ClassCodeUpdate from a JSON string
class_code_update_instance = ClassCodeUpdate.from_json(json)
# print the JSON string representation of the object
print(ClassCodeUpdate.to_json())

# convert the object into a dict
class_code_update_dict = class_code_update_instance.to_dict()
# create an instance of ClassCodeUpdate from a dict
class_code_update_from_dict = ClassCodeUpdate.from_dict(class_code_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


