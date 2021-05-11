# 자연어 처리 NLP(Natural Language Processing)
'''
형태소 분석에 필요한 모듈 설치
pip install konlpy          # 한글 형태소 분석기 라이브러리(코엔엘파이)
pip install jpype1==1.2.0   # https://wikidocs.net/77163
'''
from konlpy.tag import Okt

# Okt 객체 선언(Twitter 클래스)
okt = Okt()

# nouns = okt.nouns('nouns는 명사만 추출해줍니다.')
# print(nouns)

# pos = okt.pos('nouns는 명사만 추출해줍니다.')
# print(pos)

f = open('data.txt', 'r', encoding='utf-8')	
text = f.read()
f.close()
# print(text)

nouns = okt.nouns(text)
# print(nouns)

keywords = {}
for i in nouns:
    # 딕셔너리 안에 해당 키가 있으면 기존값 +1
    # 해당 키가 없으면 1 을 입력
    if keywords.get(i):
        keywords[i] = keywords[i] + 1
    else:
        keywords[i] = 1

print(keywords)

