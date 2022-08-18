import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from frontend import Ui_MainWindow
import datetime


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.connectivity = 0
        self.speed = 0
        self.direction = 180
        self.current = 0
        self.voltage = 0

        self.detected = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.cam = CamThread()
        self.cam.start()

        self.cam.video.connect(self.image_update_slot)
        self.ui.screenshot.clicked.connect(self.capture)

    def capture(self):
        pic = self.cam.capture.read()[1]
        pic = cv2.flip(pic, 1)
        name = str(datetime.datetime.now())
        name = name.replace(':', '-') + '.png'
        cv2.imwrite(name, pic)

    def image_update_slot(self, image):
        self.ui.camera.setPixmap(QPixmap.fromImage(image))

    def get_values(self):
        pass

    def set_speed(self):
        pass

    def set_direction(self):
        pass

    def set_voltage(self):
        pass

    def set_current(self):
        pass

    def set_connectivity(self, value):
        x = value / 100
        y = int(x * 201)
        self.ui.hide.setGeometry(QRect(0 + y, 0, 201 - y, 50))


class CamThread(QThread):
    video = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.capture = None
        self.camera_on = False

    def run(self):
        self.camera_on = True
        self.capture = cv2.VideoCapture(0)
        while self.camera_on:
            ret, frame = self.capture.read()
            if ret:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flip_img = cv2.flip(img, 1)
                convert_img = QImage(flip_img.data, flip_img.shape[1], flip_img.shape[0], QImage.Format_RGB888)
                pic = convert_img.scaled(640, 480, Qt.KeepAspectRatio)
                self.video.emit(pic)

    def stop(self):
        self.capture.release()
        self.camera_on = False


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
