# 반복문 - for문

test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

print('-' * 20)

test_str = 'abcdefg'
for i in test_str:
    print(i + '입니다.')

print('-' * 20)

marks = [90, 25, 67, 45, 80, 40, 60, 67, 10, 20]
no = 0
for mark in marks: 
    no += 1     # no = no + 1 와 동일
    if mark >= 60: 
        print(f"{no}번 학생 합격입니다.")
    else: 
        print(f"{no}번 학생 불합격입니다.")

print('-' * 20)

marks = [90, 25, 67, 45, 80, 40, 60, 67, 10, 20]
for no, mark in enumerate(marks, 1): 
    if mark >= 60: 
        print(f"{no}번 학생 합격입니다.")
    else: 
        print(f"{no}번 학생 불합격입니다.")

print('-' * 20)

marks = [90, 25, 67, 45, 80, 40, 60, 67, 10, 20]
for no, mark in enumerate(marks, 1): 
    if mark < 60:
        continue    # 아래쪽 코드를 수행하지 않고 반복문의 다음 회차로 넘어감

    print(f"{no}번 학생 합격입니다.")
    
print('-' * 20)

for i in range(0, 10, 1):  # range(시작값, 끝값(미포함), 증감값)
    print(i)

print('-' * 20)

for i in range(10): # range(0, 10, 1) 과 동일
    print(i)

print('-' * 20)

for i in range(0, 10): # range(0, 10, 1) 과 동일
    print(i)

print('-' * 20)

for i in range(1, 10, 2):  # range(시작값, 끝값(미포함), 증감값)
    print(i)

print('-' * 20)

for i in range(0, 10, 2):  # range(시작값, 끝값(미포함), 증감값)
    print(i)

print('-' * 20)

# 1부터 10까지의 합계 구하기
add = 0 
for i in range(1, 11): 
    add = add + i

print(add)


# 구구단
dan = 2
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")


# 퀴즈: 원하는 단수를 입력 받아 해당 구구단을 출력해보세요. (input 함수 이용)
# dan = int(input('단수 입력: '))     # input 함수에 담기는 값은 문자열 형태
# for i in range(1, 10):
#     print(f"{dan} x {i} = {dan * i}")


# 2단부터 9단까지 구구단 출력
# 퀴즈: 단과 단 사이에 빈 줄 출력
for dan in range(2, 10):
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
    print()     # 빈 줄 출력

print('-' * 20)

# 튜플
t1 = (1, 2, 'a', 'b')
print(t1)

# del t1[0]   # 튜플은 요소값을 삭제할 수 없음

t1 = (1, 2, 'a', 'b')
# t1[0] = 111     # 튜플은 요소값을 수정할 수 없음

print('-' * 20)

# 인덱싱은 가능함
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[-1])

# 슬라이싱 가능함
print(t1[0:2])
print(t1[2:4])

print('-' * 20)

# 튜플 연산
a = (1, 2, 'a', 'b')
b = (3, 4)
print(a + b)
print(b * 3)

print(b * 3)

# 튜플 길이 구하기
a = (1, 2, 'aaa', 'bbb', 'c')
print(len(a))

a = 'abcdef'
print(len(a))

print('-' * 20)

# 딕셔너리 자료형
a = {1: 'hi'}   # {Key : Value}
print(a)

a = {1: 'hi', 2: 'hello'}
print(a)

a[3] = 'hey'    # 키 3에 'hey' 값 추가
print(a)

a[4] = [1, 2, 3]    # 키 4에 리스트 추가
print(a)

a[2] = 'HELLO'  # 키2 의 값을 HELLO 로 수정
print(a)

del(a[3])   # 키3의 값 삭제
print(a)

'''
1. 문자열, 리스트, 튜플:
    인덱스 번호를 기준으로 값에 접근 (번호로 인덱싱)
2. 딕셔너리:
    키를 기준으로 값에 접근 (이름으로 인덱싱)
'''
print('-' * 20)

a = {
    'name': '갑',
    'phone': '010-1234-1234'
}
# 퀴즈: a 딕셔너리에 본인의 성별을 'gender' 키로 추가해보세요.
a['gender'] = '남'
print(a)

print(a['name'])
print(a['phone'])
print(a['gender'])

# print(a['email'])   # 없는 키 접근시 KeyError 발생

a = [1, 2, 3]
# print(a[10])          # 없는 인덱스 접근시 IndexError 발생

print('-' * 20)

a = {1:'a', 1:'b'}  # 하나의 딕셔너리에 키는 중복 불가
print(a)

print('-' * 20)

# 딕셔너리 관련 함수
a = {
    'name': 'pey',
    'phone': '0119993323',
    'birth': '1118'
}
print(a.keys()) # 키만 모아서 출력

for i in a.keys():
    print(i)

# print(a.keys()[0])  # 오류 발생
a = list(a.keys())  # 리스트로 변환
print(a)
print(a[0])

print('-' * 20)

a = {
    'name': 'pey',
    'phone': '0119993323',
    'birth': '1118'
}
print(a.values())   # 값만 모아서 출력

print('-' * 20)

print(a.items())   # 키와 값의 쌍을 튜플로 묶어 출력

a.clear()   # 딕셔너리의 모든 요소 삭제
print(a)

print('-' * 20)

# 딕셔너리 키로 값 얻기
a = {
    'name': 'pey',
    'phone': '0119993323',
    'birth': '1118'
}
print(a['name'])
# print(a['gender'])
print(a.get('name'))
print(a.get('gender'))   # None 반환
print(a.get('gender', '?'))
print(a.get('gender', ['남', '여']))

print('-' * 20)

# 딕셔너리 안에 해당 키가 있는지 확인
print('name' in a)
print('phone' in a)
print('gender' in a)
print('pey' in a)   # 'pey' 는 key 가 아니라 value 이기 때문에 찾지 못함


# 퀴즈: 일본 국가 번호를 삭제해보세요.
a = {
    '대한민국': '+82',
    '미국': '+1',
    '일본': '+81',
    '중국': '+86'
}
del(a['일본'])
print(a)

print('-' * 20)

# 점심 메뉴 추천 프로그램
category = {
    '한식': ['백반', '해장국', '김치찜'],
    '일식': ['초밥', '우동', '돈까스'],
    '중식': ['짜장면', '짬뽕', '탕수육'],
    '간편식': ['샌드위치', '햄버거', '김밥'],
    '특식': ['삼계탕', '피자', '보쌈']
}

import random
# 랜덤 뽑기 연습
a = [1, 2, 3, 4, 5]
print(random.choice(a))     # 리스트 안에서 랜덤하게 하나 뽑음

# 한식 중에 랜덤 음식 뽑기
print(category['한식'])
print(random.choice(category['한식']))
