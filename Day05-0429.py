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
iRandom = random.randint(0, iLen-1) 
sMenu = dicMenu[sCategory][iRandom]

print("Category = %s Menu = %s" %(sCategory, sMenu))

while False:
    
    sInput = "Category=" + str(lCartegory) + "? "
    sCategory = input(sInput)
    
    if sCategory in lCartegory:
        iLen = len(dicMenu[sCategory])
        iRandom = random.randint(0, iLen-1)
        sMenu = dicMenu[sCategory][iRandom]
        
        print("Category = %s Menu = %s" %(sCategory, sMenu))
        
    else:
        print("No categoty")
        break


# 집합
iArray = set([1,1,2,3,3,4,5,6,7,8,9,0])
print("iArray = ", iArray)

sText = set("hellooo")
print("sText = ", sText)

s1 = set([1,2,3,4,5,6])
s2 = set([5,6,7,8])
print("s1 & s2=", s1 & s2) # 교집합
print("s1 | s2=", s1 | s2) # 합집합
print("s1 - s2=", s1 - s2) # 차집합

s1.add(7)
s1.update([8,9,10])
print("s1 = ", s1)

s1.remove(10)
print("s1 remove(10) = ", s1)

print("1 == 1 ", (1 == 1))
print("1 > 2 ", (1 > 1))

print("""bool("")""", bool(""))
print("""bool(" ")""", bool(" "))
print("""bool("1")""", bool("1"))

print("s1", bool(s1))
s1.clear()
print("s1 clear", bool(s1))

a = "A"
print("a == A", bool(a == "A"))

print("NONE", bool(None))

iArray = [1,2,3,4,5,6,7,8,9,10]
print("iArray", iArray)

iPop = iArray.pop()
print("iPop=", iPop, "iArray.pop=", iArray)

iArray = [1,2,3,4,5,6,7,8,9,10]

while bool(iArray):
    print("iArray", iArray)
    iPop = iArray.pop()
    
iCorrect = random.randint(1, 10)
iAnswer = 0

while True:
    
    # a in ['q','Q']
    sAnswer = input("Numer : ")
    
    if sAnswer.upper() == "Q":
        print("Quit")
        break
        
    elif iCorrect == int(sAnswer):
        print("Collect = ", iCorrect)
        break
    
    elif iCorrect > int(sAnswer):
        print("Up")
        
    else:
        print("Down")
    

