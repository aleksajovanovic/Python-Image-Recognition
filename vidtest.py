import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while(1):
    # take each frame
    _, frame = cap.read()
    # convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue colour
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([120,255,255])
    # range of red colour
    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255])
    # threshold the HSV image to get only blue colours
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    # bitwise-and mask and original image
    mask = blue_mask + green_mask
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()