import cv2
#SIFT and SURF implementations are no longer included in the OpenCV 3 library so
#use lower versions of OpenCV
#pip install opencv-contrib-python==3.4.2.17

img = cv2.imread('IMAGE_NAME.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#sift = cv2.xfeatures2d.SIFT_create()
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray_img, None)

kp_img = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT', kp_img)
cv2.waitKey()
