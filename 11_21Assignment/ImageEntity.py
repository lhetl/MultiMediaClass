import os

import numpy
import numpy as np
import cv2
class ImageEntity:
    def __init__(self, imageName : str):
        try:
            self._path : str = os.path.join(os.path.dirname(__file__)) + "\\image\\" + imageName
            self._imageData : numpy.ndarray = cv2.imread(self._path,cv2.IMREAD_COLOR)
            self._height=self._imageData.shape[0]
            self._width=self._imageData.shape[1]
            self._channel=self._imageData.shape[2]
        except Exception as e:
            raise Exception("잘못된 파일명입니다.")
    @staticmethod
    def returnImageEntity(name : str):
        return ImageEntity(imageName=name)
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
