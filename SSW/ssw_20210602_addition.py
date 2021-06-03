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
    
    faces = []
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
    else:
        print("Error Code:" + rescode)
    
    return faces

# celebrity('face1.jpg')
# celebrity('face2.jpg')
# celebrity('face3.jpg')

def face(img, celebrities=[]):
    client_id = mytoken.client_id
    client_secret = mytoken.client_secret
    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    files = {'image': open(img, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        # print (response.text)
        json_object = json.loads(response.text)
        faces = json_object.get('faces')
        cnt = 0
        for face in faces:
            name = celebrities[cnt]['celebrity']['value']
            gender = face['gender']['value']
            age = face['age']['value']
            emotion = face['emotion']['value']
            print(name, gender, age, emotion)
            cnt += 1
    else:
        print("Error Code:" + rescode)

# face('face1.jpg')
# face('face2.jpg')

def get_info(img):
    celebrities = celebrity(img)
    face(img, celebrities)

get_info('face2.jpg')
