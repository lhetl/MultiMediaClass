import sys
from threading import Thread
import cv2
import numpy as np
from ImageControl import  ImageControl
class ImageBoundary:
    def __init__(self):
        self._imageControl : ImageControl = None
        self._thread: Thread= None
        self._imgCheck=False
    def menu(self):
        fileCheck = False
        while True:
            print("1. Load, 2. Grayscale, 3. RGB, 4. YUV, 5. LR Flip, 6. UD Flip, 7. 50% Crop, 8. Exit ?  ", end="")
            command = int(input())
            if command == 1:
                self._imgCheck=False
                print("Input filename? :", end="")
                fileName = input()
                self._imageControl = ImageControl.returnControl(fileName)
                fileCheck = True
                self.showImageThread(self._imageControl.defaultImage(),fileName)
            elif command == 8:
                self._imgCheck = False
                print("시스템을 종료합니다")
                sys.exit()
            elif fileCheck == True:
                if command == 2:
                    tmp=self._imageControl.grayColor()
                    name="GrayScale"
                    self.showImageThread(tmp, name)
                elif command == 3:
                    tmp=self._imageControl.rgbColor()
                    nameList=["RedScale","GreenScale","BlueScale"]
                    self.showImageAllThread(tmp,nameList)
                elif command == 4:
                    tmp=self._imageControl.yuvColor()
                    nameList = ["YIQScale","YCbCrScale","YPbPrScale"]
                    self.showImageAllThread(tmp,nameList)
                elif command == 5:
                    tmp=self._imageControl.lrFlip()
                    name = "LR-Flip"
                    self.showImageThread(tmp, name)
                elif command== 6:
                    tmp=self._imageControl.udFlip()
                    name = "UD-Flip"
                    self.showImageThread(tmp, name)
                elif command==7:
                    percent=50
                    tmp=self._imageControl.Crop(percent)
                    name=str(percent)+"% Crop"
                    self.showImageThread(tmp, name)
            else:
                print("잘못된 입력입니다")

    def showImageThread(self, image: np.ndarray, name: str):
        self._imgCheck=False
        try:
            self._thread = Thread(target=self.showImage, args=(image,name))
            self._thread.start()
        except:
            print("오류 발생")

    def showImageAllThread(self,image: list[np.ndarray], name: list[str]):
        self._imgCheck = False
        try:
            self._thread = Thread(target=self.showImageAll, args=(image, name))
            self._thread.start()
        except:
            print("오류 발생")
    def showImage(self,image : np.ndarray,name:str):
        cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        cv2.imshow(name,image)
        height, width, _ =image.shape
        cv2.resizeWindow(name,width,height)
        self._imgCheck=True
        while self._imgCheck is not False:
            cv2.waitKey(1)
        try:
            cv2.destroyWindow(name)
        finally:
            return
    def showImageAll(self,image: list[np.ndarray],name: list[str]):
        for i in range(len(image)):
            height, width, _ = image[i].shape
            cv2.namedWindow(name[i], cv2.WINDOW_NORMAL)
            cv2.resizeWindow(name[i],width,height)
            cv2.imshow(name[i],image[i])
        self._imgCheck = True
        while self._imgCheck is not False:
            cv2.waitKey(1)
        try:
            for i in range(len(name)):
                cv2.destroyWindow(name[i])
        finally:
            return


if __name__== '__main__':
    APP=ImageBoundary()
    APP.menu()