#Day03-0420.py

import random

pocket = ['paper', 'cellphone', 'money']

if('money' in pocket):
    print("택시를 타고 가라")
else:
     print("걸어가라")

if('money' in pocket):
    pass
else: 
    print("걸어가라")

iPoints  = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
sGrade = ""

for iPoint in iPoints:
    
    if iPoint > 90: sGrade = "수"
    elif iPoint > 80: sGrade = "우"
    elif iPoint > 70: sGrade = "미"
    elif iPoint > 60: sGrade = "양"
    else : sGrade = "가"

    print("%d is %s" %(iPoint, sGrade))


print("-" * 30)

iPoint = 100
sGrade = ""

while iPoint > 0:
    
    if iPoint > 90: sGrade = "수"
    elif iPoint > 80: sGrade = "우"
    elif iPoint > 70: sGrade = "미"
    elif iPoint > 60: sGrade = "양"
    else : sGrade = "가"

    print("%d is %s" %(iPoint, sGrade))
    iPoint -= 10

iHit = 0
while iHit <= 10:
    iHit += 1
    print("Hit:", iHit)

    if iHit > 5: 
        print("으쌰!")

    if iHit >= 10: 
        print("나무가 넘어 갑니다.")

sPromprt = """
1. Add
2. Del
3. List
4. Quit

Enter the number: """

iInput = 0
iHitCount = 0
while iHitCount > 0 or iInput != 4:
   
    print(sPromprt)
    
    # Input value
    # iInput = int(input())

    iHitCount += 1
    if iHitCount > 3:
        print("Over!")
        break

# Random
iAnswer = random.randint(1,10)
iCount  = 0
iInput = 0
while True:
    break
    iInput = int(input("1 ~ 10 사이의 숫자를 입력하세요. : "))
    iCount += 1
    
    if iInput == iAnswer:
        print("Correct!(%d Count = %d)" %(iAnswer, iCount))
        break

    elif(iInput > iAnswer):
        print("Up!")
    
    else:
        print("Down!")


iQty  = random.randint(1,5)
iPrice = 5
iSell = 0
iTotalPrice = 0
iInput  = 0

while True:
    break

    iInput = int(input("커피는 %d 입니다." %(iPrice)))

    if(iInput >= iPrice):
        iSell +=1
        iTotalPrice += iPrice

        if iInput > iPrice:
            print("Return: %d" % (iInput - iPrice))

        print("Here you are!")
        
    else:
        continue            
        
    if iSell == iQty:
        print("Sold out! Coffee: %d TotalPrice: %d" % (iQty, iTotalPrice))
        break


iLoop = 0
while iLoop <= 10:
    
    iLoop += 1

    if iLoop % 2 != 0 : 
        print("%d 는 홀수" %iLoop)
    else: 
        print("%d 는 짝수" %iLoop)