import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\bd")
import main_bd

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClientWindow(object):

    def setupUi(self, ClientWindow):
        ClientWindow.setObjectName("ClientWindow")
        ClientWindow.resize(427, 444)
        self.centralwidget = QtWidgets.QWidget(ClientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(1)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 190, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(1)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setLineWidth(1)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(1)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 210, 181, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 0, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setLineWidth(1)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 150, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 270, 181, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 340, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(main_bd.add_value_request_client)

        ClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClientWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 427, 26))
        self.menubar.setObjectName("menubar")
        ClientWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClientWindow)
        self.statusbar.setObjectName("statusbar")
        ClientWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ClientWindow)
        QtCore.QMetaObject.connectSlotsByName(ClientWindow)




    def retranslateUi(self, ClientWindow):
        _translate = QtCore.QCoreApplication.translate
        ClientWindow.setWindowTitle(_translate("ClientWindow", "ClientWindow"))
        self.label_6.setText(_translate("ClientWindow", "name"))
        self.label_8.setText(_translate("ClientWindow", "adres"))
        self.label_9.setText(_translate("ClientWindow", "value_contact"))
        self.label_7.setText(_translate("ClientWindow", "surname"))
        self.label_5.setText(_translate("ClientWindow", "ID"))
        self.pushButton_2.setText(_translate("ClientWindow", "Вставить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClientWindow = QtWidgets.QMainWindow()
    ui = Ui_ClientWindow()
    ui.setupUi(ClientWindow)
    ClientWindow.show()
    sys.exit(app.exec_())
