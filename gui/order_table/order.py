from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\bd")
import main_bd


class Ui_OrderWindow(object):
    def setupUi(self, OrderWindow):
        OrderWindow.setObjectName("OrderWindow")
        OrderWindow.resize(459, 443)
        self.centralwidget = QtWidgets.QWidget(OrderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 0, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setLineWidth(1)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(150, 190, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(1)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(1)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 150, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 340, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: main_bd.add_value_request_order(self, self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5))

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(150, 250, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setLineWidth(1)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 210, 181, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 270, 181, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(1)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 90, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        OrderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OrderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 26))
        self.menubar.setObjectName("menubar")
        OrderWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OrderWindow)
        self.statusbar.setObjectName("statusbar")
        OrderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OrderWindow)
        QtCore.QMetaObject.connectSlotsByName(OrderWindow)

    def retranslateUi(self, OrderWindow):
        _translate = QtCore.QCoreApplication.translate
        OrderWindow.setWindowTitle(_translate("OrderWindow", "OrderWindow"))
        self.label_5.setText(_translate("OrderWindow", "ID"))
        self.label_8.setText(_translate("OrderWindow", "value"))
        self.label_6.setText(_translate("OrderWindow", "id_client FC"))
        self.pushButton_2.setText(_translate("OrderWindow", "Вставить"))
        self.label_9.setText(_translate("OrderWindow", "date"))
        self.label_7.setText(_translate("OrderWindow", "id_product FC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OrderWindow = QtWidgets.QMainWindow()
    ui = Ui_OrderWindow()
    ui.setupUi(OrderWindow)
    OrderWindow.show()
    sys.exit(app.exec_())
