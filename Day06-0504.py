#Day06-0504.py

print("=" * 50)
a = [1,2,3]
b = a
print(id(a), id(b))

print("=" * 50)
a = [1,2,3]
b = a[:]
print(id(a), id(b))

print("=" * 50)
a = [1,2,3]
b = a[::-1]
a[0] = 0
print(a, b)

print("=" * 50)

def add(a, b):
    return(a +b)

print("add(1,2)", add(1,2))

print("=" * 50)

def say(sHi = None):
    
    if sHi != None:
        print(sHi)
    else:
        print("Hello!")

say("Hi")
say()

print("=" * 50)

def addMany(*args):
    iTotal = 0
    sValue = ""
    
    for sValue in str(args):
        print("sValue = ", sValue)
        
        if sValue.isnumeric():
            print("Numeric value = ", sValue)
            iTotal += int(sValue)
    
    print("iTotal = ", iTotal)
    
addMany('a','b',1,3,4,5,6)

print("=" * 50)

def addDic(dicData, **kwargs):
   
    sKey = list(kwargs.keys())[0]
    sValue = list(kwargs.values())[0]                  
    
    dicData[sKey] = str(sValue)

    return dicData

dicData = {}
dicData =addDic(dicData, a=1)
dicData = addDic(dicData, name="Rok")
dicData = addDic(dicData, age=20)
print(dicData)

print("=" * 50)
add = lambda a,b: a+b
print(add(1,2))

for i in range(1,11,1):
    print(i, end=' ')

print()
print("=" * 50)
file = open("Newfile.txt", "a", encoding="utf-8")

for i in range(10):
    file.write("line %d\n" %(i))

file.close()

file = open("Newfile.txt", "r", encoding="utf-8")
sLines = file.readlines()
for iLine, sText in enumerate(sLines, 1):
    print("%d: - %s" %(iLine, sText), end="")
file.close()

file = open("Newfile.txt", "r", encoding="utf-8")
print(file.read())
file.close()


iDan = int(input("몇단? " ))
sFileName = "Gugudan_%d.txt" % (iDan)
file = open(sFileName, "w", encoding="utf-8")

for i in range(1,10,1):
    file.write("%d * %d = %d\n" %(iDan, i, iDan * i))
file.close()

file = open(sFileName, "r", encoding="utf-8")
sText = file.read()
print(sText)
file.close()


menu = {
    '김치찌개': 6000,
    '떡국': 7000,
    '햄버거': 5000
}

sMenu = input('어떤 음식을 주문할까요? ')
iQty = input('몇 인분을 드릴까요? ')

iPrice = int(menu[sMenu][0])

file = open("Recepit.txt", "w", encoding="utf-8")
file.write("대신 식당 영수증\n")
file.write("====================\n")
file.write("%s %d인분 %d원\n" %(sMenu, iQty, iPrice * iQty))
file.write("총 %d원" %(iPrice * iQty))
file.write("====================\n")
file.write("감사합니다\n")

file.close()