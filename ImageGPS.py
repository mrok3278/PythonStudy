
#  https://www.jbmpa.com/python_advanced/3

import webbrowser

from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open("Resource/20201104_152134.jpg")
info = image._getexif()
image.close()

# 새로운 딕셔너리 생성
taglabel = {}

for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    taglabel[decoded] = value

exifGPS = taglabel['GPSInfo']

print('exifGPS',exifGPS)

latData = exifGPS[2]
lonData = exifGPS[4]

print(type(latData),latData)
print(type(lonData),lonData)

# # 도, 분, 초 계산
# latDeg = latData[0][0] / float(latData[0][1])
# latMin = latData[1][0] / float(latData[1][1])
# latSec = latData[2][0] / float(latData[2][1])

# lonDeg = lonData[0][0] / float(lonData[0][1])
# lonMin = lonData[1][0] / float(lonData[1][1])
# lonSec = lonData[2][0] / float(lonData[2][1])

# # 도, 분, 초 계산
latDeg = latData[0]
latMin = latData[1]
latSec = latData[2]

lonDeg = lonData[0]
lonMin = lonData[1]
lonSec = lonData[2]

# 도, 분, 초로 나타내기
Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

sUrl = f'https://www.google.com/maps/place/{Lat}+{Lon}'
webbrowser.open(sUrl)
