

from PyQt5 import QtCore, QtGui, QtWidgets
import firebase_admin
from PyQt5.QtWidgets import QTableWidgetItem
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1 import FieldFilter

cred = credentials.Certificate("ithelp-2f67c-firebase-adminsdk-ckc7c-57cd35c507.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
def populate_combo_box(combo_box):

    # Replace this code with your own logic to populate the combo box


    collections = db.collections()


    collection_names = [collection.id for collection in collections]
    combo_box.addItems(collection_names)

class Ui_show(object):
    def show_data(self):
        mylist_col = []
        documents_names=[]
        row_data=[]

        category=self.comboBox.currentText()
        print(category)

        data = db.collection(category)
        # query_result = data.get()
        # document_count = len(query_result)
        # print(document_count)

        docs = data.stream()
        for doc in docs:
            v=doc.to_dict()
            print(v)
            col_count=len(v.keys())
        self.tableWidget.setColumnCount(col_count)

        # get key's name (it will be my columns name) (k)
        for k,ve in v.items():
            mylist_col.append(k.capitalize())
        self.tableWidget.setHorizontalHeaderLabels(mylist_col)
        #  1- get all document name and its count
        documents=data.list_documents()
        for document in documents:
            documents_names.append(document.id)
        print(documents_names)
        row_count=len(documents_names)
        self.tableWidget.setRowCount(row_count)
        # 2- get all data in all documents
        for document in documents_names:
            db_ref=db.collection(category).document(document)
            rdata=db_ref.get()
            v=rdata.to_dict()
            for k,ve in v.items():
                row_data.append(ve) # ======> all data is here ['8.8.8.8', 'my home', 'google dns', '10.0.100.138', 'EGPI', 'GW']
        print(row_data)
        # # 3- display all data in table
        i=0
        for row_index in range(0,row_count):
            print(row_index)
            for col_index in range(0,col_count):
                # for count,row in enumerate (row_data,1):
                #     if count==col_count:
                #         break

                print(row_index,col_index,row_data[i])

                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(row_data[i]))
                # self.tableWidget.item(row_index, col_index).setBackground(QtGui.QColor(199, 199, 199))
                self.tableWidget.item(row_index, col_index).setForeground(QtGui.QColor(0, 0, 0))
                self.tableWidget.item(row_index, col_index).setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(15)

                self.tableWidget.item(row_index, col_index).setFont(font)
                i+=1



        # table.setItem(rowPosition, 0, QtGui.QTableWidgetItem("text1"))

    def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 600)
        MainWindow.setStyleSheet("background-image: url(360_F_167594893_dWtiBCm2kkQGeeIGcJSGKryKItZ8XAI1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 591, 71))
        self.label_2.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 75 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 110, 251, 51))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 127);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.comboBox.setObjectName("comboBox")

        populate_combo_box(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 321, 71))
        self.label_3.setStyleSheet("background-image: url(6510583-fotor-bg-remover-20230805182240.png);\n"
"color: rgb(0, 0, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 500, 171, 61))
        self.pushButton_8.setStyleSheet("border-radius : 80;\n"
"color: rgb(0, 0, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border : 5px solid blac;\n"
"border-color: rgb(0, 0, 127);\n"
"border-radius : 20;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.show_data)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(70, 190, 791, 300))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 127);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(15)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScrollMargin(18)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setCornerButtonEnabled(True)


        self.tableWidget.setObjectName("tableWidget")


        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget.verticalHeader().setMinimumSectionSize(38)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.pushButton_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show"))
        self.label_2.setText(_translate("MainWindow", "Show your Data : -"))
        self.label_3.setText(_translate("MainWindow", "Select Your Category:-"))
        self.pushButton_8.setText(_translate("MainWindow", "Show"))
        self.tableWidget.setSortingEnabled(False)

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_show()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
