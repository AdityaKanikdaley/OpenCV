import cv2

img = cv2.imread('Resources/lambo.png')
print(img.shape)  # to print resolution of img

imgResize = cv2.resize(img, (640, 480))
print(imgResize.shape)  # to print resolution of imgResize

imgCropped = img[0:400, 0:800]  # here height 1st then width
print(imgCropped.shape)  # to print resolution of imgCropped

cv2.imshow("Image", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)
