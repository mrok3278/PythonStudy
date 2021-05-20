
import random

# 압축 변수 만들기
sText=""
for iLoop in range(1,101,1):
   sText += chr(random.randint(97,122))


lResult =[]
# 1자리수 압축
sText = 'abbcccddddeeeee' #a2b3c4d5e'
sText += ':'

sResult = ''
iCount = 0

for i in range(len(sText) - 1):
    print(i)
    iCount += 1
    
    if sText[i] != sText[i+1]:
        sResult = "%s%s%d" %(sResult,sText[i],iCount)
        iCount = 0


lResult.append(sResult.replace('1',''))
print(lResult)

# 2자리수 압축
sText = 'abbcbc' #a2b3c4d5e'
sText += ':'

sResult = ''
iCount = 0

for i in range(len(sText) - 1):
    print(i)
    iCount += 1
    
    if sText[i] != sText[i+1]:
        sResult = "%s%s%d" %(sResult,sText[i],iCount)
        iCount = 0


lResult.append(sResult.replace('1',''))
print(lResult)