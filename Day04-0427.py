#Day02-0427.py

import random

lText = ["one", "two", "three"]

for sText in lText:
    print(sText)

sText = "abcdefg"
iLoop = 0
for sChar in sText:
    iLoop  += 1
    print("%d is %s." %(iLoop,sChar))


lMarks = [90, 25, 80, 70, 60]
iLoop = 0

for iLoop, sText in enumerate(lMarks, 1):
  
    if int(sText) > 60:
        print("FOR %d is passed (%s)." %(iLoop, int(sText)))
    else:
        print("FOR %d is failed (%s)." %(iLoop, int(sText)))

iLoop = 0
iPoint = 0

while iLoop < 10:

    iLoop += 1    
    iPoint = random.randint(1,100)
    
    if iPoint < 60:
        continue

    print(f"WHILE = {iLoop} is passed {iPoint}.")

iSum = 0
for iRange in range(1,11):
    
    print("iRange = ", iRange)
    iSum += iRange
    

for i in range(1, 10):
    
    for j in range(2, 10):
        print("%d * %d = %d" %(j, i, i*j),end="\t")

    print("")

tData = (1, 2, 3, 'a', 'b')
# del tData[0]
# tData[0] = 'a'

print("tData =", tData)
print("tData[1:] =", tData[1:])
print("tData[:2] =", tData[:2])
print("tData[1:2] =", tData[1:2])

tData1 = (1, 2, 3, 'a', 'b')
tData2 = (4, 5,'c','d')
print("tData1 +  tData2=", tData1 + tData2)

tData3 = (1, 2, 3)
tData4 = (4, 5)

# print("tData3 *  tData4 =", tData3 * tData4)
tData3 = tData3 * 2
print("tData3 * 2 =", tData3 )

dicData = {1: "1", 2: "2", 3: "3"}
dicData[len(dicData)+1] = 4
dicData[len(dicData)+1] = 5

dicData[0] = 0
del dicData[0]
print("dicData = ", dicData)

dicData = {'1': "A", '2': "B", '3': "C"}
dicData['4'] = 'D'
dicData['4'] = 'E'
print("dicData = ", dicData)

dicData = {
    "Name": "ROK",
    "Phone": "010-1234-5678"
}
dicData["Gender"] = "M"
print("dicData = ", dicData)

dicData["Name"] = "MyeongRok"
print("dicData = ", dicData)

# print("dicData email ?  ", dicData["email"]) 

dicData = {1:'a', 1:'b'}
print("dicData = ", dicData)

dicData = {
    "Name": "ROK",
    "Phone": "010-1234-5678",
    "Gender": "M"
}

print("dicData.keys() = ", dicData.keys())

print("dicData.keys() = ", dicData.keys())

for sKey in dicData.keys():
    print("Key: %s Value:%s" %(sKey, dicData[sKey]))

for sValue in dicData.values():
    print("Value:%s" %(sValue))

lData = list(dicData.keys())
print("lData[0]:", lData[0])

dicData.clear()
print("dicData = ", dicData)

dicData = {
    "Name": "ROK",
    "Phone": "010-1234-5678",
    "Gender": "M"
}

print("dicData.get('E-mail') = ", dicData.get('E-mail'))

if dicData.get('E-mail') == None:
    print("None???")

print("E-mail in dicData = ", 'E-mail' in dicData)

dicData = {
    'KR':'82',
    'JP':'81',
    'CN':'86',
    'US':'1'
}
print("dicData = ", dicData)

del dicData['JP']
print("dicData = ", dicData)


#Q1 - 3의 배수
iCounter = 0
iSum = 0

while  iCounter < 1000:
    iSum += iCounter
    iCounter += 3

print("Sum = ", iSum)

