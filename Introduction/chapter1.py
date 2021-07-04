import cv2

print('Package imported')

#  Image *************
img = cv2.imread('Resources/lena.png')  # to readImage
cv2.imshow('Output', img)  # to show image
cv2.waitKey(0)  # for waiting that imageWindow not to close

# Video **************
cap = cv2.VideoCapture('Resources/test_video.mp4')
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Camera **************
camera = cv2.VideoCapture(0)
camera.set(3, 640)  # 3 is prop. for width
camera.set(4, 480)  # 4 is prop. for height
camera.set(10, 100)  # 10 is prop. for brightness
while True:
    success, img = camera.read()
    cv2.imshow('Camera', img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
