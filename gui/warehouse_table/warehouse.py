from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\bd")
import main_bd

class Ui_WarehouseWindow(object):
    def setupUi(self, WarehouseWindow):
        WarehouseWindow.setObjectName("WarehouseWindow")
        WarehouseWindow.resize(430, 414)
        self.centralwidget = QtWidgets.QWidget(WarehouseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 180, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 210, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(1)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 300, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: main_bd.add_value_request_warehouse(self, self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4))


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 120, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 240, 181, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        WarehouseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WarehouseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 26))
        self.menubar.setObjectName("menubar")
        WarehouseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WarehouseWindow)
        self.statusbar.setObjectName("statusbar")
        WarehouseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WarehouseWindow)
        QtCore.QMetaObject.connectSlotsByName(WarehouseWindow)

    def retranslateUi(self, WarehouseWindow):
        _translate = QtCore.QCoreApplication.translate
        WarehouseWindow.setWindowTitle(_translate("WarehouseWindow", "WarehouseWindow"))
        self.label_2.setText(_translate("WarehouseWindow", "id_product FC"))
        self.label_3.setText(_translate("WarehouseWindow", "total"))
        self.label_4.setText(_translate("WarehouseWindow", "delivery_date_number"))
        self.label.setText(_translate("WarehouseWindow", "ID"))
        self.pushButton.setText(_translate("WarehouseWindow", "Вставить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WarehouseWindow = QtWidgets.QMainWindow()
    ui = Ui_WarehouseWindow()
    ui.setupUi(WarehouseWindow)
    WarehouseWindow.show()
    sys.exit(app.exec_())
