
# 1 - 배열에 최대값, 최소값 , 중간값을 출력해보기
import random
import math

lNum = []
for iLoop in range(0,10,1):
    lNum.append(random.randint(1,10))

# Remove duplicate values by set()
lNum = list(set(lNum))
lNum.sort()

# Middle value's index
iMiddle = round(len(lNum) / 2)

# Print results
print("Numbers =", lNum)
print("Min = %d" %(lNum[0]))
print("Max = %d" %(lNum[-1]))
print("Middle = %d" %(lNum[iMiddle]))
