from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys
import os
import cv2
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\client_table")
import client
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\order_table")
import order
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\product_table")
import product
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\suppiler_table")
import supplier
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\warehouse_table")
import warehouse
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\select_table")
import select
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\requset_table")
import request
sys.path.append(r"C:\Users\Nike\Desktop\Scripts\Python\pgsql\bd")
import main_bd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 250, 171, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_window)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 310, 171, 41))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.clear_table)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 310, 135, 41))
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_3.clicked.connect(self.image_open)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(110, 40, 256, 192))
        self.listView.setObjectName("listView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        iterable = ["Client", "Order", "Product", "Warehouse", "Supplier", "Request"]
        model = QtCore.QStringListModel()
        model.setStringList(iterable)
        self.listView.setModel(model)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def image_open(self):
        img = cv2.imread(r'C:\Users\Nike\Desktop\Scripts\Python\pgsql\gui\erd\image_erd.jpg')
        cv2.imshow("ERD", img)
        cv2.waitKey(0)

    def clear_table(self):
        if str(self.listView.currentIndex().data()) == "Client":
            main_bd.clear_table_main_bd(self, "client")
        elif str(self.listView.currentIndex().data()) == "Order":
            main_bd.clear_table_main_bd(self, "orders")
        elif str(self.listView.currentIndex().data()) == "Product":
            main_bd.clear_table_main_bd(self, "product")
        elif str(self.listView.currentIndex().data()) == "Warehouse":
            main_bd.clear_table_main_bd(self, "warehouse")
        elif str(self.listView.currentIndex().data()) == "Supplier":
            main_bd.clear_table_main_bd(self, "supplier")

    def open_window(self):
        def check(x):
            match x:
                case "Client":
                    self.send_window = client.QtWidgets.QMainWindow()
                    ui = client.Ui_ClientWindow()
                    

                case "Order":
                    self.send_window = order.QtWidgets.QMainWindow()
                    ui = order.Ui_OrderWindow()


                case "Product":
                    self.send_window = product.QtWidgets.QMainWindow()
                    ui = product.Ui_ProductWindow()


                case "Warehouse":
                    self.send_window = warehouse.QtWidgets.QMainWindow()
                    ui = warehouse.Ui_WarehouseWindow()


                case "Supplier":
                    self.send_window = supplier.QtWidgets.QMainWindow()
                    ui = supplier.Ui_SupplierWindow()
                
                case "Request":
                    self.send_window = request.QtWidgets.QMainWindow()
                    ui = request.Ui_MainWindow()

            ui.setupUi(self.send_window)
            self.send_window.show()

        check(self.listView.currentIndex().data())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Перейти"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить таблицу"))
        self.pushButton_3.setText(_translate("MainWindow", "Таблица ERD Info"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
