import sys
import os
from PyQt5 import QtCore, uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication

from thread import Worker, NWorker, MWorker, OWorker, PWorker


class FrontWindow(QMainWindow):
    heart_signal = QtCore.pyqtSignal()
    eye_signal = QtCore.pyqtSignal()
    emotion_signal = QtCore.pyqtSignal()
    speech_signal = QtCore.pyqtSignal()
    history_signal = QtCore.pyqtSignal()

    def __init__(self, *args, **kvargs):
        super(FrontWindow, self).__init__()
        uic.loadUi("DSD.ui", self)
        self.setWindowTitle("Vaistas Diagnoser")
        self.Heartbeat_Button.clicked.connect(self.Heartbeat_Signal)
        self.Eyeblink_Button.clicked.connect(self.Eyeblink_Signal)
        self.Emotion_Button.clicked.connect(self.Emotion_Signal)
        self.Speech_Button.clicked.connect(self.Speech_Signal)
        self.History_Button.clicked.connect(self.History_Signal)

    def Heartbeat_Signal(self):
        print("Signal from Heartbeat is emitted")
        self.heart_signal.emit()

    def Eyeblink_Signal(self):
        print("Signal from EyeBlink is emitted")
        self.eye_signal.emit()

    def Emotion_Signal(self):
        print("Signal from Emotion is emitted")
        self.emotion_signal.emit()

    def Speech_Signal(self):
        print("Signal from Speech is emitted")
        self.speech_signal.emit()

    def History_Signal(self):
        print("Signal from Speech is emitted")
        self.history_signal.emit()


class Heart_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Heart_Window, self).__init__()
        self.threadpool = QThreadPool()
        worker = PWorker()
        self.threadpool.start(worker)
        # uic.loadUi('DMS.ui',self)


class Eye_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Eye_Window, self).__init__()
        self.threadpool = QThreadPool()
        worker = NWorker()
        self.threadpool.start(worker)


class Emotion_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Emotion_Window, self).__init__()
        # uic.loadUi('main.ui',self)

        self.threadpool = QThreadPool()
        worker = MWorker()
        self.threadpool.start(worker)

        # os.system("python heartbeat.py")


class Speech_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Speech_Window, self).__init__()

        # uic.loadUi('Speech.ui',self)
        # self.setWindowTitle("Speech Diagnosis")
        self.threadpool = QThreadPool()
        worker = OWorker()
        self.threadpool.start(worker)


class History_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(History_Window, self).__init__()
        # uic.loadUi('main.ui',self)
        os.system("python cred.py")
        os.system("python store.py")


class Controller:
    def D_Window(self):
        self.a = FrontWindow()
        self.a.heart_signal.connect(self.H_Window)
        self.a.show()
        self.a.eye_signal.connect(self.E_Window)
        self.a.show()
        self.a.emotion_signal.connect(self.Em_Window)
        self.a.show()
        self.a.speech_signal.connect(self.S_Window)
        self.a.show()
        self.a.history_signal.connect(self.HI_Window)
        self.a.show()

    def H_Window(self):
        # self.a.show()
        self.h = Heart_Window()
        # self.a.show()

    def E_Window(self):
        # self.a.show()
        self.e = Eye_Window()
        # self.e.show()

    def Em_Window(self):
        # self.a.show()
        self.em = Emotion_Window()
        # self.em.show()

    def S_Window(self):
        # self.a.show()
        self.s = Speech_Window()
        # self.s.show()

    def HI_Window(self):
        # self.a.show()
        self.h = History_Window()
        # self.h.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ctr1 = Controller()
    ctr1.D_Window()
    sys.exit(app.exec())
