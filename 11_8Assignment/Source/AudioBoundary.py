
import sys
from AudioController import AudioController
from threading import Thread
class AudioBoundary:
    def __init__(self):
        self._audioController :AudioController= None
        self._thread : Thread = None
        self.menu()
    def menu(self):
        num=0
        fileCheck = False
        while True:
            print("1. Load, 2. Play, 3. Stop, 4, R-Play, 5, Plot, 6. Exit ? : ",end="")
            num = int(input())
            if num == 1:
                print("Input filename? :",end="")
                filename=input()
                self._audioController = AudioController.returnControl(filename)
                print("Sampling rate =",self._audioController.getRate())
                print("Play time = ",self._audioController.getTime())
                fileCheck=True
            elif num == 6:
                sys.exit()
            elif fileCheck==True:
                try:
                    if num == 2:
                        self.play(False)
                    elif num == 3:
                        self.stop()
                    elif num == 4:
                        self.play(True)
                    elif num == 5:
                        print("Input start time?: ",end="")
                        left = int(input())
                        print("Input end time?: ",end="")
                        right = int(input())
                        self._audioController.plot(left,right)
                except Exception as e:
                    print("오류가 발생했습니다",e)
            else:
                print("잘못된 입력입니다")

    def play(self, reverse):
        self._thread=Thread(target=self._audioController.playAudio,args=(reverse,1024))
        self._thread.start()


    def stop(self):
        self._thread=None
        self._audioController.stopAudio()

if __name__ == '__main__':
    APP=AudioBoundary()
