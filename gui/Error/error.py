from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorWindow(object):
    def setupUi(self, ErrorWindow):
        ErrorWindow.setObjectName("ErrorWindow")
        ErrorWindow.resize(321, 265)
        self.centralwidget = QtWidgets.QWidget(ErrorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 10, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        ErrorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ErrorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 26))
        self.menubar.setObjectName("menubar")
        ErrorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ErrorWindow)
        self.statusbar.setObjectName("statusbar")
        ErrorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ErrorWindow)
        QtCore.QMetaObject.connectSlotsByName(ErrorWindow)

    def retranslateUi(self, ErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        ErrorWindow.setWindowTitle(_translate("ErrorWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ErrorWindow = QtWidgets.QMainWindow()
    ui = Ui_ErrorWindow()
    ui.setupUi(ErrorWindow)
    ErrorWindow.show()
    sys.exit(app.exec_())
