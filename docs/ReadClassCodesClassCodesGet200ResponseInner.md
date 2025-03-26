# ReadClassCodesClassCodesGet200ResponseInner


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
**parent_ref_full_name** | **str** |  | [optional] 
**sublevel** | **int** |  | [optional] 
**time_created** | **datetime** |  | [optional] 
**source** | [**AccountingSource**](AccountingSource.md) |  | [optional] 
**db_created_by** | **str** |  | [optional] 
**db_time_created** | **datetime** |  | [optional] 
**db_time_modified** | **datetime** |  | [optional] 

## Example

```python
from finops_client.models.read_class_codes_class_codes_get200_response_inner import ReadClassCodesClassCodesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadClassCodesClassCodesGet200ResponseInner from a JSON string
read_class_codes_class_codes_get200_response_inner_instance = ReadClassCodesClassCodesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ReadClassCodesClassCodesGet200ResponseInner.to_json())

# convert the object into a dict
read_class_codes_class_codes_get200_response_inner_dict = read_class_codes_class_codes_get200_response_inner_instance.to_dict()
# create an instance of ReadClassCodesClassCodesGet200ResponseInner from a dict
read_class_codes_class_codes_get200_response_inner_from_dict = ReadClassCodesClassCodesGet200ResponseInner.from_dict(read_class_codes_class_codes_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


