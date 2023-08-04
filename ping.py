
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

from PyQt5 import QtCore, QtGui, QtWidgets




class noha(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 803)
        MainWindow.setStyleSheet("background-image: url(360_F_167594893_dWtiBCm2kkQGeeIGcJSGKryKItZ8XAI1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 591, 71))
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 320, 221, 211))
        self.label_3.setStyleSheet("background-image: url(download.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 370, 171, 61))
        self.pushButton_5.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;\n"
                                        )
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(780, 380, 181, 61))
        self.pushButton_6.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(620, 180, 171, 61))
        self.pushButton_7.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 610, 171, 61))
        self.pushButton_8.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 610, 171, 61))
        self.pushButton_9.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(340, 180, 171, 61))
        self.pushButton_10.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_10.setObjectName("pushButton_10")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, -10, 521, 251))
        self.label.setStyleSheet("background-image: url(images-fotor-bg-remover-20230804215155.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-260, 450, 721, 441))
        self.label_4.setStyleSheet("background-image: url(5170843-fotor-bg-remover-2023080422148.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Welcome from IT Helper :"))
        self.pushButton_5.setText(_translate("MainWindow", "Add Category"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete Category"))
        self.pushButton_7.setText(_translate("MainWindow", "Show Data"))
        self.pushButton_8.setText(_translate("MainWindow", "Delete Data"))
        self.pushButton_9.setText(_translate("MainWindow", "Add Data"))
        self.pushButton_10.setText(_translate("MainWindow", "Check "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = noha()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
