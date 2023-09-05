# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database.notes import create_new_note, find_one_note, update_note_by_id


class Ui_main_editor(object):
    def setupUi(self, main_editor):
        main_editor.setObjectName("main_editor")
        main_editor.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(main_editor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_export = QtWidgets.QPushButton(self.centralwidget)
        self.button_export.setObjectName("button_export")
        self.verticalLayout.addWidget(self.button_export)
        self.input_title = QtWidgets.QLineEdit(self.centralwidget)
        self.input_title.setObjectName("input_title")
        self.verticalLayout.addWidget(self.input_title)
        self.input_text_area = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_text_area.setObjectName("input_text_area")
        self.verticalLayout.addWidget(self.input_text_area)
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setObjectName("button_save")
        self.verticalLayout.addWidget(self.button_save)
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setObjectName("button_back")
        self.verticalLayout.addWidget(self.button_back)
        main_editor.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_editor)
        QtCore.QMetaObject.connectSlotsByName(main_editor)

        # Event
        self.button_export.clicked.connect(self.export_note)
        self.button_save.clicked.connect(self.check_status)
        self.button_back.clicked.connect(self.open_ui_notelist)


        # this ui
        self.this_ui = main_editor

    def retranslateUi(self, main_editor):
        _translate = QtCore.QCoreApplication.translate
        main_editor.setWindowTitle(_translate("main_editor", "Prinost - Editor"))
        self.button_export.setText(_translate("main_editor", "Export"))
        self.input_title.setPlaceholderText(_translate("main_editor", "Title"))
        self.input_text_area.setPlaceholderText(_translate("main_editor", "Type anything you want"))
        self.button_save.setText(_translate("main_editor", "Save a note"))
        self.button_back.setText(_translate("main_editor", "Back"))

    def set_previous_ui(self, previous_ui):
        self.previous_ui = previous_ui

    def set_user(self, user = None,status = "create", note = None):
        self.user = user
        self.status = status
        if self.status != "create":
            self.note = note
            note = find_one_note(self.note)
            self.input_title.setText(note["title"])
            self.input_text_area.setPlainText(note["content"])

    # Action
    def open_ui_notelist(self):
        self.previous_ui.get_some_note()
        self.previous_ui.this_ui.show()
        self.this_ui.hide()

    def check_status(self):
        if self.status == "create":
            self.create_note()
            self.show_info("Create new note","You have created a new note.")
        else:
            self.update_note()
            self.show_info("Update note", "You have updated a note.")
        self.open_ui_notelist()

    def create_note(self):
        title = self.input_title.text()
        content = self.input_text_area.toPlainText()
        now = datetime.datetime.utcnow()
        created_date = datetime.datetime(now.year,now.month,now.day,now.hour,now.minute)
        create_new_note(self.user["_id"],title,content,created_date)

    def update_note(self):
        title = self.input_title.text()
        content = self.input_text_area.toPlainText()
        now = datetime.datetime.utcnow()
        updated_date = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute)
        update_note_by_id(self.note,title,content,updated_date)

    def export_note(self):
        title = self.input_title.text()
        if title != "":
            title = "file/" + title + ".txt"
            content = self.input_text_area.toPlainText()
            with open(title, "w", encoding="utf8") as f:
                f.write(content)
            self.show_info("Export file","Export note to a file completed.")
        else:
            self.show_warn("Warning","Please, enter title")


    # Pop up
    def show_info(self,title,message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
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
#     app = QtWidgets.QApplication(sys.argv)
#     main_editor = QtWidgets.QMainWindow()
#     ui = Ui_main_editor()
#     ui.setupUi(main_editor)
#     main_editor.show()
#     sys.exit(app.exec_())
