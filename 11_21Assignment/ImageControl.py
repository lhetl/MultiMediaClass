import numpy as np
from numpy import ndarray

from ImageEntity import ImageEntity
class ImageControl:
    def __init__(self, imageEntity : ImageEntity):
        self._imageEntity : ImageEntity = imageEntity
    def height(self) -> int:
        return self._imageEntity.height
    def width(self) -> int:
        return self._imageEntity.width
    @staticmethod
    def returnControl(name: str):
        return ImageControl(ImageEntity.returnImageEntity(name=name))
    def defaultImage(self):
        return self._imageEntity.imageData
    def grayColor(self) -> np.ndarray:
        height=self._imageEntity.height
        width=self._imageEntity.width
        image = self._imageEntity.imageData
        grayscale = np.zeros((height,width), dtype=np.uint8)

        for i in range(height):
            for j in range(width):
                b, g, r = image[i, j]
                grayscale[i, j] = 0.299 * r + 0.587* g + 0.114 * b
        return grayscale

    def rgbColor(self) -> list[ndarray]:
        height = self._imageEntity.height
        width = self._imageEntity.width
        image = self._imageEntity.imageData
        redScale = np.zeros((height, width), dtype=np.uint8)
        greenScale = np.zeros((height, width), dtype=np.uint8)
        blueScale = np.zeros((height, width), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                b,g,r= image[i,j]
                redScale[i,j] = r
                greenScale[i,j] = g
                blueScale[i,j] = b
        tmp: list[np.ndarray] = [redScale,greenScale,blueScale]
        return tmp
    def yuvColor(self)-> list[ndarray]:
        height = self._imageEntity.height
        width = self._imageEntity.width
        image = self._imageEntity.imageData
        YIQScale = np.zeros((height, width), dtype=np.uint8)
        YCbCrScale = np.zeros((height, width), dtype=np.uint8)
        YPbPrScale = np.zeros((height, width), dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                b, g, r = image[i, j]
                YIQScale[i, j] = 0.229 * r + 0.587* g + 0.114 * b
                YCbCrScale[i, j] = round(-(0.148*r)-(0.291*g)+(0.439*b)+128)
                YPbPrScale[i, j] = round((0.439*r)-(0.368*g)-(0.071*b)+128)

        tmp:list[np.ndarray]=[YIQScale,YCbCrScale,YPbPrScale]
        return tmp
    def lrFlip(self)-> np.ndarray:
        height = self._imageEntity.height
        width = self._imageEntity.width
        channel=self._imageEntity.channel
        image = self._imageEntity.imageData
        lrFilpNp=np.zeros((height,width,channel),dtype=np.uint8)
        for i in range(height):
            for j in range(width):
                lrFilpNp[i,j]=image[i,width-j-1]
        return lrFilpNp
    def udFlip(self)-> np.ndarray:
        height = self._imageEntity.height
        width = self._imageEntity.width
        channel = self._imageEntity.channel
        image = self._imageEntity.imageData
        udFilpNp = np.zeros((height, width, channel), dtype=np.uint8)
        for i in range(height):
            udFilpNp[i] = image[height-i-1]
        return udFilpNp
    def Crop(self,percent: int)-> np.ndarray:
        height = self._imageEntity.height
        width = self._imageEntity.width
        channel = self._imageEntity.channel
        image = self._imageEntity.imageData
        cropFilpNp = np.zeros((round(height*(percent/100)), round(width*(percent/100)), channel), dtype=np.uint8)
        setStart=(1-percent/100)/2
        startHeight=round(setStart*height)
        startWidth=round(setStart*width)
        for i in range(0,len(cropFilpNp),1):
            for j in range(0,len(cropFilpNp[0]),1):
                cropFilpNp[i,j]=image[i+startHeight,j+startWidth]
        return cropFilpNp