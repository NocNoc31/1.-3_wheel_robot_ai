import cv2
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui2 import Ui_MainWindow
import numpy as np

# from cvzone.HandTrackingModule import HandDetector

from Detect_and_show import Detection
from direct1 import Ui_Form
from PyQt5 import QtWidgets
import controller_keyboard_rebuild


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.switch_but.clicked.connect(self.openUi)
        self.uic.start_but.clicked.connect(self.start_capture_video)
        self.thread = {}

    def closeEvent(self, event):
        self.stop_capture_video()

    def openUi(self, key):

        self.Second_windown = QtWidgets.QMainWindow()
        self.uic1 = Ui_Form()
        self.uic1.setupUi(self.Second_windown)
        self.Second_windown.show()
        # self.uic1.forw_but.clicked.connect(forward)
        # self.uic1.reverse_but.clicked.connect(reverse)
        # self.uic1.left_but.clicked.connect(turn_left)
        # self.uic1.right_but.clicked.connect(turn_right)
        self.uic1.start_but.clicked.connect(controller_keyboard_rebuild.get_key)
        self.uic1.back_but.clicked.connect(self.goBack)

    def goBack(self):
        self.Second_windown.close()

    def stop_capture_video(self):
        self.thread[1].stop()

    def start_capture_video(self):
        Detection()

    def show_wedcam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.camera.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888
        )
        p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


class capture_video(QThread):
    signal = pyqtSignal(np.ndarray)

    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(capture_video, self).__init__()

    def run(self):
        cap = cv2.VideoCapture(0)  # 'D:/8.Record video/My Video.mp4'
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.signal.emit(cv_img)

    def stop(self):
        print("stop threading", self.index)
        self.terminate()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
