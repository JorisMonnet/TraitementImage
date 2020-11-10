""" T image """
import os
import cv2
import numpy as np
import copy


def showAndWait(img, string) :
    cv2.imshow(string, img)
    cv2.waitKey(0)

def openMorpho(img):
    """ open image : erode then dilate"""
    es = np.ones((5,5),np.uint8)
    img = cv2.erode(img, es, iterations= 1)
    img = cv2.dilate(img, es, iterations= 1)
    return img

def closeMorpho(img):
    """ close image : dilate then erode"""
    es = np.ones((5,5),np.uint8)
    img = cv2.dilate(img, es, iterations= 1)
    img = cv2.erode(img, es, iterations= 1)
    return img

if __name__ == "__main__":
    #Les opérations à réaliser sont:
    # 1-Seuillage couleur pour extraire la balle bleue (optionnel, des images seuillées sont fournies)
    # 2-Suppression des trous et des petites taches grâce à des opérations morphologiques
    # 3-Calcul du contour grâce à des opérations morphologiques

    path = "./4e/"
    imageName = "TroisBallesRougeBleueBlanche.jpg"

    #1. Get blue channel
    img = cv2.imread(os.path.join(path, imageName))
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #config UNEBALLEBLEU
    #BLUE_MIN = 47; BLUE_MAX = 255
    BLUE_MIN = 55; BLUE_MAX = 255
    (thresh, bAndW) = cv2.threshold(grayImage, BLUE_MIN, BLUE_MAX, cv2.THRESH_BINARY)
    bAndW = cv2.bitwise_not(bAndW)

    showAndWait(bAndW, "basic blue image")

    bOpen = copy.deepcopy(bAndW)
    bOpen = openMorpho(bOpen)
    showAndWait(bOpen, "Opened image")

    bOpen2 = copy.deepcopy(bAndW)
    bOpen2 = cv2.morphologyEx(bOpen2, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
    showAndWait(bOpen2, "Opened image with CV2")

    bClosed = copy.deepcopy(bAndW)
    bClosed = closeMorpho(bClosed)
    showAndWait(bClosed, "Closed image")

    bOpenClose = copy.deepcopy(bAndW)
    bOpenClose = cv2.morphologyEx(bOpenClose, cv2.MORPH_OPEN, np.ones((7,7),np.uint8))
    bOpenClose = cv2.morphologyEx(bOpenClose, cv2.MORPH_CLOSE, np.ones((7,7),np.uint8))
    showAndWait(bOpenClose, "Open then closed")

    bOpenClose = copy.deepcopy(bAndW)
    bOpenClose = cv2.morphologyEx(bOpenClose, cv2.MORPH_CLOSE, np.ones((7,7),np.uint8))
    bOpenClose = cv2.morphologyEx(bOpenClose, cv2.MORPH_OPEN, np.ones((7,7),np.uint8))
    showAndWait(bOpenClose, "Closed then open")

    es = np.ones((5,5),np.uint8)
    contour=cv2.dilate(bOpenClose, es, iterations= 1)-cv2.erode(bOpenClose, es, iterations= 1)
    showAndWait(contour, "Contour")