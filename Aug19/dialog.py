# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogStitch.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stitching(object):
    def setupUi(self, Stitching):
        Stitching.setObjectName("Stitching")
        Stitching.resize(953, 535)
        self.uploadLabel = QtWidgets.QLabel(Stitching)
        self.uploadLabel.setGeometry(QtCore.QRect(20, 21, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uploadLabel.setFont(font)
        self.uploadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadLabel.setObjectName("uploadLabel")
        self.uploadButton = QtWidgets.QPushButton(Stitching)
        self.uploadButton.setGeometry(QtCore.QRect(450, 30, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uploadButton.setFont(font)
        self.uploadButton.setObjectName("uploadButton")
        self.stitchButton = QtWidgets.QPushButton(Stitching)
        self.stitchButton.setGeometry(QtCore.QRect(580, 31, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stitchButton.setFont(font)
        self.stitchButton.setObjectName("stitchButton")
        self.detectionButton = QtWidgets.QPushButton(Stitching)
        self.detectionButton.setGeometry(QtCore.QRect(710, 31, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.detectionButton.setFont(font)
        self.detectionButton.setObjectName("detectionButton")
        self.stitchedLabel = QtWidgets.QLabel(Stitching)
        self.stitchedLabel.setGeometry(QtCore.QRect(40, 150, 873, 357))
        self.stitchedLabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stitchedLabel.setText("")
        self.stitchedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stitchedLabel.setObjectName("stitchedLabel")
        self.stitchedFrame = QtWidgets.QFrame(Stitching)
        self.stitchedFrame.setGeometry(QtCore.QRect(33, 143, 887, 371))
        self.stitchedFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stitchedFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stitchedFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stitchedFrame.setObjectName("stitchedFrame")
        self.uploaded = QtWidgets.QLabel(Stitching)
        self.uploaded.setGeometry(QtCore.QRect(330, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.uploaded.setFont(font)
        self.uploaded.setText("")
        self.uploaded.setAlignment(QtCore.Qt.AlignCenter)
        self.uploaded.setObjectName("label")
        self.stitchedFrame.raise_()
        self.uploadLabel.raise_()
        self.uploadButton.raise_()
        self.stitchButton.raise_()
        self.detectionButton.raise_()
        self.stitchedLabel.raise_()
        self.uploaded.raise_()

        self.retranslateUi(Stitching)
        QtCore.QMetaObject.connectSlotsByName(Stitching)

    def retranslateUi(self, Stitching):
        _translate = QtCore.QCoreApplication.translate
        Stitching.setWindowTitle(_translate("Stitching", "Dialog"))
        self.uploadLabel.setText(_translate("Stitching", "Please upload photos to be stitched"))
        self.uploadButton.setText(_translate("Stitching", "Upload"))
        self.stitchButton.setText(_translate("Stitching", "Stitch"))
        self.detectionButton.setText(_translate("Stitching", "Detect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stitching = QtWidgets.QDialog()
    ui = Ui_Stitching()
    ui.setupUi(Stitching)
    Stitching.show()
    sys.exit(app.exec_())
