# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database.users import is_auth
from notelist import Ui_main_dashboard
from signup import Ui_form_signup


class Ui_form_login(object):
    def setupUi(self, form_login):
        form_login.setObjectName("form_login")
        form_login.resize(240, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_login.sizePolicy().hasHeightForWidth())
        form_login.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(form_login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 130, 181, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.form_field = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.form_field.setContentsMargins(0, 0, 0, 0)
        self.form_field.setObjectName("form_field")
        self.input_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_username.setObjectName("input_username")
        self.form_field.addWidget(self.input_username)
        self.input_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.form_field.addWidget(self.input_password)
        self.button_login = QtWidgets.QPushButton(form_login)
        self.button_login.setGeometry(QtCore.QRect(30, 190, 181, 23))
        self.button_login.setObjectName("button_login")
        self.button_signup = QtWidgets.QPushButton(form_login)
        self.button_signup.setGeometry(QtCore.QRect(30, 250, 181, 23))
        self.button_signup.setObjectName("button_signup")
        self.label_title = QtWidgets.QLabel(form_login)
        self.label_title.setGeometry(QtCore.QRect(36, 22, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_title.setFont(font)
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_subtitle = QtWidgets.QLabel(form_login)
        self.label_subtitle.setGeometry(QtCore.QRect(30, 80, 181, 16))
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setObjectName("label_subtitle")
        self.label_signup = QtWidgets.QLabel(form_login)
        self.label_signup.setGeometry(QtCore.QRect(30, 230, 181, 16))
        self.label_signup.setObjectName("label_signup")

        # Event
        self.button_signup.clicked.connect(self.open_ui_signup)
        self.button_login.clicked.connect(self.to_login)

        self.retranslateUi(form_login)
        QtCore.QMetaObject.connectSlotsByName(form_login)

        # this ui
        self.this_ui = form_login

    def retranslateUi(self, form_login):
        _translate = QtCore.QCoreApplication.translate
        form_login.setWindowTitle(_translate("form_login", "Prinost"))
        self.input_username.setPlaceholderText(_translate("form_login", "Username or Email"))
        self.input_password.setPlaceholderText(_translate("form_login", "Password"))
        self.button_login.setText(_translate("form_login", "Log In"))
        self.button_signup.setText(_translate("form_login", "Sign Up"))
        self.label_title.setText(_translate("form_login", "Prinost"))
        self.label_subtitle.setText(_translate("form_login", "Private Note System"))
        self.label_signup.setText(_translate("form_login", "Don\'t have an account ?"))

    # Action
    # Open UI signup
    def open_ui_signup(self):
        self.input_username.clear()
        self.input_password.clear()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_form_signup()
        self.ui.setupUi(self.window)
        self.ui.set_previous_ui(self.this_ui)
        self.window.show()
        self.this_ui.hide()

    def to_login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        authentication, user = is_auth(username, password)
        if authentication and user is not None:
            self.open_ui_notelist(user)
        else:
            self.show_warn("Warning", "The username or password is incorrect.")

    def open_ui_notelist(self, user):
        self.input_username.clear()
        self.input_password.clear()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_main_dashboard()
        self.ui.setupUi(self.window)
        self.ui.set_previous_ui(self.this_ui)
        self.ui.set_user(user)
        self.ui.get_all_note()
        self.window.show()
        self.this_ui.hide()

    def show_warn(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form_login = QtWidgets.QWidget()
    ui = Ui_form_login()
    ui.setupUi(form_login)
    form_login.show()
    sys.exit(app.exec_())
