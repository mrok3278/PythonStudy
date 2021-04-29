#Day02-0429.py

import random

lCartegory  = ['한식',  '일식','중식','간편식', '특식']

dicMenu = {
    '한식': ['백반', '해장국', '김치찜','갈비찜'],
    '일식': ['초밥', '우동', '돈까스'],
    '중식': ['짜장면', '짬뽕', '탕수육','깐풍기', '고추잡채'],
    '간편식': ['샌드위치', '햄버거', '김밥','피자','떡복이','튀김','과자','라면'],
    '특식': ['삼계탕', '피자']
}

sCategory = random.choice(lCartegory)
iLen = len(dicMenu[sCategory])
iRandom = random.randint(0, iLen)

sMenu = dicMenu[sCategory][iRandom]

print("Category = %s Menu = %s" %(sCategory, sMenu))

while False:
    
    sInput = "Category=" + str(lCartegory) + "? "
    sCategory = input(sInput)
    
    if sCategory in lCartegory:
        
        iRandom = random.randint(0, len(dicMenu[sCategory]))
        sMenu = dicMenu[sCategory][iRandom]
        print("Category = %s Menu = %s" %(sCategory, sMenu))
        
    else:
        print("No categoty")
        break



iArray = set([1,1,2,3,3,4,5,6,7,8,9,0])
print("iArray = ", iArray)

sText = set("hellooo")
print("sText = ", sText)

