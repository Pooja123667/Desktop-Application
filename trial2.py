# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial-2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_SuccessDialog(object):
    def setupUi(self, SuccessDialog):
        SuccessDialog.setObjectName("SuccessDialog")
        SuccessDialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo-check-1.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SuccessDialog.setWindowIcon(icon)
        SuccessDialog.setStyleSheet("background-color: #B3E0F2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SuccessDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SuccessDialog)
        self.label.setStyleSheet("font: 12pt \"Calibri\";\n"
"color: #000000;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(SuccessDialog)
        self.pushButton.setStyleSheet("font: 75 12pt \"Calibri\";\n"
"background-color: rgb(113, 177, 217);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ok_button_handler)#############
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(SuccessDialog)
        QtCore.QMetaObject.connectSlotsByName(SuccessDialog)

    def retranslateUi(self, SuccessDialog):
        _translate = QtCore.QCoreApplication.translate
        SuccessDialog.setWindowTitle(_translate("SuccessDialog", "Waste Segregator"))
        self.label.setText(_translate("SuccessDialog", "Waste segregated successfully!\n"
"Check results section to know more"))
        self.pushButton.setText(_translate("SuccessDialog", "OK"))

    def ok_button_handler(self):
            #app = QtWidgets.QApplication(sys.argv)
            #QtCore.QCoreApplication.instance().quit() #i dont want to quit the application, only the dialog
            SuccessDialog = QtWidgets.QDialog()
            print("Sucess dialog")
            QtWidgets.QDialog().close()
            #SuccessDialog.done(1)
            #SuccessDialog.exit() #not closing
            #takes integer argument'''
           
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SuccessDialog = QtWidgets.QDialog()
    ui = Ui_SuccessDialog() 
    ui.setupUi(SuccessDialog)
    SuccessDialog.show()
    sys.exit(app.exec_())
