import os
import cv2
import 
import numpy as np

def showAndWait(img, string) :
    cv2.imshow(string, img)
    cv2.waitKey(0)
    
def openGrayimg():
    img = cv2.imread('./LenaX.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    showAndWait(imgGray, "base")
    return imgGray


#ex3
noyau1 = {[1,1,1],[1,1,1],[1,1,1]}
noyau2 = {[-1,0,1],[-1,0,1],[-1,0,1]}
noyau3={[-1,-1,-1],[0,0,0],[1,1,1]}
noyau4={[-1,-1,-1],[-1,8,-1],[-1,-1,-1]}
noyau5={[-1,-1,-1],[-1,12,-1],[-1,-1,-1]}

if __name__ == "__main__":
    img = openGrayimg()
    showAndWait(cv2.filter2D(img,new Mat,noyau1))