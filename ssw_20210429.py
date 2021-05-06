# 점심 메뉴 추천 프로그램
category = {
    '한식': ['백반', '해장국', '김치찜'],
    '일식': ['초밥', '우동', '돈까스'],
    '중식': ['짜장면', '짬뽕', '탕수육'],
    '간편식': ['샌드위치', '햄버거', '김밥'],
    '특식': ['삼계탕', '피자', '보쌈']
}


import random
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = random.choice(a)
print(result)

print('-' * 20)

print(category['한식'])
print(category['일식'])

print('-' * 20)

a = category['한식']
print(random.choice(a))

# 사용자로부터 음식 카테고리를 입력받아(input 함수 이용)
# 해당 메뉴를 랜덤으로 추천해주는 프로그램을 작성해보세요.

# while True:
#     menu = input('한식/일식/중식 중에 고르세요: ')
    
#     if menu == '':  # 입력값이 비어 있으면
#         break       # 반복문 종료

#     food_list = category.get(menu, ['뷔페', '굶기'])
#     print(random.choice(food_list))


print('-' * 20)

# 집합 자료형
'''
순서가 없다
중복이 없다
'''

s1 = set([1, 2, 3, 2, 3, 1])
# 출력값에 중괄호, 딕셔너리처럼 콜론(:)이 없음
print(s1)

s1 = {1, 2, 3}  # 중괄호 사용하여 집합 생성
print(s1)

s2 = set("Hello")
print(s2)

print('-' * 20)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)      # 교집합
print(s2 & s1)      # 교집합(순서 바꿔도 결과 같음)

print(s1 | s2)      # 합집합
print(s2 | s1)      # 합집합(순서 바꿔도 결과 같음)

print(s1 - s2)      # 차집합
print(s2 - s1)      # 차집합(순서에 따라 결과 달라짐)

print('-' * 20)

# 리스트 안에서 중복값을 제거하여 유일한 값만 남기기
a = [1, 2, 3, 1, 2, 3, 4]
b = set(a)
c = list(b)
print(c)

print(list(set(a)))

print('-' * 20)

# 집합에 값 추가하기
s1 = set([1, 2, 3])
s1.add(4)   # 값 1개 추가
print(s1)

s1.update([5, 6, 7, 8]) # 값 여러개 추가
print(s1)

# 값 제거하기
s1 = set([1, 2, 3])
s1.remove(2)    # 해당 값 삭제(인덱스 번호 아님)
print(s1)

print('-' * 20)

# 불 자료형
a = True
b = False
print(a)
print(b)
print(type(a))  # 해당 값의 자료형 출력
print(type(b))

print(type(123))
print(type('123'))

print('-' * 20)

print(1 == 1)   # 비교연산자 사용시 결과가 불 자료형으로 나타남
print(1 > 2)

print('-' * 20)

print(bool("python"))   # bool: 참 거짓 판단
print(bool(""))
print(bool(" "))

print('-' * 20)

print(bool([1, 2, 3]))  # 값이 하나라도 있으면 참
print(bool([]))         # 값이 없으면 거짓

print('-' * 20)

print(bool(1))
print(bool(0))  # 숫자형은 0만 거짓, 나머지는 모두 참
print(bool(-1))

print('-' * 20)

print(bool(None))   # None 은 항상 거짓

print('-' * 20)

# pop 함수 연습
a = [1, 2, 3, 4]
b = a.pop()
print(b)
print(a)

print('-' * 20)

a = [1, 2, 3, 4]
while a:
    print(a.pop())

print('-' * 20)

# Up & Down 게임!
'''
1~10 숫자 중 하나가 정답(정답: 5)
정답 > 응답 --> Up!
정답 < 응답 --> Down!
정답 == 응답 --> Correct!
'''
# 숫자 대신 'q' 또는 'Q' 를 입력하면 게임 종료
import random
correct = random.randint(1, 10)
while True:
    answer = int(input('1~10 사이의 값 입력: '))
    if correct > answer:
        print('Up!')
    elif correct < answer:
        print('Down!')
    elif correct == answer:
        print('Correct!')
        break

