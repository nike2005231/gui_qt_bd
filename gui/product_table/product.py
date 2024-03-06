from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\bd")
import main_bd

class Ui_ProductWindow(object):
    def setupUi(self, ProductWindow):
        ProductWindow.setObjectName("ProductWindow")
        ProductWindow.resize(429, 412)
        self.centralwidget = QtWidgets.QWidget(ProductWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 280, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: main_bd.add_value_request_product(self, self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4))


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 100, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 160, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 220, 181, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 190, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLineWidth(1)
        self.label_4.setObjectName("label_4")
        ProductWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ProductWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 26))
        self.menubar.setObjectName("menubar")
        ProductWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ProductWindow)
        self.statusbar.setObjectName("statusbar")
        ProductWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProductWindow)
        QtCore.QMetaObject.connectSlotsByName(ProductWindow)

    def retranslateUi(self, ProductWindow):
        _translate = QtCore.QCoreApplication.translate
        ProductWindow.setWindowTitle(_translate("ProductWindow", "ProductWindow"))
        self.pushButton.setText(_translate("ProductWindow", "Вставить"))
        self.label.setText(_translate("ProductWindow", "ID"))
        self.label_2.setText(_translate("ProductWindow", "name_product"))
        self.label_3.setText(_translate("ProductWindow", "price_product"))
        self.label_4.setText(_translate("ProductWindow", "description_product"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductWindow = QtWidgets.QMainWindow()
    ui = Ui_ProductWindow()
    ui.setupUi(ProductWindow)
    ProductWindow.show()
    sys.exit(app.exec_())
