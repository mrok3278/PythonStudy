# Day09-0513.py

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import matplotlib.pyplot as plt

img = Image.open('Resource/travel.png')
img.thumbnail((64,64)) # 튜플형때문에 괄호로 묶어 호출
img.save('Resource/travel_thumbnail.png')
img.close()

img = Image.open('Resource/travel.png')
newImg = img.crop((10,10,100,100))
newImg.save('Resource/travel_crop.png')
newImg.close()
img.close()

img = Image.open('Resource/travel.png')
newImg = img.rotate(180)
newImg.save('Resource/travel_rotate.png')
newImg.close()
img.close()

lImgFilter = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL, 
    ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS, ImageFilter.FIND_EDGES, 
    ImageFilter.SHARPEN, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE
]

img = Image.open('Resource/travel.png')
for iCount, filter in enumerate(lImgFilter, 1):
    
    sFilterName = str(filter).split(".")[-1]
    sFilterName = sFilterName.replace('>','')
    sFilterName = sFilterName.replace("'",'')
    
    newImg = img.filter(filter)
    # newImg.save('Resource/travel_Filter_%s.png' %(str(iCount).zfill(2)))
    newImg.save(f'Resource/travel_Filter_{sFilterName}.png')
    newImg.close()
    
img.close()

# img = Image.new(mode='RGB', size=(500, 500), color='#FFFFFF')
font = ImageFont.truetype('C:/Windows/Fonts/BROADW.TTF', size=40)

img = Image.open('Resource/travel.png')
draw = ImageDraw.Draw(img)
draw.text((100, 100), 'Hello! Python', fill='#000000', font=font)
img.save('Resource/travel_text.png', format='PNG')
img.close()

img = Image.open('Resource/travel.png')
imgSub = Image.open('Resource/wordcloud.png')
imgSub = imgSub.resize((100,100))
img.paste(im=imgSub, box=(20,20))
img.save('Resource/travel_wordcloud.png')
img.close()

TRANSPARENCY = 20   # 투명도

main_image = Image.open('Resource/travel.png')
sub_image = Image.open('Resource/wordcloud.png')
sub_image = sub_image.resize(main_image.size)   # 메인 이미지 사이즈로 맞춤

if sub_image.mode!='RGBA':
    alpha = Image.new('L', sub_image.size, 255)
    sub_image.putalpha(alpha)

paste_mask = sub_image.split()[3].point(lambda i: i * TRANSPARENCY / 100)
main_image.paste(sub_image, (0,0), mask=paste_mask)
main_image.save(('Resource/watermark.png'))
# main_image.close()

try:
    plt.imshow(main_image)
    plt.imshow(img.imread('Resource/travel_wordcloud.png'))
    plt.axis('off')
    plt.show()
    
except TypeError as e:
    print("Type error =", e)
    
except Exception as e:
    print(e)
