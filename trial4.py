# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trial-4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_exitDialog(object):
    def setupUi(self, exitDialog):
        exitDialog.setObjectName("exitDialog")
        exitDialog.resize(400, 300)
        exitDialog.setStyleSheet("background-color: rgb(179, 224, 242);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(exitDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(exitDialog)
        self.label.setStyleSheet("font: 12pt \"Calibri\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelpushButton = QtWidgets.QPushButton(exitDialog)
        self.cancelpushButton.setStyleSheet("background-color: #8c8880;\n"
"color: rgb(255, 255, 255);")
        self.cancelpushButton.setObjectName("cancelpushButton")
        self.cancelpushButton.clicked.connect(self.cancel_button_handler)
        self.horizontalLayout.addWidget(self.cancelpushButton)
        self.exitpushButton = QtWidgets.QPushButton(exitDialog)
        self.exitpushButton.setStyleSheet("background-color: rgb(113, 177, 217);\n"
"color: rgb(255, 255, 255);")
        self.exitpushButton.setObjectName("exitpushButton")
        self.exitpushButton.clicked.connect(self.exit_button_handler)
        self.horizontalLayout.addWidget(self.exitpushButton)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(exitDialog)
        QtCore.QMetaObject.connectSlotsByName(exitDialog)

    def retranslateUi(self, exitDialog):
        _translate = QtCore.QCoreApplication.translate
        exitDialog.setWindowTitle(_translate("exitDialog", "Dialog"))
        self.label.setText(_translate("exitDialog", "Are you sure you want\n"
" to exit the Application?"))
        self.cancelpushButton.setText(_translate("exitDialog", "Cancel"))
        self.exitpushButton.setText(_translate("exitDialog", "EXIT"))

    def cancel_button_handler(self):
            print("cancel button pressed")
            exitDialog = QtWidgets.QDialog()
            exitDialog.reject()


    def exit_button_handler(self):
            import sys
            app = QtWidgets.QApplication(sys.argv)
            print("exit button pressed")
            exitDialog = QtWidgets.QDialog()
            exitDialog.accept()
            sys.exit(app.quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exitDialog = QtWidgets.QDialog()
    ui = Ui_exitDialog()
    ui.setupUi(exitDialog)
    exitDialog.show()
    sys.exit(app.exec_())
