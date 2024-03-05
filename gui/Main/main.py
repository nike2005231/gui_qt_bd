from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sys
import os
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

        iterable = ["Client", "Order", "Product", "Warehouse", "Supplier"]
        model = QtCore.QStringListModel()
        model.setStringList(iterable)
        self.listView.setModel(model)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def open_window(self):
        print(self.listView.currentIndex().data())
        print(client.__dict__)
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

            ui.setupUi(self.send_window)
            self.send_window.show()

        check(self.listView.currentIndex().data())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Перейти"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
