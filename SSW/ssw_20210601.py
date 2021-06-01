# API (Application Programming Interface) - https://terms.naver.com/entry.naver?docId=815224&cid=42344&categoryId=42344
# ssw_20210601_API.html 파일 참조

# import json

# json_string = '''{
#     "name": "홍길동",
#     "gender": "남성",
#     "age": 50
# }'''

# json_object = json.loads(json_string)

# print(json_object)
# print(type(json_object))

# print(json_object.get('name'))
# print(json_object.get('gender'))
# print(json_object.get('age'))
# print(json_object.get('email', '?'))

# print(json_object['name'])
# print(json_object['gender'])
# print(json_object['age'])
# # print(json_object['email'])

# print('-' * 20)

# json_object = {
#     "name": "홍길동",
#     "gender": "남성",
#     "age": 50
# }

# json_string = json.dumps(json_object, indent=4, ensure_ascii=False)

# print(json_string)
# print(type(json_string))


import os
import sys
import requests
import mytoken
import json


def celebrity(img):
    client_id = mytoken.client_id
    client_secret = mytoken.client_secret
    # url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식
    files = {'image': open(img, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        # print (response.text)
        json_string = response.text
        json_object = json.loads(json_string)
        faces = json_object.get('faces')
        # print(faces)
        for face in faces:
            # print(face['celebrity'])
            name = face['celebrity']['value']
            conf = face['celebrity']['confidence']
            print(name, conf)
        # [퀴즈] json 모듈을 이용하여 아래와 같이 출력해보세요.
        '''
        닮은꼴: 홍길동
        신뢰도: 23.5%
        '''
    else:
        print("Error Code:" + rescode)

# celebrity('face1.jpg')
# celebrity('face2.jpg')
# celebrity('face3.jpg')

def face(img):
    client_id = mytoken.client_id
    client_secret = mytoken.client_secret
    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    files = {'image': open(img, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
        # 퀴즈: json 모듈을 이용하여 다음과 같이 출력해보세요.
        '''
        성별: 남
        나이: 20~25
        감정: 화남
        '''
    else:
        print("Error Code:" + rescode)

face('face1.jpg')
