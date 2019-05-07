# -*- coding: utf-8 -*- 
import datetime
import cv2

capture = cv2.VideoCapture(0)

capture.set(3,640)
capture.set(4,480)
ret, frame = capture.read()

now = datetime.datetime.now().strftime("%d_%H-%M-%S")

cv2.imwrite("/home/pi/Desktop/" + str(now) + ".png", frame)
 
capture.release()
cv2.destroyAllWindows()
