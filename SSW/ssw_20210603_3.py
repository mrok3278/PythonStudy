import cv2  # pip install opencv-python

# 이미지에 도형 그리기 - 사각형
img = cv2.imread('ocr1.jpg', cv2.IMREAD_COLOR)
cv2.rectangle(img, [50, 50], [100, 100], (0, 0, 255), 1)
cv2.imshow('rectangle', img)
cv2.waitKey()
cv2.destroyAllWindows()


# 이미지에 도형 그리기 - 선
img = cv2.imread('ocr1.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (50, 50), (100, 100), (0, 255, 0), 3)
cv2.imshow('line', img)
cv2.waitKey()
cv2.destroyAllWindows()
