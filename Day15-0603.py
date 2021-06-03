
d = {
    "info": {
        "name": "홍길동",
        "age": 19,
        "gender": "남"
    },
    "data": [
        {
            "kor": 100,
            "eng": 85,
            "math": 90
        },
        {
            "kor": 100,
            "eng": 90,
            "math": 95
        },
        {
            "kor": 100,
            "eng": 95,
            "math": 100
        },
    ]
}

info = d.get('info')
for key in info.keys():
    print(key, ':', info.get(key))

point = {}

data = d.get('data')
for i in range(len(data)):
    print('=== %d ===' %(i+1))
    
    for key in data[i].keys():
        print(key, ':', data[i].get(key))
        
        if point.get(key,None) == None:
            point[key] = '0'
        
        sum = int(point.get(key)) + int(data[i].get(key))
        point[key] = str(sum)

print('=== AVG ===')
for key in point.keys():
    print(key, ':', int(point.get(key)) / len(data))
        

