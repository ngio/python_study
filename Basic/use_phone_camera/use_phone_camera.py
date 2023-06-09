""" https://thecleverprogrammer.com/2021/01/05/use-phone-camera-with-python/

    https://pypi.org/project/opencv-python/
    > pip install opencv-python
    > pip install opencv-contrib-python
"""
import cv2
import numpy as np

url = "Your IP Address/video"

cap = cv2.VideoCapture(url)

while(True):
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break

cv2.destroyAllWindows()


