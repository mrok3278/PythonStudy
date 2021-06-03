''' 
    reference link : https://junyoung-jamong.github.io/computer/vision,/ocr/2019/01/30/Python%EC%97%90%EC%84%9C-Tesseract%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-OCR-%EC%88%98%ED%96%89%ED%95%98%EA%B8%B0.html 
    Have to download OCR program firstly. 
    Link : https://github.com/UB-Mannheim/tesseract/wiki 
    environment : Window 10, python 3.6 
    tesseract ver : v5.0.0.20190526.exe 
    - 이미지 글자 추출 테스트 cmd > tesseract path\name.png stdout 
    - 패키지 설치 
    pip install pillow 
    pip install pytesseract 
    pip install opencv-python 
''' 
    
import cv2
import os 
from PIL import Image 
import pytesseract 

# 설치한 tesseract 프로그램 경로 (64비트) 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
text = pytesseract.image_to_string(Image.open('Resource/text.png'), lang='kor') 
print(text)

# # 이미지 불러오기, Gray 프로세싱 
# image = cv2.imread('Resource/text.png') 
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# # write the grayscale image to disk as a temporary fil  e so we can 
# # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장. 
# filename = "{}.png".format(os.getpid()) 

# cv2.imwrite(filename, gray) 

# # Simple image to string 
# text = pytesseract.image_to_string(Image.open(filename), lang='kor') 
# os.remove(filename) 
# print(text) 

# cv2.imshow("Image", image) 
# cv2.waitKey(0)
