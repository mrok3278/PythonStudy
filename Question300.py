# Question300.py

import random

# 1
print("Hello world")

# 2
print("Mary's cosmetics")

# 3
print("""Mr.sin was shouting "It's a thief.""")

# 4
print("c:\\Windows")

# 5
print("Hello.\nIt's nice to \t\tmmet you.")

# 6
print("Today is","Thurday")

# 7
print("naver;kakao;sk;samsung")

# 8
print("naver/kakao/sk/samsung")

#9
print("first", end=" "); print("second")

#10
print(5/3)

# TODO 11~


#21
sText = "python"
print("%s %s" % (sText[0], sText[2]))

#22
sText = "24가 2210"
print("%s" % ( sText.split(" ")[-1]))

#23
sText = "홀짝홀짝"
print("%s" % (sText[::2]))

#24
sText = "PYTHON"
print("%s" % (sText[::-1]))

#25
sText = "010-1234-5678"
print("%s" % ( sText.replace("-", " ")))

#26
sText = "010-1234-5678"
print("%s" % ( sText.replace("-", "")))

#27
sText = "http://sharebook.kr"
print("%s" % ( sText.split(".")[-1]))

#28
sText = "python"
# sText[0] = 'P'
sText = 'P' + sText[1:]
print("%s" % (sText))

#29
sText = "abcdfe2a354a32a"
print("%s" % (sText.replace('a', 'A')))

#30
sText = "abcd"
print("%s" % (sText.replace('b', 'B')))

#31
sText1 = "a"
sText2 = "b"
print("%s" % (sText1 + sText2))

#32
print("%s" % ("hi" * 3))

#33
print("-" * 80)

#34
sText1 = "Python"
sText2 = "Java"
print("%s" % ((sText1 + ' ' + sText2) * 5))

#35~37
sName = "김민수"; iAge = 10
print("Name : %s Age: %d" % (sName,iAge ))
print("Name : {0} Age: {1}".format("김민수",10))
print(f"Name : {sName} Age: {iAge}")

#38
sText = "123,456,789,"
iNumber = int(sText.replace(',',''))
print("Number : %d" % (iNumber))

#39
sText = "2020/03(E) (IFRS연결)"
print("%s" % (sText[0:7]))

#40
sText = "     2020/03(E) (IFRS연결)    "
print("%s" % (sText.strip()))

# TODO 41~

#51
lMovies = ["Iron Man", "Hulk", "Thor"]

#52
lMovies.append ("Batman")
print(lMovies)

#53
lMovies.insert(2, "Superman")
print(lMovies)

#53 ~ 55
lMovies.remove("Superman")
del lMovies[1]
print(lMovies)

#56
sLang1 = ["C", "C++", "JAVA"]
sLang2 = ["Python", "Go", "C#"]
sLangs = sLang1 + sLang2
print(sLangs)

#57
iNumbers = [3,1,9,7,5,2]
print("Min: %d  Max:%d" %(min(iNumbers), max(iNumbers)))

#58
print("Sum: %d" %(sum(iNumbers)))

#59
sCook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print("Cook's len: %d" %(len(sCook)))

#60
print("Sum: %.1f" %(sum(iNumbers) / len(iNumbers)))

#61
rPrice = ['20180728', 100, 130, 140, 150, 160, 170]
print("price: ", rPrice[1:])

#62 ~ 64
rPrice = [1,2,3,4,5,6,7,8,9,10]
print("price: ", rPrice[::2])
print("price: ", rPrice[1::2])
print("price: ", rPrice[::-1])

#65
sText = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("1 = %s, 2 = %s " %(sText[0], sText[2] ))
print("Text = %s " %(" ".join(sText)))
print("Text = %s " %("\n".join(sText)))

#69
sText = "삼성전자/LG전자/Naver"
print("Spint = %s" %(sText.split('/')))

#70
nData = [2, 4, 3, 1, 5, 10, 9]
nData.sort()
nData.reverse()
print("Number = ", nData)

#71
tData = ()
print(tData)
print(type(tData))

#72
tData = ("Iron Man", "Hulk", "Thor")
print(tData)

#73
tData = (1)
print("data ", tData ,"type ",type(tData))

tData = (1,)
print("data ", tData ,"type ",type(tData))

#74
tData = (1,2,3)
# It error tData[0] = "a"
tData = tData + (4,)
print("data ", tData)

#75
tData = 1,2,3
print("data ", tData ,"type ",type(tData))

#76
tData = ('a', 'b', 'c')
tData = ('A', 'b', 'c')
print("data ", tData ,"type ",type(tData))

#77
tData = ('삼성전자', 'LG전자', 'SK Hynix')
lData = list(tData)
print("data ", lData ,"type ",type(lData))

#78
lData.append("카카오")
tData = tuple(lData)
print("data ", tData ,"type ",type(tData))

#79
tData = ('apple', 'banana', 'cake')
a, b, c = tData
print(a, b, c)

#80
tData = tuple(range(2, 101, 2))
print(tData)

#81 ~ 83

#84
dicTemp = {}
print("dicTemp=",dicTemp)

#85
dicTemp = {"메로나":1000, 
           "폴라포":1200,
           "빵빠레":1800}
print("dicTemp=",dicTemp)

#86
dicTemp["죠스바"] = 1200
dicTemp["월드콘"] = 1500
print("dicTemp=",dicTemp)

#87
print("메로나=",dicTemp["메로나"])

#88
dicTemp["메로나"] = 999
print("메로나=",dicTemp["메로나"])

#89
del dicTemp["메로나"]
print("dicTemp=",dicTemp)

#91
dicTemp = {
        "메로나":[300, 20], 
        "비비빅":[400, 30],
        "죠스바":[250, 40]
        }
print("dicTemp=",dicTemp)

#92
print("메로나[0]=", dicTemp["메로나"][0])

#93
print("메로나[1]=", dicTemp["메로나"][1])

#94
dicTemp["월드콘"] = [500, 10]
print("dicTemp=",dicTemp)

#95
print("lDicKey=", list(dicTemp.keys()))

#96
print("lDicVaule=", list(dicTemp.values()))

#97
iQty = 0
iValue = 0
iSum  = 0
 
for sValue in dicTemp.values():
    iQty = int(sValue[0])
    iValue = int(sValue[1])
    iSum += int(sValue[0]) *  int(sValue[1])

print("iSum=", iSum)

#98
dicAdd = {
        "월드콘":[600, 80],
        "구구콘":[700, 90]
        }

dicTemp.update(dicAdd)
print("dicTemp=",dicTemp)

#99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

dicTemp = dict(zip(keys,vals))
print("dicTemp=",dicTemp)

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

dicTemp = dict(zip(date,close_price))
print("dicTemp=",dicTemp)

#101 ~ 110 If

#111
#print(input() * 2)

#112
# print("Number + 10 =", int(input()) +10)

#113
# iInput = int(input())
iInput = 1
if (iInput % 2 != 0):
    print("%d  = 홀수" %(iInput))
else:
    print("%d  = 짝수" %(iInput))

#114
#iInput = min(int(input()) + 20, 255)
print("Number = ", iInput)

#115
# iInput = int(input())

if (iInput - 20 < 0):
    print(0)
elif  (iInput - 20 > 255):
    print(255)
else:
    print(iInput)

## commit ?

# 116
# sInput = input("Input the time(hh:mm): ")
sInput =""

if sInput.find(":") <= 0 :
    print("Invalid format")

elif sInput.split(":")[1] == "00":
    print("정각입니다")
else:
    print("정각이 아닙니다.")

# 117
sFruit = ["사과", "포도", "홍시"]
# sInput = input("Fruit: ")
sInput =""
if sInput in sFruit :
    print("정답입니다.")
else:
    print("오답입니다")
        
# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# sInput = input("input: ")

if sInput in warn_investment_list :
    print("투자 경고 종목이 입니다.")
else:
    print("투자 경고 종목이 아닙니다")

# 119 ~ 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# sInput = input("input: ")

if sInput in fruit:
    print(fruit.get(sInput))
else:
    print("No")

# 121
if random.randint(1, 2) % 2 == 0:
    sChar = "a"
else:
    sChar = "A"

if sChar.islower():
    print("sChar = ", sChar.upper())
else:
     print("sChar = ", sChar.lower())
     
# 122
sGrade = ""
iScore = 0
# iScore = int(input("점수를 입력하세요 : "))

if iScore > 100 or iScore < 0:
    sGrade = None
elif iScore >= 81:
    sGrade = "A"
elif iScore >= 61:
    sGrade = "B"
elif iScore >= 41:
    sGrade = "C"
elif iScore >= 21:
    sGrade = "D"
else:
    sGrade = "E"
    
print("sGrade = ", sGrade)

# 123
lRate =  {"D":1167, "N":1.096, "E":1268, "Y":171}
# sPrice = input("금액을 입력하세요. : ")
sPrice = "200 D"
iPrice = int(sPrice.split(" ")[0])             
sType = sPrice.split(" ")[1].upper()
iRate = lRate[sType]
print("Rate = %.4f Price = %.4f" %(iRate, iRate * iPrice))

# 124
iInput = 0
# iInput = int(input("1: "))
# iInput = max(iInput, int(input("2: ")))
# iInput = max(iInput, int(input("3: ")))
print("Max = ", iInput)

# 125
dCompany = {"011":"SKT", "016":"KT", "019":"LG", "010":"Other"}
# sPhone = input("Phone = ")
sPhone= "010"
print("Company = ", dCompany.get(sPhone[0:3]))

# 126
# sInput = input("Postcode: ")
sInput= "01400"
sThirdChar = sInput[2:3]
if sThirdChar in "012":
    print("강북구")
elif sThirdChar in "345":
    print("도봉구")
else:
    print("노원구")
    
# 127
sID = "123456-?234567"
sID = sID.replace("?", str(random.randint(1, 4)))
sSex = sID.split("-")[1][0:1]

if sSex in  "13":
    print("남자 =", sID)
else:
    print("여자 =", sID)

# 128
sID = "821010-1635210"
print("ilen", len(sID))
for iLoop, sChar in enumerate(sID):
    if not sChar.isnumeric():
        continue
    
    print("iLoop=", iLoop, " sChar =", sChar)
    
