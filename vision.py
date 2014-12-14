import cv2
import numpy as np
import time
import thread

POLL_FREQUENCY = 5

class Detector:
    def __init__(self, callback, showCamera=False):
        self.camera = cv2.VideoCapture(0)
        self.callback = callback
        self.showCamera = showCamera
        self.run()

    def run(self):
        while True:
            time.sleep(POLL_FREQUENCY)
            # TODO replace with the location of the dog in space
            contour = self.find_largest_contour()
            if contour:
                self.callback(contour)

def find_largest_contour(self):
    _, im = self.read()
    COLOR_MIN = np.array([127, 127, 127],np.uint8)
    COLOR_MAX = np.array([255, 255, 255],np.uint8)
    mask = cv2.inRange(im, COLOR_MIN, COLOR_MAX)
    output = cv2.bitwise_and(im, im, mask = mask)
    ret,thresh = cv2.threshold(mask,0,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    bounding_rect = None
    if len(contours) > 0:
      areas = [cv2.contourArea(c) for c in contours]
      max_index = np.argmax(areas)
      cnt=contours[max_index]

      bounding_rect = cv2.boundingRect(cnt)
      x,y,w,h = bounding_rect
      cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)

    # if self.showCamera:
    cv2.imshow("images", np.hstack([im, output]))

    return bounding_rect

def main():
    cap = cv2.VideoCapture(0)
    while True:
        contour = find_largest_contour(cap)

main()

# def hi(stuff):
#     return ""
#
# d = Detector(hi, True)
