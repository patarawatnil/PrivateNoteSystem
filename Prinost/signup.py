# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import re

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database.users import is_user_exists, is_email_exists, create_new_user_account


class Ui_form_signup(object):

    def __init__(self):
        self.is_user_ok = False
        self.is_email_ok = False
        self.is_pass_ok = False
        self.is_pass_confirm = False
        self.username = ""
        self.email = ""
        self.password = ""

    def setupUi(self, form_signup):
        form_signup.setObjectName("form_signup")
        form_signup.resize(240, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_signup.sizePolicy().hasHeightForWidth())
        form_signup.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(form_signup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 221, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_username.setObjectName("input_username")
        self.verticalLayout.addWidget(self.input_username)
        self.label_warn_user = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_warn_user.setObjectName("label_warn_user")
        self.verticalLayout.addWidget(self.label_warn_user)
        self.input_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_email.setObjectName("input_email")
        self.verticalLayout.addWidget(self.input_email)
        self.label_warn_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_warn_email.setObjectName("label_warn_email")
        self.verticalLayout.addWidget(self.label_warn_email)
        self.input_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_pass.setObjectName("input_pass")
        self.verticalLayout.addWidget(self.input_pass)
        self.label_warn_pass = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_warn_pass.setObjectName("label_warn_pass")
        self.verticalLayout.addWidget(self.label_warn_pass)
        self.input_confirm_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_confirm_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_confirm_pass.setObjectName("input_confirm_pass")
        self.verticalLayout.addWidget(self.input_confirm_pass)
        self.label_warn_conp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_warn_conp.setObjectName("label_warn_conp")
        self.verticalLayout.addWidget(self.label_warn_conp)
        self.button_signup = QtWidgets.QPushButton(form_signup)
        self.button_signup.setGeometry(QtCore.QRect(30, 260, 181, 23))
        self.button_signup.setObjectName("button_signup")
        self.button_back = QtWidgets.QPushButton(form_signup)
        self.button_back.setGeometry(QtCore.QRect(30, 290, 181, 23))
        self.button_back.setObjectName("button_back")
        self.label_discription = QtWidgets.QLabel(form_signup)
        self.label_discription.setGeometry(QtCore.QRect(30, 10, 181, 16))
        self.label_discription.setObjectName("label_discription")

        # Event
        self.button_back.clicked.connect(self.open_ui_login)
        self.button_signup.clicked.connect(self.create_new_account)

        self.input_username.editingFinished.connect(self.check_user)
        self.input_email.editingFinished.connect(self.check_email)

        self.input_pass.textChanged.connect(self.check_pass)
        self.input_confirm_pass.textChanged.connect(self.check_confirm_pass)

        self.retranslateUi(form_signup)
        QtCore.QMetaObject.connectSlotsByName(form_signup)

        # this ui
        self.this_ui = form_signup

    def retranslateUi(self, form_signup):
        _translate = QtCore.QCoreApplication.translate
        form_signup.setWindowTitle(_translate("form_signup", "Prinost - Sign up"))
        self.input_username.setPlaceholderText(_translate("form_signup", "Username"))
        self.label_warn_user.setText(_translate("form_signup", "Enter username"))
        self.input_email.setPlaceholderText(_translate("form_signup", "E-mail"))
        self.label_warn_email.setText(_translate("form_signup", "Enter email"))
        self.input_pass.setPlaceholderText(_translate("form_signup", "Password"))
        self.label_warn_pass.setText(_translate("form_signup", "Password must be at least 6 characters"))
        self.input_confirm_pass.setPlaceholderText(_translate("form_signup", "Confirm Password"))
        self.label_warn_conp.setText(_translate("form_signup", "Re-enter password"))
        self.button_signup.setText(_translate("form_signup", "Create new account"))
        self.button_back.setText(_translate("form_signup", "Back"))
        self.label_discription.setText(_translate("form_signup", "Please, fill in every field"))

    def set_previous_ui(self, previous_ui):
        self.previous_ui = previous_ui

    # Action
    def open_ui_login(self):
        self.previous_ui.show()
        self.this_ui.hide()

    def check_user(self):
        new_user = self.input_username.text().strip()
        if not is_user_exists(new_user):
            self.username = new_user
            self.is_user_ok = True
            self.label_warn_user.setText("Username OK")
        else:
            self.is_user_ok = False
            self.username = ""
            self.label_warn_user.setText("This username already exists")

    def check_email(self):
        new_email = self.input_email.text().strip()
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, new_email)):
            if not is_email_exists(new_email):
                self.email = new_email
                self.is_email_ok = True
                self.label_warn_email.setText("Email OK")
            else:
                self.is_email_ok = False
                self.email = ""
                self.label_warn_email.setText("This email already exists")
        else:
            self.is_email_ok = False
            self.email = ""
            self.label_warn_email.setText("Invalid Email")

    def check_pass(self):
        pass_length = len(self.input_pass.text())
        if pass_length >= 6:
            self.is_pass_ok = True
            self.label_warn_pass.setText("Password OK")
        else:
            self.is_pass_ok = False
            self.label_warn_pass.setText("Password must be at least 6 characters")

    def check_confirm_pass(self):
        password = self.input_pass.text()
        con_pass = self.input_confirm_pass.text()
        if password == con_pass:
            self.password = password
            self.is_pass_confirm = True
            self.label_warn_conp.setText("Confirm password OK")
        else:
            self.is_pass_confirm = False
            self.password = ""
            self.label_warn_conp.setText("Please, confirm your password")

    def create_new_account(self):
        if self.is_user_ok and self.is_email_ok and self.is_pass_ok and self.is_pass_confirm:
            create_new_user_account(self.username, self.email, self.password)
            self.show_info()
            self.open_ui_login()
        else:
            self.show_warn("Incomplete field", "Please, fill in the empty field or complete thier condition.")

    # Pop up
    def show_info(self):
        msg = QMessageBox()
        msg.setWindowTitle("Create new account")
        msg.setText("You have created a new account.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def show_warn(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     form_signup = QtWidgets.QWidget()
#     ui = Ui_form_signup()
#     ui.setupUi(form_signup)
#     form_signup.show()
#     sys.exit(app.exec_())
