#Day02-0420.py

print("=" * 30)
print("Day02-0420.py")

def getIndexCount(sText, sFindChar):
    # To get index count of text
    # sText     - Original text
    # sFindChar - Find character

    iIndexCount = 0
    iIndex = -1

    while True:
        iIndex = sText.find(sFindChar, iIndex  +1)

        if iIndex == -1:
            break  
        
        iIndexCount = iIndexCount + 1

    return iIndexCount

a = "Python is the best choice."

print(a.find('n'))
print(a.find('t'))
print(a.find('Z'))

print(a.index('n'))
print(a.index('t'))
# print(a.index('Z'))

a = "Python is the best choice."
count = getIndexCount(a, 't')
print(f"Total count = {count}")

a = "Life is too short"
# a = a.join("abcd")
a = a.join("abcd")
print(f"a=={a}")

print("upper => {0}".format(a.upper()))
print("lower => {0}".format(a.lower()))
print("replace L -> * => {0}".format(a.upper().replace("L", "*")))
print("split ' ' => {0}".format(a.split()))

a = [1,2,3]
print("a=> {0}".format(a[0]))
print("a=> {0}".format(a[1]))
print("a=> {0}".format(a[2]))
print("a=> {0}".format(a[-1]))
print("a=> {0}".format(a[-2]))
print("a len => {0}".format(len(a)))

a = "2021-04-20"
print(a.split("-"))

for i in a.split("-"):
    print(i)

a = [1,2,3,["A","B"]]
print("a=> {0}".format(a[3][0]))
print("a=> {0}".format(a[3][1]))
  
a = [1,2,3,["A","B",["life","is"]]]
print("a=> {0}".format(a[3][2][0]))
print("a=> {0}".format(a[3][2][1]))
print("a=> {0}".format(a[2:5]))

del a[2:]
print("a[0].len=> {0}".format(a))

a = [1, 4, 3, 2]
a.sort()
a.reverse()
print(a)

a.insert(1,5)
print("a.insert(1,5) = ", a)

bMoney = False

if bMoney:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print("도착")

# Q1 - 평균점수
rDatas = [["국어",80], ["영어",75], ["수학",55]]
iSubject = 0
iTotal = 0

for rData in rDatas:
    iSubject = iSubject + 1
    iTotal = iTotal + rData[1]

print("%s의 총점: %d 평균: %.2f" % ("홍길동", iTotal, iTotal/iSubject))

# Q2 - 홀짝
if 13 % 2 == 0:
    print("짝수")
else:
    print("홀수")

# Q3, Q4 - 주민등록번호
pID = "881120-1068234"
pDate = pID.split("-")[0]
pNum = pID.split("-")[1]

print("Date = ", pDate, " Number = ", pNum,  " Sex = ", pNum[0])

# Q5 - Replace
sText = "a:b:c:d"
print("Replace =>", sText.replace(":", "#"))

# Q6 - Sort
lNumbers = [1, 3, 4, 5, 2]
lNumbers.sort()
lNumbers.reverse()
print("Number = ", lNumbers)

# Q7 - Join
sText = ["Life", "is", "too", "short"]
sText =  " ".join(sText).replace(' ', '*')
print("Text =", sText)

# Q8 - Tuple
tNumbers = (1, 2, 3)
tNumbers = tNumbers + (4, 5)
print("Tuple =", tNumbers)

# Q9 ~ 11 - Dictionary
# Syntax error - a[('a',)] = 'python'
dData = {'A':90, 'B':80, 'C':70}
print("B =", dData.pop('B'))

lNumbers = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
sNumbers = set(lNumbers)
  
print("Number = ", lNumbers)
print("Set number = ", sNumbers)



