'''
이미지 처리
https://pillow.readthedocs.io/en/stable/
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as img


# 이미지 필터링
list_var = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, 
    ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS,
    ImageFilter.FIND_EDGES, ImageFilter.SHARPEN, ImageFilter.SMOOTH,
    ImageFilter.SMOOTH_MORE
]

# 필터 리스트 생성(필터 번호 및 필터 이름)
filter_list = []
no = 0
for i in list_var:
    no += 1
    filter_list.append(f"{no}. {i.name}")   # i.name 은 12번째 줄의 ImageFilter.BLUR 중 BLUR 부분에서 Ctrl + 마우스 클릭시 해당 클래스 내용을 볼 수 있습니다. 클래스 내에 name 이라는 속성이 있으므로 사용 가능합니다.
# print(filter_list)

# 필터 번호 사용자 입력
print('\n'.join(filter_list))
i = int(input('원하시는 필터 번호를 입력하세요: '))

# 해당 필터 적용 및 저장
im = Image.open('original.png')
temp = im.filter(list_var[i-1])
temp.save('output.png')
