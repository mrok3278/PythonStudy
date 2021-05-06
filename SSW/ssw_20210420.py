# 퀴즈
a = 1
b = 2
c = "3"
d = "4"

print(a + b)  # 3
print(c + d)  # 34
# print(a + c)  # 
# print(a + d)  #

print('-' * 20)


# 문자 위치 알려주기(인덱스 번호)
a = "Python is the best choice"
print(a.find('n'))
print(a.find('t'))  # 가장 앞의 t 에 대한 인덱스 번호
print(a.find('z'))  # 해당 문자가 없으면 -1 반환

print('-' * 20)

a = "Life is too short"
print(a.index('i'))
# print(a.index('z')) # 해당 문자가 없으면 오류 발생


# 문자열 삽입
a = ",".join('abcd')
print(a)

a = " ".join('abcd')
print(a)

# 퀴즈
'''
a
b
c
d
'''
a = "\n".join('abcd')
print(a)

a = "\t".join('abcd')
print(a)

print('-' * 20)

# 소문자를 대문자로
a = "hi"
print(a.upper())

# 대문자를 소문자로
a = "HELLO"
print(a.lower())

a = "Hello Python"
print(a.upper())
print(a.lower())

print('-' * 20)

# 공백 제거
a = "   hi   "
print(a.lstrip() + '!')   # 왼쪽 공백 제거
print(a.rstrip() + '!')   # 오른쪽 공백 제거
print(a.strip() + '!')    # 양쪽 공백 제거

a = "  Hello Python   "
print(a.strip())

print('-' * 20)

# 문자열 바꾸기
a = "  Hello Python   "
print(a.replace(" ", ""))
print(a.replace("l", "L"))
print(a.replace("l", "L", 1))   # 값 1개만 바꿈

a = "Life is too short"
print(a.replace('Life', 'Your leg'))

print('-' * 20)

# 문자열 나누기
a = "Life is too short"
print(a.split(" ")) # 공백을 기준으로 나눔
print(a.split())    # split() 값을 생략하면 공백 또는 줄바꿈을 기준으로 나눔


print('-' * 20)

# 리스트 자료형
a = [1, 2, 3]
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])

print('-' * 20)

a = '2021-03-27'
print(a[:4])
print(a[5:7])
print(a[8:])

print('-' * 20)

print(a.split('-'))
print(a.split('-')[0])
print(a.split('-')[1])
print(a.split('-')[2])

b = a.split('-')
print(b[0])
print(b[1])
print(b[2])

print('-' * 20)

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[1])
print(a[2])
print(a[3])

# 퀴즈: 'b' 만 따로 출력해보세요.
print(a[3][1])

b = a[3]
print(b)
print(b[1])

# 'Life' 문자만 출력하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[-1])
print(a[-1][-1])
print(a[-1][-1][0])

print('-' * 20)

# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[2:5])
print(a[:3])
print(a[3:])
print(a[:])
print(a[::2])   # [시작번호:끝번호(전):인덱스증감값]
print(a[::-1])

print('-' * 20)

# 리스트의 덧셈
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 리스트 곱하기 숫자
a = [1, 2]
print(a * 3)

# 리스트끼리 곱하기
a = [1, 2]
b = [3, 4]
# print(a * b)    # 오류 발생: 리스트끼리 곱셈 불가


print('-' * 20)

# 리스트 길이(요소 개수) 구하기
a = [10, 20, 30]
print(len(a))

a = []
print(len(a))

a = "Pithon"
# a[1] = 'y'  # 문자열은 인덱싱을 통해 부분적으로 값 수정 불가

# 리스트 값 수정하기
a = [1, 2, 3]
a[1] = 22       # 리스트는 인덱싱을 통해 부분적으로 값 수정 가능
print(a)

print('-' * 20)

# 리스트 값 삭제하기
a = [1, 2, 3]
del a[1]    # 인덱스 번호에 해당하는 값 삭제
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

a = ['a', 'b', 'c', 'd']
a.remove('c') # 실제 값을 기준으로 삭제
print(a)

a = ['a', 'b', 'c', 'd']
del a[2]      # 인덱스 번호 기준으로 삭제
print(a)

print('-' * 20)

# 리스트 값 추가
a = [1, 2, 3]
a.append(4) # 리스트 마지막에 값 추가
print(a)
a.append(5)
print(a)

print('-' * 20)


# 리스트 정렬
a = [1, 4, 3, 2]
a.sort()    # 오름차순 정렬
print(a)

# 역순으로 재배치
a = [1, 4, 3, 2]
a.reverse()
print(a)

# 내림차순 정렬
a = [1, 4, 3, 2]
a.sort()
a.reverse()
print(a)

# sort() 함수 사용시 주의점
a = [1, 4, 3, 2]
b = a.sort()    # sort() 함수는 단지 정렬만 하며, 결과값을 반환하지 않음
print(b)        # None

print('-' * 20)

# 위치 반환(인덱스 번호 반환)
a = [1, 2, 3]
print(a.index(1))
print(a.index(2))
print(a.index(3))
# print(a.index(300)) # 없는 요소 접근시 오류 발생


# 요소 삽입
a = [1, 2, 3]
a.insert(1, 100)    # 1번 자리에 100이 들어감
print(a)

print('-' * 20)

# 리스트 요소 꺼내기
a = [1, 2, 3]
b = a.pop() # a의 마지막 요소를 꺼내 b에 저장
print(b)
print(a)    # pop() 으로 꺼낸 값은 사라짐

a = [1, 2, 3]
b = a.pop(1)    # 해당 인덱스 값을 꺼냄
print(b)
print(a)

print('-' * 20)

# 요소 개수 세기
a = [1, 2, 3, 1]
print('1: ', a.count(1))
print('2: ', a.count(2))
print('3: ', a.count(3))
print('310: ', a.count(310))

print('-' * 20)

# 조건문
'''
돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
'''
money = False
if money:
    print('택시를 타고 간다.')
    print('아싸~')
else:
    print('걸어간다.')
    print('힘드네.')

print('집에 도착')

print('-' * 20)


# 비교 연산자
x = 3
y = 2
print(x == y)
print(x > y)

print('-' * 20)


'''
만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라
'''
money = 200000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print('-' * 20)


'''
돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라
'''
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
