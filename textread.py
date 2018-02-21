import cv2
import numpy as np
import pytesseract
from PIL import Image

imgPath = './images/receiptImg.JPG'

def imageTextToString(imgPath):
    img = cv2.imread(imgPath, 0)
    img = cv2.medianBlur(img, 5)
    threshedImg = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    text = pytesseract.image_to_string(Image.fromarray(img))
    print(text)
    cv2.imshow('og', img)
    return;

imageTextToString(imgPath)
cv2.waitKey(0)