# Day08-0511.py

import Mod1

print(Mod1.add(1,2))
print(Mod1.sub(10,3))
print(Mod1.mul(5,3))
print(Mod1.div(8, 2))

from Mod1 import mul, div

print(mul(5,3))
print(div(10,2))
# print(add(10,2)) Not imported by from

from Mod1 import *
print(add(1,2))
print(sub(10,3))
print(mul(5,3))
print(div(8, 2))

