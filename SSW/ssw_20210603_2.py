import json

import cv2      # pip install opencv-python
import requests
import sys
import kakao_key

LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024  # 1MB
LIMIT_BOX = 40


def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)

    :param image_path: 이미지파일 경로
    :return:
    """
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None


def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()


    return requests.post(API_URL, headers=headers, files={"image": data})


def main():
    image_path, appkey = 'ocr1.jpg', kakao_key.key

    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(image_path, appkey).json()
    # print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2)))

    # [퀴즈] output 변수에 들어 있는 내용을 바탕으로
    # 인식된 모든 글자를 출력해보세요.
    # print(output['result'])
    for words in output['result']:
        print(words['recognition_words'][0])

    # [퀴즈] 인식된 글자에 테두리 선을 그려보세요.
    for o in output['result']:
        box = o['boxes']
        img = cv2.imread('ocr1.jpg', cv2.IMREAD_COLOR)
        cv2.line(img, box[0], box[1], (0, 255, 0), 1)
        cv2.line(img, box[1], box[2], (0, 255, 0), 1)
        cv2.line(img, box[2], box[3], (0, 255, 0), 1)
        cv2.line(img, box[3], box[0], (0, 255, 0), 1)
        cv2.imshow('line', img)
        cv2.waitKey()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    main()
