# EntityMin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_id** | **str** |  | 
**time_modified** | **datetime** |  | 
**edit_sequence** | **int** |  | 

## Example

```python
from finops_client.models.entity_min import EntityMin

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMin from a JSON string
entity_min_instance = EntityMin.from_json(json)
# print the JSON string representation of the object
print(EntityMin.to_json())

# convert the object into a dict
entity_min_dict = entity_min_instance.to_dict()
# create an instance of EntityMin from a dict
entity_min_from_dict = EntityMin.from_dict(entity_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


