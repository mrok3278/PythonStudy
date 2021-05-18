import sys
import calendar

print(sys.argv)
try:
    option = sys.argv[1]

    if option == '-a':
        memo = sys.argv[2]
        f = open('memo.txt', 'a', encoding='utf-8')   # a: appending(추가 모드)
        f.write(memo)
        f.write('\n')
        f.close()
    elif option == '-v':
        f = open('memo.txt', encoding='utf-8')
        memo = f.read()
        f.close()
        print(memo)
    elif option == '-d':
        f = open("memo.txt", 'w')
        f.close()
    elif option == '-c':
        # 퀴즈: python ssw_20210518.py -c 2021   로 실행시 2021 년 달력 출력
        # 파일명: calendar_2021.txt
        year = sys.argv[2]
        f = open(f"calendar_{year}.txt", 'w')
        f.write(calendar.calendar(int(year)))
        f.close()
    else:
        print('다시 실행하세요')
except IndexError as e:
    print('다시 실행하세요.', e)
except Exception as e:
    print(e)

# 퀴즈: 존재하지 않는 옵션 입력시 "다시 실행하세요" 메시지를 출력해보세요.
# 힌트: if~elif~else, 예외처리(try~except)
# 테스트1: python ssw_20210518.py -zzz
# 테스트2: python ssw_20210518.py
