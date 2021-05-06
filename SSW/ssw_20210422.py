'''
만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라
'''
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print('-' * 20)

'''
주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
'''
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass   # 가만히 있어라
else:
    print("카드를 꺼내라")


# 조건문의 조합
'''
if      : 필수(단독적으로 사용 가능)
elif    : 선택(또 다른 조건들)
else    : 선택(기타 조건일때)
'''

'''
수: 90점 이상
우: 80점 이상
미: 70점 이상
양: 60점 이상
가: 60점 미만
'''
score = 50
if score >= 90:
    print('수')
elif score >= 80:
    print('우')
elif score >= 70:
    print('미')
elif score >= 60:
    print('양')
else:
    print('가')

print('-' * 20)

score = 100
if score >= 90:
    print('수')
if score >= 80:
    print('우')
if score >= 70:
    print('미')
if score >= 60:
    print('양')
else:
    print('가')

print('-' * 20)

# 반복문 - while
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1

    print(f"나무를 {treeHit}번 찍었습니다.")

    if treeHit > 5:
        print('아이고 힘들어!!')

    if treeHit == 10:
        print("나무 넘어갑니다.")


print('-' * 20)


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())


print('-' * 20)

# Up & Down 게임!
'''
1~10 숫자 중 하나가 정답(정답: 5)
정답 > 응답 --> Up!
정답 < 응답 --> Down!
정답 == 응답 --> Correct!
'''
# import random   # 랜덤 패키지 불러오기

# print('게임 시작')
# correct = random.randint(1, 1000)  # 1~10 사이의 랜덤 정수 획득

# cnt = 0
# while True:
#     answer = int(input('1~1000 사이의 정수 입력: '))
#     cnt = cnt + 1

#     if correct > answer:
#         print('Up!', '시도횟수:', cnt)
#     elif correct < answer:
#         print('Down!', '시도횟수:', cnt)
#     elif correct == answer:
#         print('Correct!', '시도횟수:', cnt)
#         break    # 반복문 종료

# print('게임 종료')

print('-' * 20)

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print(f"남은 커피의 양은 {coffee}개입니다.")
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# print('-' * 20)

# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print(f"거스름돈 {money -300}를 주고 커피를 줍니다.")
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")

#     print(f"남은 커피의 양은 {coffee}개 입니다.")

#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

print('-' * 20)

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:  # 2로 나눈 나머지가 0 --> 짝수
        continue    # 반복문의 다음 회차로 넘어감
    print(a)


while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
    