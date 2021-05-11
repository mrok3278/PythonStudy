# Day08-0511.py

# import Mod1

# print(Mod1.add(1,2))
# print(Mod1.sub(10,3))
# print(Mod1.mul(5,3))
# print(Mod1.div(8, 2))

# from Mod1 import mul, div

# print(mul(5,3))
# print(div(10,2))
# # print(add(10,2)) Not imported by from

# from Mod1 import *
# print(add(1,2))
# print(sub(10,3))
# print(mul(5,3))
# print(div(8, 2))

# Wordcloud

import wordcloud
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np
import random

from konlpy.tag import Okt

mask = np.array(Image.open('Resource/mask.jpg'))

keywords = {}
# for iNum in range(500):
#     sKey = f"채원({iNum})"
#     keywords[sKey] = random.randint(1,10)
    
#     sKey = f"나겸({iNum})"
#     keywords[sKey] = random.randint(1,10)

file = open("Resource/news.txt", "r", encoding="utf-8")
sNews = file.read()
file.close()

okt = Okt()
lKeyword  = okt.nouns(sNews)

for sKey in lKeyword:
    
    if len(sKey) <= 1:
        continue
    
    if keywords.get(sKey):
        keywords[sKey] = keywords[sKey] + 1
    else:
        keywords[sKey] = 1

wc = wordcloud.WordCloud(
    font_path="C:/Windows/Fonts/malgun.ttf", 
    background_color="#FFFFFF",
    width=800,
    height=1000,
    mask=mask,
    colormap='twilight_shifted',
    max_font_size=300,
    max_words=500,
    )

cloud = wc.generate_from_frequencies(keywords)
wc.to_file("Resource/wordcloud.png")

plt.imshow(cloud)
plt.axis('off')
plt.show()
