import cv2
import time
import os

def getListOfFiles(dirName):
    ListOfFiles=cs.listdir(dirname)
    allFiles=list()

    for entry in listofFile:
        fullPath+os.path.join(dirName,entry)
        if os.path.isdir(fullPath):
            allFiles= allFiles+getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles
def main():
     dirname= 'Pictures'
     ListOfFiles =getListOfFiles(dirname)

     for i in range(10):
        imagePath=listoffiles[i]
        print (imagePath)
        cascPath= "harcascadefrontalfacedefault.xml"
        faceCascade=cv2.CascadeClassifier(cascPath)
        image=cv2.imread(imagePath)
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces=facecascade.detectMultiScale(grayscaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        for (x, y, w, h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0), 2)
        cv2.imshow("Faces found",image)
        cv2.waitkey(4)
        time.sleep(5)
        cv2.destroyAllWindows()

if __name__=='  main  ':
    main()
    
    


