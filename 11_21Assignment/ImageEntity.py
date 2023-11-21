import os

import PIL.JpegImagePlugin
import numpy
from PIL import Image
import numpy as np
import cv2
class ImageEntity:
    def __init__(self, imageName : str):
        self._path : str = os.path.join(os.path.dirname(__file__)) + "\\image\\" + imageName
        self._imageData : numpy.ndarray = cv2.imread(self._path,cv2.IMREAD_COLOR)
        # self._npData : np.ndarray = np.array(self._imageData)
        # cv2.imshow("test", self._imageData)
        # self._npData=self._npData[:, :, ::-1].copy()
        self._height,self._width,self._channel=self._imageData.shape

    @staticmethod
    def returnImageEntity(name : str):
        return ImageEntity(imageName=name)
    # @property
    # def imageData(self) -> Image.Image:
    #     return self._imageData
    @property
    def imageData(self) -> np.ndarray:
        return self._imageData
    @property
    def height(self) -> int:
        return self._height
    @property
    def width(self) -> int:
        return self._width
    @property
    def path(self) -> str:
        return self._path
    @property
    def channel(self)-> int:
        return self._channel
