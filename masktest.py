import cv2
import numpy
# load
img1 = cv2.imread('./images/jurassic_world.jpg')
img2 = cv2.imread('./images/receiptFont.png')
# region of interest (top-left)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
# create mask and inverse mask of img2
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
# black out left roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1',img1_bg)
# take logo region(in our case it will be random letters for png)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2',img2_fg)
#combine
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('result',img1)
cv2.waitKey(0)