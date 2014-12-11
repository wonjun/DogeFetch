import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# def gen_mask(frame):
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # define range of blue color in HSV
#     lower_blue = np.array([110,50,50], dtype=np.uint8)
#     upper_blue = np.array([130,255,255], dtype=np.uint8)
#
#     # Threshold the HSV image to get only blue colors
#     return cv2.inRange(hsv, lower_blue, upper_blue)
#
# def rect_size(rect):
#     return (rect[0] + rect[2]) * (rect[1] + rect[3])
#
# while (1):
#   _,frame = cap.read()
#   frame = cv2.medianBlur(frame, 5)
#   mask = gen_mask(frame)
#   cv2.imshow('mask', mask)
#   contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#   if len(contours) > 0:
#     areas = [cv2.contourArea(c) for c in contours]
#     max_index = np.argmax(areas)
#     cnt=contours[max_index]
#
#     x,y,w,h = cv2.boundingRect(cnt)
#     cv2.rectangle(mask,(x,y),(x+w,y+h),(0,255,0),2)
#     cv2.imshow("Show",mask)
#
#
#
# cv2.destroyAllWindows()

while True:
    _, im = cap.read()

    hsv_img = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    COLOR_MIN = np.array([200, 200, 200],np.uint8)
    COLOR_MAX = np.array([255, 255, 255],np.uint8)
    frame_threshed = cv2.inRange(hsv_img, COLOR_MIN, COLOR_MAX)
    imgray = frame_threshed
    ret,thresh = cv2.threshold(frame_threshed,0,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Find the index of the largest contour
    if len(contours) > 0:
      areas = [cv2.contourArea(c) for c in contours]
      max_index = np.argmax(areas)
      cnt=contours[max_index]

      x,y,w,h = cv2.boundingRect(cnt)
      cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Show",im)
