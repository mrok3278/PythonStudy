# 자연어 처리 NLP(Natural Language Processing)
'''
형태소 분석에 필요한 모듈 설치
pip install konlpy          # 한글 형태소 분석기 라이브러리(코엔엘파이)
pip install jpype1==1.2.0   # https://wikidocs.net/77163
'''
from konlpy.tag import Okt

import wordcloud
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np
import random

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

no_words = ['언어', '프로그래밍']   # 제외할 단어 지정
keywords = {}
for i in nouns:
    # 단어 중 한 글자짜리 제외시키기
    if len(i) == 1:
        continue
    
    # 제외 단어 리스트에 속해있으면 제외시키기
    if i in no_words:
        continue

    # 딕셔너리 안에 해당 키가 있으면 기존값 +1
    # 해당 키가 없으면 1 을 입력
    if keywords.get(i):
        keywords[i] = keywords[i] + 1
    else:
        keywords[i] = 1

# print(keywords)

mask = np.array(Image.open('mask2.jpg'))

# 워드 클라우드 생성
wc = wordcloud.WordCloud(font_path='c:/windows/fonts/malgun.ttf',
                        background_color='white',    # #FF5E00, white, ...
                        width=800,
                        height=600,
                        mask=mask,
                        max_words=500,
                        max_font_size=300,
                        colormap='twilight_shifted'
                        # Blues, Reds, plasma, prism, ... (오류 발생시 후보맵 조회 가능)
)
cloud = wc.generate_from_frequencies(keywords)

wc.to_file('wc_test.png')

# 워드 클라우드 출력
plt.imshow(cloud)
plt.axis('off') # 축 제거
plt.show()
