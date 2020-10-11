# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial-3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!




from PyQt5 import QtCore, QtGui, QtWidgets
from trial1 import Ui_MainWindow
from trial4 import  Ui_exitDialog
import logo_rc  

class Ui_StartDialog(object):
    def setupUi(self, StartDialog):
        StartDialog.setObjectName("StartDialog")
        StartDialog.resize(850, 600)
        StartDialog.setStyleSheet("background-color: rgb(179, 224, 242);")
        self.gridLayout = QtWidgets.QGridLayout(StartDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.imagelabel = QtWidgets.QLabel(StartDialog)
        self.imagelabel.setText("")
        self.imagelabel.setPixmap(QtGui.QPixmap(":/images/logo-check-1.JPG"))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setObjectName("imagelabel")
        self.verticalLayout_2.addWidget(self.imagelabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 20, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(StartDialog)
        self.pushButton_2.setStyleSheet("background-color: #8c8880;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.exit_button_handler)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(StartDialog)
        self.pushButton.setStyleSheet("background-color: rgb(113, 177, 217);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start_button_handler)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 20)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(StartDialog)
        QtCore.QMetaObject.connectSlotsByName(StartDialog)

    def retranslateUi(self, StartDialog):
        _translate = QtCore.QCoreApplication.translate
        StartDialog.setWindowTitle(_translate("StartDialog", "Waste Segregator"))
        self.pushButton_2.setText(_translate("StartDialog", "EXIT"))
        self.pushButton.setText(_translate("StartDialog", "START"))
    
    def exit_button_handler(self):
        print("exit button pressed")
        exitDialog = QtWidgets.QDialog()
        ui = Ui_exitDialog()
        ui.setupUi(exitDialog)
        exitDialog.show()
        exitDialog.exec_()
        

    def start_button_handler(self):
        print("start button clicked")
        self.StartDialog = QtWidgets.QDialog()
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show() #how to execute the main window
        self.StartDialog.accept() #returns 2 and closes the dialog #added self
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartDialog = QtWidgets.QDialog()
    ui = Ui_StartDialog()
    ui.setupUi(StartDialog)
    StartDialog.show()
    sys.exit(app.exec_())



    
