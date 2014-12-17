import cv2
import numpy as np
import time
from threading import Thread 

POLL_FREQUENCY = .05
DOG_THRESHOLD = [1, 1, 300, 200]


class Detector:
    def __init__(self, callback, showCamera=False):
        self.camera = cv2.VideoCapture(0)
        self.callback = callback
        self.showCamera = showCamera
        self.start()
    
    def start(self):
        self.thread = Thread(target=self.run, args=())
        self.thread.start()
    def run(self):
        while True:
            time.sleep(POLL_FREQUENCY)
            # TODO replace with the location of the dog in space
            contour = self.find_largest_contour()
            if contour:
                width = self.camera.get(3)
                x_center = contour[0] + contour[2]/2
                if self.get_size(contour) >= self.get_size(DOG_THRESHOLD):
                    if x_center >= width/2:
                        self.callback("left")
                    else:
                        self.callback("right")

    def get_size(self, rect):
        return rect[2] * rect[3]

    def find_largest_contour(self):
        _, im = self.camera.read()
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
        # cv2.imshow('vid stream', im)
        key = cv2.waitKey(10)
        if key == 27:
            cv2.destroyWindow('vid stream')

        return bounding_rect

if __name__ == '__main__':
    def hi(contour):
        print contour
        d = Detector(hi, True)
