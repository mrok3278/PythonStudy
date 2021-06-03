import os
import sys
import requests
import json
import Token
import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Resource/chromedriver.exe')

client_id = Token.NAVER_client_id
client_secret = Token.NAVER_client_secret

# url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

# for file in os.listdir('Resource/celeb'):
    
#     files = {'image': open(f'Resource/celeb/{file}', 'rb')}

#     headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
#     response = requests.post(url,  files=files, headers=headers)
#     rescode = response.status_code

#     if(rescode == 200):
#         json_response = json.loads(response.text)
        
#         print(json_response)
#         info =  json_response.get('info')
#         faces = json_response.get('faces')
        
#         for face in faces:
            
#             name = face.get('celebrity').get('value')
#             sUrl = f"https://www.google.com/search?q={name}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi5y8mBq_bwAhVG7GEKHX49DkIQ_AUoAXoECAIQAw&cshid=1622547309388377&biw=1920&bih=880"
#             driver.get(sUrl)
            
#             time.sleep(1)
            
#             a_first_image = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
#             a_first_image.click()
            
#             time.sleep(3)
                        
#             close_mark = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[2]/a')
#             close_mark.click()
    
#     else:
#         print("Error Code:" + rescode)


url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
# url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

for file in os.listdir('Resource/celeb'):
    
    files = {'image': open(f'Resource/celeb/{file}', 'rb')}

    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code

    if(rescode == 200):
        json_response = json.loads(response.text)
        
        # print(json_response)
        info =  json_response.get('info')
        faces = json_response.get('faces')
        
        for face in faces:
            print('emotion =', face.get('emotion').get('value'), 'confidence=', int(float(face.get('emotion').get('confidence')) * 100))
       
    
    else:
        print("Error Code:" + rescode)

