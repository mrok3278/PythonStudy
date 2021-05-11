# 모듈(파일)
import mod1     # 첫번째 방법
print(mod1.add(1, 2))
print(mod1.sub(1, 2))

# from mod1 import add, sub    # 두번째 방법(모듈명 생략 가능)
# print(add(2, 3))
# print(sub(2, 3))

# from mod1 import *  # 세번째 방법(모듈명 생략 가능)
# print(add(3, 4))
# print(sub(3, 4))

# 워드 클라우드
# 텍스트 마이닝(Text Mining)
'''
https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html

wordcloud 모듈 설치 방법
    pip install wordcloud
'''
import wordcloud
import matplotlib.pyplot as plt     # as(alias): 별칭

from PIL import Image
import numpy as np
import random

mask = np.array(Image.open('mask2.jpg'))


# 시각화할 데이터 입력
keywords = {
    'Hello': 5,
    'Python': 3,
    'text': 10,
    'mining': 15,
    '텍스트': 6,
    '마이닝': 7,

    # 'Python0': 5,
    # 'Python1': 4,
    # 'Python2': 8,
}

# 다량의 임의 데이터 추가 입력
for i in range(1000):
    text = f"Python{i}"
    keywords[text] = random.randint(1, 10)

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

