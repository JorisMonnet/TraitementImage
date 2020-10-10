"""Exercice 1 :
a)T=((1,2)(-1,2))
T^-1=((0.5,0.25)(-0.5,0.25))
g(1,0) : (1,0)*T^-1

Degré 0
A=(0.5,0.25) -> arrondi
-> (1,0) -> 34
B=(0,0.5)
-> 0,1 -> 22
C=(-0.5,0.75)
->(-1,1)->hors bords, retour 0 -> (0,1) = 22

Degré 1 :
Utilisation de la formule du cours -> moyenne des points avoisinants avec différents points : 
A = 0.5*0.75*33+0.75*0.5*22+0.5*0.25*34+0.5*0.25*0 = 27.875
B = 1*0.5*33+0.5*0*22+1*0.5*34*0 = 16.5
C = 1.5*0.25*33+0.25*0*22+0*0.75*34+0 = 12.375

Exercice 2 :

a)Les niveaux de gris seront tous inversés.
Application possible : améliorer le contraste (+contrasté)

b)Moins de niveau de gris. 
c)L'image sera plus "blanche" et paraitra donc plus intense =>correction contraste+maximisation de la dynamique. 
d)L'image sera noir et blanc binaire, avec un seuil
e)L'image est grisée, avec très peu de contraste =>correction du contraste -> diminution de contraste
f)solarisation  -> sur-exposition/normal
g)IMPOSSIBLE CE N'EST PAS UNE FONCTION : une image ne peut avoir plus d'un antécédent.
h)aux extrémités image identique mais variant sur la partie centrale avec décalage linéaire=>correction du contraste

Exercice 3 :
"""
import os
import cv2
import numpy as np

def showAndWait(img, string) :
    cv2.imshow(string, img)
    cv2.waitKey(0)

def histoStrange(imagePath) :
    '''Display image with normalized, equalized and CLAHE histograms'''
    img = cv2.imread(imagePath)
    showAndWait(img, "base")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    showAndWait(img, "gray")

    imgNormalized = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    showAndWait(imgNormalized, "normalized")

    imgEqualized = cv2.equalizeHist(img)
    showAndWait(imgEqualized, "equalized")

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    claheImg = clahe.apply(img)
    showAndWait(claheImg, "CLAHE")

def createConstratLT(fBase, gmax) :
    fMin = np.min(fBase)
    fMax = np.max(fBase)
    print("fmin : {}, fmax : {}".format(fMin, fMax))
    fun = lambda f : putInIntegerRange(gmax * ((f - fMin) / (fMax - fMin)), 0, 255)
    return [fun(f) for f in range(256)]

def putInIntegerRange(x, min, max) :
    x = int(x)
    return 0 if x < min else max if x > max else x

if __name__ == "__main__":
    path = "./"

    # ex3 
    """for file in os.listdir(path):
        if file.endswith((".tif", ".pgm", "bmp")) :
            histoStrange(os.path.join(path, file))
            cv2.destroyAllWindows() """
    #ex4
    img = cv2.imread('lena10.pgm')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lookupTable=np.arange( 255, -1, -1 )
    imgRes=lookupTable[img].astype(np.uint8)
    showAndWait(img,'base')
    showAndWait(imgRes,'inverted')

    lookUpConstrast = np.array(createConstratLT(img, 255)).astype(np.uint8)
    print("lookupTable contraste : {} len : {}".format(lookUpConstrast, len(lookUpConstrast)))
    imgConstrasted = lookUpConstrast[img].astype(np.uint8)
    showAndWait(imgConstrasted, "constrastée")

