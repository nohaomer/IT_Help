import subprocess
import tkinter as tk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


from PyQt5 import QtCore, QtGui, QtWidgets
from google.cloud.firestore_v1 import FieldFilter

cred = credentials.Certificate("ithelp-2f67c-firebase-adminsdk-ckc7c-57cd35c507.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
def populate_combo_box(combo_box):

    # Replace this code with your own logic to populate the combo box


    collections = db.collections()


    collection_names = [collection.id for collection in collections]
    combo_box.addItems(collection_names)








class noha(object):
    def ping(self): # here ping and replay
        name=self.comboBox_2.currentText()
        category=self.comboBox.currentText()
        print(category)
        ################ select ip from name from database
        # Query the database

        docs = (
            db.collection(category)
            .where(filter=FieldFilter("name", "==", name))
            .stream()
        )

        for doc in docs:
            v = doc.to_dict()
            ip = v['ip']
            print(ip)

        ping = ""
        error = ""
        output = subprocess.run(['C:\Windows\System32\cmd.exe', '/c', f'ping {ip}'], stdout=subprocess.PIPE, text=True)
        #
        if 'Lost = 4' in output.stdout:
            print(" not replay")
            error = error + ip + " "

        else:
            print(" replay")
            ping = ping + ip + " "

        # # Create a root window


        messagebox.showinfo("outputs", f"Replay IPs are :   {ping}" + "\n" f"Not Replay IPs are : {error}")


    def ok(self): #here show data of combo box
        my_list = []  # Existing list

        # Using append() method

        category = self.comboBox.currentText()
        emp_ref = db.collection(category)
        docs = emp_ref.stream()

        for doc in docs:
            v = doc.to_dict()
            name = v['name']
            my_list.append(name)
        print(my_list)
        self.pushButton_8.hide()
        self.pushButton_7.show()
        self.label_4.show()
        self.comboBox_2.show()
        self.comboBox_2.addItems(my_list)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-image: url(360_F_167594893_dWtiBCm2kkQGeeIGcJSGKryKItZ8XAI1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 591, 71))
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 510, 171, 61))
        self.pushButton_7.setStyleSheet("border-radius : 80;\n"
                                        "color: rgb(0, 0, 127);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "border : 5px solid blac;\n"
                                        "border-color: rgb(0, 0, 127);\n"
                                        "border-radius : 20;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.hide()
        self.pushButton_7.clicked.connect(self.ping)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 190, 251, 51))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 127);\n"
                                      "background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
                                    "font: 12pt MS Shell Dlg 2;\n")
        self.comboBox.setObjectName("comboBox")
        populate_combo_box(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 300, 251, 51))
        self.comboBox_2.setStyleSheet("color: rgb(0, 0, 127);\n"
                                      "background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
                                      "font: 12pt MS Shell Dlg 2;\n")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.hide()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 321, 71))
        self.label_3.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
"color: rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 321, 71))
        self.label_4.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
"color: rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 20, 301, 521))
        self.label.setStyleSheet("background-image: url(Screenshot 2023-08-05 183012-fotor-bg-remover-2023080518319.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(350, 430, 171, 61))
        self.pushButton_8.setStyleSheet("border-radius : 80;\n"
                                        "color: rgb(0, 0, 127);\n"
                                        "font: 75 14pt \"MS Shell Dlg 2\";\n"
                                        "border : 5px solid blac;\n"
                                        "border-color: rgb(0, 0, 127);\n"
                                        "border-radius : 20;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.ok)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Ping To Your Device : -"))
        self.pushButton_7.setText(_translate("MainWindow", "Ping"))
        self.pushButton_8.setText(_translate("MainWindow", "OK"))
        self.label_3.setText(_translate("MainWindow", "Select Your Category:-"))
        self.label_4.setText(_translate("MainWindow", "Select Your Device:-"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = noha()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
