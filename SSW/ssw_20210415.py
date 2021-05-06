print("Hello world!")
print(1 + 2)
print(1 - 2)    # Alt + Shift + ↓
print(1 * 2)    # Alt + Shift + ↓
print(1 / 2)    # Alt + Shift + ↓

# 글자 크기 조정: Ctrl + +/-

# 숫자형
a = 123     # 정수형
print(a)

a = 123.45  # 실수형
print(a)

a = 2
b = 3
print(a ** b)   # a 의 b 제곱
print(a // b)   # 나눈 몫
print(a % b)    # 나눈 나머지


# 문자열 자료형     # Ctrl + / : 주석 처리/해제
print("Hello python")
print('Hello python')
print("""Hello python""")
print('''Hello python''')


# 작은 따옴표를 출력하고 싶을때
print("Python's favorite food is perl")
# print('Python's favorite food is perl')
print('Python\'s favorite food is perl')

# 큰 따옴표를 출력하고 싶을때
print('"Python is very easy." he says.')
# print(""Python is very easy." he says.'")
print("\"Python is very easy.\" he says.'")

# 여러 줄을 한번에 출력하고 싶을때
print('''Life is too short
You need python''')
print("""Life is too short
You need python""")
# print("Life is too short
# You need python")
print('Life is too short\nYou need python')
print("Life is too short\nYou need python")

print()     # 빈 줄 출력

# 문자열 덧셈
head = "Python"
tail = " is fun"
print(head + tail)

# 문자열과 숫자의 곱셈
a = 'Python'
print(a * 2)

# 문자열과 문자열의 곱셈: 오류 발생
# print('python' * 'is fun')

print('=' * 20) # 문자열과 숫자 곱셈 응용(구분선으로 이용) Alt + Up/Down 라인 위치 변경

a = "Life is too short"
print(len(a))   # 길이 구하는 함수

b = "abcd"
print(len(b))

c = ""
print(len(c))

print('-' * 20)

# 문자열 인덱싱
a = 'Life is too short, You need Python'
print(a[0])     # a의 첫 번째 글자(0번 인덱스 값)
print(a[1])
print(a[-1])    # 끝에서 첫번째 문자
print(a[-2])    # 끝에서 두번째 문자

# 퀴즈
'''
1. Life 라는 글자를 출력해보세요. (인덱싱 이용)
'''
print(a[0] + a[1] + a[2] + a[3])

'''
2. Life is too 까지 출력해보세요. (인덱싱 이용)
'''
print(a[0] + a[1] + a[2] + a[3] + a[4] + a[5] + a[6] + a[7])

print('-' * 20)

# 문자열 슬라이싱 [시작번호:끝번호(전)]
a = 'Life is too short, You need Python'
print(a[0:4])
print(a[0:6])   # [시작번호:끝번호(전)]
print(a[:4])    # 처음부터 4번 앞까지
print(a[4:])    # 4번부터 끝까지
print(a[:])     # 처음부터 끝까지

print(a[::2])   # [시작번호:끝번호(전):인덱스번호의증감값(간격)]
print(a[::1])   # 처음부터 끝까지(마지막 1은 생략 가능)

print(a[::-1])   # [시작번호:끝번호(전):인덱스번호의증감값(간격)]

print('-' * 20)

# 퀴즈
'''
슬라이싱을 이용하여 년, 월, 일, 날씨를 각각 출력해보세요.
'''
a = '20210415Rainy'
print(a[0:4])     # 2021
print(a[4:6])     # 04
print(a[6:8])     # 15
print(a[8:13])     # Rainy

a = '20210415Cloudy'
print(a[:4])     # 2021
print(a[4:6])     # 04
print(a[6:8])     # 15
print(a[8:])     # Cloudy

print('-' * 20)

a = "Pithon"
# a[1] = 'y'  # 오류 발생(문자열은 인덱싱을 통해 값 수정 불가)
print(a[0] + 'y' + a[2:])

print('-' * 20)

# 문자열 포맷팅1
print("I eat %d apples." % 3)
print("I eat %d apples." % 5)
# print("I eat %d apples." % 'five')  # %d 자리에는 정수만 대입 가능

print("I eat %s apples." % 'five')  # %s 자리에는 숫자형, 문자열 모두 가능
print("I eat %s apples." % 2)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
# print("I ate %d apples. so I was sick for %s days." % (day, number))
print("I ate %s apples. so I was sick for %s days." % (day, number))


# 문자열 포맷팅2
print("I eat {0} apples".format(3))
print("I eat {0} apples".format(5))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {1} apples. so I was sick for {0} days.".format(number, day))


# 문자열 포맷팅3
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day='three'))


# 문자열 포맷팅4: f-string(Python 3.6 이상)
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나의 이름은 {name}입니다. 나이는 {age+10}입니다.')

print('-' * 20)

a = "hobby"
print(a.count('h'), end=' ')     # 'h' 글자 개수 세기
print(a.count('o'), end=' ')
print(a.count('b'), end=' ')
print(a.count('y'), end=' ')
print(a.count('z'), end='\n')

print('-' * 20)
