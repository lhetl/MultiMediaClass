import matplotlib.pyplot as plt
from AudioData import AudioData

class AudioController:
    def __init__(self, audioData: AudioData):
        self._audioData: AudioData = audioData
        self._isPlay=False

    @staticmethod
    def returnControl(name: str):
        return AudioController(AudioData.returnData(name=name))

    def playAudio(self, reverse: bool,chunk:int):
        self._isPlay=True
        cnt=1
        if reverse==True:
            self._audioData.wavFile.setpos(self._audioData.wavFile.getnframes()-chunk)
        while len(data:=self._audioData.wavFile.readframes(chunk)):
            if self._isPlay:
                self._audioData.soundData.write(data)
                if reverse==True:
                    cnt+=1
                    if self._audioData.wavFile.getnframes()-chunk*cnt >0:
                        self._audioData.wavFile.setpos(self._audioData.wavFile.getnframes() - chunk*cnt)
                    else:
                        break
        self._isPlay=False
        # self._soundData.stop_stream() // 있으면 재생 종료시 load 초기화

    def stopAudio(self):
        changeName=self._audioData.wavDir.split("\\")[-1]
        if self._isPlay:
            self._isPlay = False
            self._audioData.soundData.stop_stream()
        self._audioData=AudioData.returnData(changeName)

    def getRate(self):
        return self._audioData.rate
    def getTime(self):
        return self._audioData.time
    def plot(self,start,end):
        rate = self._audioData.librosaRate()
        leftVal=self._audioData.librosaSignal()[0,start*rate:end*rate]
        rightVal=self._audioData.librosaSignal()[1,start*rate:end*rate]
        time = [i / rate+start for i in range(len(leftVal))]
        midVal=rightVal-leftVal

        plt.subplot(5, 1, 1)
        plt.plot(time,leftVal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.title("Left Channel")

        plt.subplot(5, 1, 3)
        plt.plot(time,rightVal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.title("Right Channel")

        plt.subplot(5, 1, 5)
        plt.plot(time,midVal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.title("Diff Channel")
        plt.show()
