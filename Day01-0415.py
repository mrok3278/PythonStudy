#Day01-0415.py

import datetime

# 주석 Ctrl + /
# 실행 F5, Ctrl + F5
# 라인복사 Alt + Shift + Down
# AAlt + Up / Down 위 아래 조정

print("=" * 30)
print("Day01-0415.py")


print("=" * 30)
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)

# 정수형
a = 123
print(a)

# 실수형
a = 123.45
print(a)

print("=" * 30)
a = 2
b = 3
print(a ** b) # a의 b제곱
print(a // b) # 나눈 몫
print(a % b) # 나눈 나머지

print("=" * 30)
print('Hello python')
print("Hello python")
print('''Hello python''')
print("""Hello python""")

print("=" * 30)
print("Python's favorite food is perl")
print('Python\'s favorite food is perl') # 작은따옴표만 사용할때는 \로 처리
print('\'Python is very easy.\' he says')

print("=" * 30)
print("Life is too short\nyou need Python")
print("""Life is too short
you need Python""")

print("=" * 30)
sHead = "Python "
sTail = "is fun! "

print(sHead + sTail)
print(sHead * 2)
print(sTail * 3)
# print(sTail * sTail)

print("=" * 30)
a = "Life_is_too_short_you_need_Python"
b = ""

print(a[0:4])
print(a[5:])
print(a[:6])
print(a[:-6])
print(a[-6:])
print(a[-6])
print(a[::2])
print(a[::-1]) # 반대로 출력

len1 = len(a)
len2 = len(b)
print("a = %d " %len1)
print("a = %s " %len1)
print("a = %d %d" % (len1, len1))
print("b = %d %s %c" % (len2, "100?", '0'))

print("=" * 30)
# date = "20210415Rainy"
dt_now = datetime.datetime.now()
date = dt_now.strftime('%Y%m%dCloudy')

print(date[0:4])
print(date[4:6])
print(date[6:8])
print(date[8:])

a = "Pithon"
a = a[0] + "y" + a[2:]
print(a)


print("Error is %d%%" % 98)
print("%10s %-10s FFFF" % ("hi", "hello"))

print("I ate {0} apples. so I was sick for {1} days".format(2,"three"))

name = "RokRokRok"
age = 10

# *** print(f""")
print(f"My name is {name} and I am {age} years old.")

a = f"My name is {name} and I am {age} years old."
print(a)
print(a.upper())
print(a.lower())

a = f"       My name is {name} and I am {age} years old.     "
print(a.lstrip().replace(" ","-"))
print(a.rstrip())
print(a.strip())
print(a.split())

# 마우스 휠 누르고 드래그
print("name.count R = {0}".format(name.count("R")), end='\t')
print("name.count o = {0}".format(name.count("o")), end='\t')
print("name.count k = {0}".format(name.count("k")), end='\n')

print("name.index R = {0}".format(name.index('R')))
print("name.index o = {0}".format(name.index('o')))
print("name.index k = {0}".format(name.index('k')))

f = 3.12345
print("f==> %.1f " % f)

