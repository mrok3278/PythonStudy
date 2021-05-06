# 변수
a = [1, 2, 3]
print(id(a))    # a의 메모리 주소

b = a
print(id(b))    # b의 메모리 주소

b[0] = 10   # 메모리 주소가 같으면 한쪽 값 수정시 다른 변수 값도 함께 바뀜
print(b)
print(a)

print('-' * 20)

a = [1, 2, 3]
print(id(a))

b = a[:]    # 메모리 주소가 달라짐
print(id(b))

b[0] = 100  # b의 값만 수정됨
print(b)
print(a)

print('-' * 20)

# 함수
'''
def 함수명(매개변수1, 매개변수2, ...):
    명령문1
    명령문2
    return 반환할 값
'''

def add(a, b):  # 함수 정의
    return a + b

c = add(2, 3)   # c = 5
print(c)

print(add(3, 4))    # print(7)

def say():  # 입력값(매개변수)이 없는 함수
    return 'Hi'

print(say())    # print('Hi')

print('-' * 20)

def add(a, b):  # 결과값(return)이 없는 함수
    print(f"{a}, {b}의 합은 {a+b}입니다.")

print(add(5, 6))    # return 이 없으면 None 반환

print('-' * 20)

a = [2, 3, 1, 5, 6]
print(a.sort()) # sort 는 결과값(return)이 없는 함수 --> None 반환
print(a)

print('-' * 20)

def say():  # 입력값(매개변수)과 결과값(return) 모두 없는 함수
    print('Hi')

print(say())

print('-' * 20)

def message():
    print("A")
    print("B")

message()   # A B (함수 안의 명령문을 모두 수행 후 다음 줄로 넘어감)
print("C")  # C
message()   # A B

print('-' * 20)

def sub(a, b):
    return a - b

sub(1, 3)   # 아무것도 출력되지 않음(print 명령문이 없으므로)
print(sub(1, 3))

print('-' * 20)

result = sub(a=3, b=7)
print(result)

result = sub(b=7, a=3)  # 매개변수 이름을 지정하면 순서 상관없이 입력 가능
print(result)

print('-' * 20)

result = sub(3, 7)
print(result)

result = sub(7, 3)
print(result)

print('-' * 20)

def add_many(*args): 
    result = 0
    print(args)
    for i in args:
        result = result + i     # (1, 2)
    return result 

print(add_many(1))
print(add_many(1, 2))
print(add_many(1, 2, 3))

print('-' * 20)

a = (1, 2, 3)
for i in a:
    print(i)

print('-' * 20)

def say_nick(nick): 
    if nick == "바보": 
        print('바보라고? ')
        return  # 함수 종료
    print(f"나의 별명은 {nick} 입니다.")

say_nick('천재')
say_nick('천사')
say_nick('바보')

print('-' * 20)

def say_myself(name, old, man=True): 
    print(f"나의 이름은 {name} 입니다.") 
    print(f"나이는 {old}살입니다.") 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself('홍길동', 50, True)
print()
say_myself('홍길동', 50)
print()
say_myself('홍길동', 50, False)

print('-' * 20)

print('hello', end=' ')
print('Hi', end=' ')
print('Python', end='\n')
print('Java', end='\n')

print('-' * 20)

print('a', 'b', 'c')
print('a', 'b', 'c', sep='')
print('a', 'b', 'c', sep='#')

print('-' * 20)

a = 1 
def vartest(a): 
    # 함수 안에서의 a는 함수 밖에서의 a와는 다르다! 단지 이름만 같음!
    a = a + 1

vartest(a)
print(a)

print('-' * 20)

a = 1 
def vartest(a): 
    a = a + 1 
    return a

a = vartest(a) 
print(a)

print('-' * 20)

add = lambda a, b: a+b      # lambda: 한줄짜리 함수

def add(a, b):
    return a+b

print('-' * 20)

# 사용자 입력과 출력
print("life" + "is" + "too short")
print("life" "is" "too short")

for i in range(10):
    # print(i)
    print(i, end=' ')

print('-' * 20)

# 파일 입출력
f = open("새파일.txt", 'w')     # writing(쓰기 모드)
f.close()   # 파일 닫기

f = open("새파일2.txt", 'w', encoding='utf-8')
f.write('Hello World!\n')
f.write('Hello Python!\n')
f.write('안녕하세요!\n')
f.close()   # 파일 닫기

f = open("새파일3.txt", 'a', encoding='utf-8')  # a: appending(추가 모드)
for i in range(10):
    f.write(f"{i+1}번째 줄입니다.\n")
f.close()

print('-' * 20)

f = open("새파일3.txt", 'r', encoding='utf-8')     # r: reading(읽기 모드)
line = f.readline()     # 한 줄만 읽음
print(line)
f.close()

print('-' * 20)

f = open("새파일3.txt", 'r', encoding='utf-8')
lines = f.readlines()       # 리스트 형태로 반환
# print(lines)
for line in lines:
    print(line, end='')
f.close()

print('-' * 20)

f = open("새파일3.txt", 'r', encoding='utf-8')
data = f.read()     # 문자열 형태로 반환
print(data)
f.close()

print('-' * 20)

# 퀴즈
'''
구구단의 단수를 사용자 입력으로 받아
해당 구구단을 gugudan.txt 에 출력해보세요.
'''
f = open('gugudan.txt', 'w')
dan = input('몇 단? ')
for i in range(1, 10):
    f.write(f"{dan} x {i} = {int(dan) * i}\n")
f.close()

print('-' * 20)

# 퀴즈
'''
음식점 영수증을 bill.txt 에 출력해보세요.

대신 식당 영수증
====================
김치찌개 1인분 6000원
떡국 2인분 14000원
총 20000원
====================
감사합니다.
'''
menu = {
    '김치찌개': 6000,
    '떡국': 7000,
    '햄버거': 5000
}
order = input('어떤 음식을 주문할까요? ')
amount = input('몇 인분을 드릴까요? ')