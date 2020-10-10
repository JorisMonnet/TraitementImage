import cv2
import numpy as np

def loadAndDisplayColorImage(imagePath):
    img = cv2.imread(imagePath)
    cv2.imshow("Image", img)
def importColorImageAsGray(imagePath):
    img = cv2.imread(imagePath,0)
    cv2.imshow("Gray Image", img)
def importColorImageAndConvert(imagePath):
    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image converted ", gray)
def splitImageOpenCV(image):
    cv2.imshow("image", image)
    b,g,r = cv2.split(image)
    cv2.imshow("blue", b)
    cv2.imshow("red",r)
    cv2.imshow("green",g)
def displaySplitImageNumpy(image):
    cv2.imshow("blue", image[:,:,0])
    cv2.imshow("red",image[:,:,1])
    cv2.imshow("green",image[:,:,2])
    print("Press any key\n")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saveGrayImage(imagePath):
    img = cv2.imread(imagePath,0)
    if cv2.imwrite("lenaGray.png", img):
        print("File saved successfully")
    else:
        print("Error in saving file")

if __name__ == "__main__":
    #loadAndDisplayColorImage("lena.png")
    #importColorImageAndConvert("lena.png")
    #importColorImageAsGray("lena.png")
    #saveGrayImage("lena.png")
    #splitImageOpenCV(cv2.imread("lena.png"))
    displaySplitImageNumpy(cv2.imread("lena.png"))
    cv2.waitKey(0)