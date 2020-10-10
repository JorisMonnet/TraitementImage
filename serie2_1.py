import cv2,numpy as np,sys,os
from matplotlib import pyplot as plt
"""
if __name__ == "__main__":
    image = cv2.imread(sys.argv[1])
    shape = image.shape
    print("definition : ")
    print(shape[0]*shape[1])
    print("type de données : ")
    print(image.dtype)
    print("nombre de cannaux : ")
    print(shape[2])
    print("taille : ")
    print(os.path.getsize(sys.argv[1]))
    print("la valeur min : ")
    print(np.amin(image))
    print("la valeur max : ")
    print(np.amax(image))
    print("la valeur moyenne : ")
    print(np.mean(image))
    print("ecart type : ")
    print(np.std(image))
    print("mode : ")
    print(np.argmax(np.bincount(image.flatten())))
"""
if __name__ == "__main__":
    image = cv2.imread(sys.argv[1])
    color = ('r','g','b')
    labels = ('h','s','v')
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    for i,col in enumerate(color):
        hist = cv2.calcHist([image],[i],None,[256],[0,256])
        hist2,bins = np.histogram(image.ravel(),256,[0,256])
        #plt.hist(image.ravel(),256,[0,256])
        plt.plot(hist2,color = col,label=labels[i])
        plt.xlim([0,256])
    plt.title('Histogram for gray scale image')
    plt.show()
