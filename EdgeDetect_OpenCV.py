# Import OpenCv for computer vision
import cv2
import os
from matplotlib import pyplot as plt

IMG_PATH = os.path.join('webcamphoto.jpg')

# read image
img = cv2.imread(IMG_PATH)

#Apply Canny (used for Edge detection)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey, (5,5), 0)
canny = cv2.Canny(blur, threshold1 = 180, threshold2 = 200)

#resize Image
resized_image = cv2.resize(canny, (int(img.shape[1]/2), int(img.shape[0]/2)))

#view image using OpenCV
cv2.imshow('Frame View', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('edges.jpg', canny)
