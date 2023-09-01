import firebase_admin
from firebase_admin import firestore, credentials
from PyQt5 import QtCore, QtGui, QtWidgets

# cred = credentials.Certificate("ithelp-2f67c-firebase-adminsdk-ckc7c-57cd35c507.json")
# firebase_admin.initialize_app(cred)
class Add_category(object):
    def add(self):
        category = self.lineEdit.text()
        f =self.lineEdit_2.text()
        v = self.lineEdit_3.text()
        fields=f.split(",")
        values=v.split(",")
        document_data = dict(zip(fields, values))
        print(document_data)

        print(category)
        print(fields)
        print(values)

        if ((len(category)== 0) or (len(fields)==0) or (len(values)==0)):
            print(5)


            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit.clear()
            self.label.setText("Please Enter All Data")
        elif len(fields) != len(values):
            print(10)
            self.label.setText("Please make values and fields equal")
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()

        else:
            self.label.setText("")
            print("1b")

            db = firestore.client()

            # Add a new collection and document to Firestore
            collection_name = category


            # Add the document to the collection
            doc_ref = db.collection(collection_name).document()
            doc_ref.set(document_data)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 683)
        MainWindow.setStyleSheet("background-image: url(360_F_167594893_dWtiBCm2kkQGeeIGcJSGKryKItZ8XAI1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 591, 71))
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);\n"
"background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 321, 71))
        self.label_3.setStyleSheet("background-image: url(C:/Users/support-user/Downloads/6510583-fotor-bg-remover-20230805182240.png);\n"
"color: rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(430, 560, 171, 61))
        self.pushButton_8.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.add)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 321, 71))
        self.label_4.setStyleSheet("background-image: url(C:/Users/support-user/Downloads/6510583-fotor-bg-remover-20230805182240.png);\n"
"color: rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 220, 321, 41))
        self.lineEdit.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 320, 321, 41))
        self.lineEdit_2.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 430, 321, 41))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 321, 71))
        self.label_5.setStyleSheet("background-image: url(C:/Users/support-user/Downloads/6510583-fotor-bg-remover-20230805182240.png);\n"
"color: rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(570, 180, 491, 461))
        self.label_6.setStyleSheet("background-image: url(9243391-fotor-bg-remover-20230831161326.png);\n"
"background-repeat: no;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 640, 971, 61))
        self.label.setStyleSheet(
            "background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
            "color: rgb(214, 0, 0);\n"
            "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(24, 70, 1011, 31))
        self.label_7.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
                                   "color: rgb(156, 156, 156);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 1011, 31))
        self.label_8.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
                                   "color: rgb(156, 156, 156);\n"
                                   "font: 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Add New Category : -"))
        self.label_3.setText(_translate("MainWindow", "Category Name:-"))
        self.pushButton_8.setText(_translate("MainWindow", "Add"))
        self.label_4.setText(_translate("MainWindow", "Add Fields Name:-"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter all fields seperate by ,"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter all values seperate by ,"))
        self.label_5.setText(_translate("MainWindow", "Add Fields Values:-"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_7.setText(_translate("MainWindow","Rember that here you add new category and it\'s field so you should enter data for this fields "))
        self.label_8.setText(_translate("MainWindow", "but if you want to add more data go to add data button in previous page."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Add_category()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
