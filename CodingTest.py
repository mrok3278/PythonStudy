
import random
import math

def compressText(sText):
    lResult = []
    
    for iStep in range(1, math.floor(len(sText) / 2) + 1):
        
        sResult = ''
        iCount = 1
        
        for iIndex in range(0, len(sText), iStep):
            
            iSIndex = iIndex
            iEIndex = iSIndex + iStep
            sCurrText = sText[iSIndex:iEIndex]
            
            iSIndex = iIndex + iStep
            iEIndex = iSIndex + iStep
            sNextText = sText[iSIndex:iEIndex]
            
            if sCurrText == sNextText:
                iCount += 1
            else:
                sResult = "%s%d%s" %(sResult,iCount,sCurrText)
                iCount = 1
        
        lResult.append(sResult.replace('1',''))
    
    return lResult 

sText=""
for iLoop in range(1,101,1):
    
#    sText += chr(random.randint(97,122))
   sText += chr(random.randint(97,98))
   
# lResult = compressText(sText)
lResult = compressText("abcdabcd")
iMinIndex = 0
iMaxIndex = 0
iMinLength = len(sText)
iMaxLength = 0

for iIndex, sText in enumerate(lResult, 0):
    
    if iMinLength > len(sText):
        iMinLength = len(sText)
        iMinIndex = iIndex
    
    if iMaxLength <= len(sText):
        iMaxLength = len(sText)
        iMaxIndex = iIndex
    
    # print(iIndex+1, sText)        

print("Min = %d, %d, %.2f, %s" %(iMinIndex + 1, iMinLength, (len(sText)/iMinLength*100),lResult[iMinIndex]))
print("Max = %d, %d, %.2f, %s" %(iMaxIndex + 1, iMaxLength, (len(sText)/iMaxLength*100) ,lResult[iMaxIndex]))