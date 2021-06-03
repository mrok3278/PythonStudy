# 데이터 파싱(Parsing)

'''
[퀴즈1] 주어진 딕셔너리로부터 다음과 같이 출력해보세요.

<모의고사 결과>
--------------------
이름: 홍길동
나이: 19
성별: 남
--------------------
국어: 100
영어: 85
수학: 90
--------------------
'''
d = {
    "info": {
        "name": "홍길동",
        "age": 19,
        "gender": "남"
    },
    "data": {
        "kor": 100,
        "eng": 85,
        "math": 90
    }
}

# print(d['info'])
print('<모의고사 결과>')
print('-' * 20)
print('이름:', d['info']['name'])
print('나이:', d['info']['age'])
print('성별:', d['info']['gender'])
print('-' * 20)
print('국어:', d['data']['kor'])
print('영어:', d['data']['eng'])
print('수학:', d['data']['math'])



'''
[퀴즈2] 주어진 딕셔너리로부터 다음과 같이 출력해보세요.

<모의고사 결과>
--------------------
이름: 홍길동
나이: 19
성별: 남
--------------------
1회차
국어: 100
영어: 85
수학: 90
--------------------
2회차
국어: 100
영어: 90
수학: 95
--------------------
3회차
국어: 100
영어: 95
수학: 100
--------------------
'''

d = {
    "info": {
        "name": "홍길동",
        "age": 19,
        "gender": "남"
    },
    "data": [
        {
            "kor": 100,
            "eng": 85,
            "math": 90
        },
        {
            "kor": 100,
            "eng": 90,
            "math": 95
        },
        {
            "kor": 100,
            "eng": 95,
            "math": 100
        },
    ]
}

print('<모의고사 결과>')
print('-' * 20)
print('이름:', d['info']['name'])
print('나이:', d['info']['age'])
print('성별:', d['info']['gender'])
print('-' * 20)
# print(d['data'])
cnt = 0
for x in d['data']:
    cnt = cnt + 1
    print(f"{cnt}회차")
    print('국어:', x['kor'])
    print('영어:', x['eng'])
    print('수학:', x['math'])
    print('-' * 20)

'''
[퀴즈3] 주어진 딕셔너리로부터 다음과 같이 출력해보세요.

<모의고사 결과>
--------------------
이름: 홍길동
나이: 19
성별: 남
--------------------
평균
국어: 100.0
영어: 90.0
수학: 95.0
--------------------
'''

d = {
    "info": {
        "name": "홍길동",
        "age": 19,
        "gender": "남"
    },
    "data": {
        "kor": [100, 100, 100],
        "eng": [85, 90, 95],
        "math": [90, 95, 100]
    }
}

avg_kor = sum(d['data']['kor']) / len(d['data']['kor'])
avg_eng = sum(d['data']['eng']) / len(d['data']['eng'])
avg_math = sum(d['data']['math']) / len(d['data']['math'])

print('<모의고사 결과>')
print('-' * 20)
print('이름:', d['info']['name'])
print('나이:', d['info']['age'])
print('성별:', d['info']['gender'])
print('-' * 20)
print('평균')
print('국어:', avg_kor)
print('영어:', avg_eng)
print('수학:', avg_math)
print('-' * 20)


print('-' * 20)


