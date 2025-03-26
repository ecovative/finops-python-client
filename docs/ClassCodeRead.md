# ClassCodeRead


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
**parent_ref_full_name** | **str** |  | [optional] 
**sublevel** | **int** |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 
**parent_class_code** | [**ClassCodeBase**](ClassCodeBase.md) |  | [optional] 
**child_class_codes** | [**List[ClassCodeBase]**](ClassCodeBase.md) |  | [optional] 

## Example

```python
from finops_client.models.class_code_read import ClassCodeRead

# TODO update the JSON string below
json = "{}"
# create an instance of ClassCodeRead from a JSON string
class_code_read_instance = ClassCodeRead.from_json(json)
# print the JSON string representation of the object
print(ClassCodeRead.to_json())

# convert the object into a dict
class_code_read_dict = class_code_read_instance.to_dict()
# create an instance of ClassCodeRead from a dict
class_code_read_from_dict = ClassCodeRead.from_dict(class_code_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


