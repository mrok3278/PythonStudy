# 209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

print('-' * 20)

# 210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


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
# print(menu['김치찌개'])
# print(menu.get('떡국'))
total = 0

import datetime
now = datetime.datetime.now()
# print(now)

f = open('bill.txt', 'w', encoding='utf-8')
f.write('대신 식당 영수증\n')
f.write('====================\n')

while True:
    order = input('어떤 음식을 주문할까요? ')
    if order == '':
        break

    amount = int(input('몇 인분을 드릴까요? '))
    total = total + (menu.get(order) * amount)    # 음식 단가 * 수량

    f.write(f"{order} {amount}인분 {menu.get(order) * amount}원\n")

f.write(f"총 {total}원\n")
f.write('====================\n')
f.write('감사합니다.\n')
# f.write(str(now))
f.write(f"{now}")
f.close()
