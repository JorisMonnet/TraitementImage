import os
import cv2
import numpy as np

def showAndWait(img, string) :
    cv2.imshow(string, img)
    cv2.waitKey(0)
    
def openGrayimg():
    img = cv2.imread('./LenaX.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    showAndWait(imgGray, "base")
    return imgGray

def exo1():
    for i in range(8):
        imgRes = cv2.bitwise_and(openGrayimg(),2**i)
        showAndWait(imgRes, str(2**i))

def exo2():
    for i in range(8):
        nullBit = 0
        for j in range (i):
            nullBit +=2**j
        imgRes = cv2.bitwise_and(openGrayimg(),255-nullBit)
        showAndWait(imgRes, str(255-nullBit))

def exo3():
    path = "./BackgroudSubtraction/image_"
    imgRef = cv2.imread(path+"ref.bmp")
    imgRefGray = cv2.cvtColor(imgRef, cv2.COLOR_BGR2GRAY)
    showAndWait(imgRefGray, "imgRefGray")

    for i in range(1,25):
        img = cv2.imread(path+("0"if i<10 else "")+str(i)+".bmp")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sub = cv2.subtract(imgGray,imgRefGray)
        showAndWait(sub,"sub")

def exo4():
    img1 = cv2.imread("./images/100dollarsA.tif")
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread("./images/100dollarsC.tif")
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    showAndWait(img1-img2,"result")
if __name__ == "__main__":
    #exo1()
    exo2()
    #exo3()
    #exo4()