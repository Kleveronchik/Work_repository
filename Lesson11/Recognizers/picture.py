import cv2
from cv2 import Mat
from PIL import Image

class Picture:
    def __init__(self, path:str):
        self.Path:str = path
        self.Image: Mat = self.Reading(self.Path)
        self.MultiScale = list()
    def Reading(self, path:str):
        return cv2.imread(path)
    def ShowImg(self, winName: str):
        cv2.imshow(winName, self.Image)
        cv2.waitKey()
    def GetCoordinates(self, path:str):
        cascade = cv2.CascadeClassifier(path)
        return cascade.detectMultiScale(self.Image)
    def Highlight(self, img:Mat):
        for (x, y, width, height) in self.MultiScale:
            cv2.rectangle(self.Image, (x, y), (x+width, y+height), (255, 143, 143), 3)
    def PasteImg(self, path:str, oldPath:str, newPath:str):
        try:
            fLayout = Image.open(oldPath)
            sLayout = Image.open(path)
            fLayoutConverted = fLayout.convert('RGBA')
            sLayoutConverted = sLayout.convert('RGBA')
            for (x, y, width, height) in self.MultiScale:
                sLayoutConverted = sLayoutConverted.resize(width, int(height/3))
                fLayoutConverted.paste(sLayoutConverted, (x, int(y + height/4)))
                fLayoutConverted.save(newPath)
                return cv2.imread(path)
        except Exception as ex:
            print(ex)
if __name__ == '__main__':
    imgPath = '../Imgs/cat.jpeg'
    winName = 'Cat'
    filePath = '../Files/haarcascade_frontalcatface_extended.xml'
    pict = Picture(imgPath)
    pict.MultiScale = pict.GetCoordinates(filePath)
    #print(pict.MultiScale)
    pict.Highlight(pict.MultiScale)
    pict.ShowImg(winName)