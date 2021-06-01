# Day14-0601.py

import json

json_string = '''{
    "name": "홍길동",
    "gender": "남성",
    "age": 50,
    "data": {"k1":"v1", "k2":"v2", "k3":"v3"}
}'''

json_object = json.loads(json_string)

print(json_object.get('name'))
print(json_object.get('gender'))
print(json_object.get('age'))
print(json_object.get('data').get('k5'))
print(json_object.get('data').get('k1'))

json_object = {
    "name": "홍길동",
    "gender": "남성",
    "age": 50
}

json_string = json.dumps(json_object, indent=4, ensure_ascii=False)
print(json_string)