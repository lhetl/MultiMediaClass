import os

import numpy
from pyaudio import PyAudio, Stream
from wave import Wave_read, open
import pydub
from librosa import load


class AudioData:
    def __init__(self, name: str):
        try:
            checker = name.split('.')[-1]
            self._wavDir : str=os.path.join(os.path.dirname(__file__)) + "\\file\\" + name
            if checker == "mp3":
                temp = pydub.AudioSegment.from_mp3(self._wavDir)
                file = os.path.join(os.path.dirname(__file__)) + "\\file\\" + name.split('.')[0] + ".wav"
                temp.export(file, format="wav")
                wavFile = open(file, 'rb')
                self._wavDir: str = file
            elif checker == "wav":
                wavFile = open(self._wavDir, "rb")
            self._wavFile: Wave_read = wavFile
            self._rate = self._wavFile.getframerate()
            self._time = self._wavFile.getnframes() / self._wavFile.getframerate()
            p = PyAudio()
            self._librosa = load(self._wavDir, mono=False)
            self._soundData: Stream = p.open(
                format=p.get_format_from_width(self._wavFile.getsampwidth()),
                channels=self._wavFile.getnchannels(),
                rate=self._wavFile.getframerate(),
                output=True)
        except:
            print("파일에 오류가 발생했습니다.")

    @staticmethod
    def returnData(name: str):
        return AudioData(name=name)

    @property
    def soundData(self) -> Stream:
        return self._soundData

    @property
    def wavFile(self) -> Wave_read:
        return self._wavFile

    @property
    def time(self) -> str:
        hms = ""
        timeData = self._time
        if timeData / 3600 > 1:
            hms += str(int(timeData / 3600)) + " hour "
            timeData %= 3600
        if timeData / 60 > 1:
            hms += str(int(timeData / 60)) + " min "
            timeData %= 60
        timeData = round(timeData * 1000) / 1000
        hms += str(timeData) + " sec"
        return hms
    @property
    def wavDir(self):
        return self._wavDir
    @property
    def rate(self) -> str:
        return str(self._rate) + " hz"

    def frames(self, value):
        return self._wavFile.readframes(value)

    def librosaSignal(self) -> numpy.ndarray:
        return self._librosa[0]

    def librosaRate(self) -> float:
        return self._librosa[1]
