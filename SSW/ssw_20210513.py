'''
이미지 처리
https://pillow.readthedocs.io/en/stable/
'''

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as img

# 간단한 사용법
im = Image.open('mask.jpg')         # 이미지 파일 오픈
print(im)
print(im.format, im.size, im.mode)  # 이미지 파일 정보

im.save('output.jpg')             # 파일 변환(저장)


# 썸네일 생성
im = Image.open('original.png')
print(im.format, im.size, im.mode)

im.thumbnail( (64, 64) )    # thumbnail( (가로, 세로) )
im.save('output_thumbnail.png')


# 이미지 자르기
im = Image.open('original.png')
temp = im.crop( (50, 50, 300, 300) )   # crop( (x1, y1, x2, y2) )
temp.save('output_crop.png')


# 이미지 회전
im = Image.open('original.png')
temp = im.rotate(180)
temp.save('output_rotate.png')


# 이미지 리사이징
im = Image.open('original.png')
temp = im.resize( (500, 500) )  # 가로/세로 비율도 함께 적용됨
temp.save('output_resize.png')


# 이미지 필터링
im = Image.open('original.png')
temp = im.filter(ImageFilter.EMBOSS)
temp.save('output_emboss.png')

list_var = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, 
    ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS,
    ImageFilter.FIND_EDGES, ImageFilter.SHARPEN, ImageFilter.SMOOTH,
    ImageFilter.SMOOTH_MORE
]
print(len(list_var))
# 퀴즈: list_var 안에 들어있는 모든 필터를 각각 적용하여
# output_filter1.png ~ output_filter10.png 로 저장해보세요.

# im = Image.open('original.png')
# cnt = 0
# for i in list_var:
#     cnt = cnt + 1
#     print(cnt, i)

#     temp = im.filter(i)
#     temp.save(f'output_{cnt}.png')


# 이미지에 텍스트 넣기
# im = Image.new(mode='RGB', size=(400, 400), color='#FFFFFF')
im = Image.open('original.png')
draw = ImageDraw.Draw(im)
font = ImageFont.truetype(font='C:/Windows/Fonts/BROADW.TTF', size=24)
draw.text((100, 100), 'Hello world!', fill='yellow', font=font)
im.save('output_text.png', format='PNG')

# plt.imshow(img.imread('output_text.png'))
# plt.axis('off')
# plt.show()


# 이미지에 이미지 추가
main_image = Image.open('original.png')
sub_image = Image.open('mask.jpg')
sub_image = sub_image.resize((200, 200))      # 추가 이미지 사이즈 변경
main_image.paste(im=sub_image, box=(10, 10))  # box: 추가 이미지를 넣을 좌표
main_image.save('output_add.png', format='PNG')


# 워터마크 추가(투명도 적용)
# 검색어 pil 이미지 투명 워터마크
# (https://www.javaer101.com/ko/article/26402527.html)

try:
    main_image = Image.open('original100.png')
    print(4 / 0)
    sub_image = Image.open('mask.jpg')
    sub_image = sub_image.resize(main_image.size)   # 메인 이미지 사이즈로 맞춤

    TRANSPARENCY = 20   # 투명도

    if sub_image.mode!='RGBA':
        alpha = Image.new('L', sub_image.size, 255)
        sub_image.putalpha(alpha)

    paste_mask = sub_image.split()[3].point(lambda i: i * TRANSPARENCY / 100.)
    main_image.paste(sub_image, (0,0), mask=paste_mask)
    main_image.save('output_watermark.jpg')
except FileNotFoundError as e:
    print('오류 발생', e)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.', e)
except Exception as e:
    print('기타 오류 발생', e)

print('프로그램 종료')
