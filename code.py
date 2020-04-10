from PyQt5 import QtCore, QtGui, QtWidgets
import ipaddress
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(286, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 120, 251, 261))
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):
        ip = self.lineEdit.text()
        ipi = ipaddress.ip_interface(ip)

        print("Address", ipi.ip)
        print("Mask", ipi.netmask)
        print("Network", str(ipi.network).split('/')[0])
        print("Broadcast", ipi.network.broadcast_address)
            #IP ARALIĞI GİRİLMELİ.
        self.textEdit.append("Adres:{}\nMask:{}\nNetwork:{}\nBroadcast:{}\n"
                             .format(ipi.ip,ipi.netmask,str(ipi.network).split('/')[0],ipi.network.broadcast_address))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Calc"))
        self.label.setText(_translate("MainWindow", "ip adresi: "))
        self.pushButton.setText(_translate("MainWindow", "hesapla"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
