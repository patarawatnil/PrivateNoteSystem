# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from database.notes import delete_note_by_id, find_from_search
from editor import Ui_main_editor


class Ui_main_dashboard(object):

    def setupUi(self, main_dashboard):
        main_dashboard.setObjectName("main_dashboard")
        main_dashboard.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(main_dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_create = QtWidgets.QPushButton(self.centralwidget)
        self.button_create.setObjectName("button_create")
        self.gridLayout.addWidget(self.button_create, 2, 0, 1, 2)
        self.button_logout = QtWidgets.QPushButton(self.centralwidget)
        self.button_logout.setObjectName("button_logout")
        self.gridLayout.addWidget(self.button_logout, 0, 1, 1, 1)
        self.input_keyword = QtWidgets.QLineEdit(self.centralwidget)
        self.input_keyword.setObjectName("input_keyword")
        self.gridLayout.addWidget(self.input_keyword, 0, 2, 1, 2)
        self.label_welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_welcome.setObjectName("label_welcome")
        self.gridLayout.addWidget(self.label_welcome, 0, 0, 1, 1)
        self.combo_time = QtWidgets.QComboBox(self.centralwidget)
        self.combo_time.setObjectName("combo_time")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.combo_time.addItem("")
        self.gridLayout.addWidget(self.combo_time, 2, 2, 1, 3)
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setObjectName("button_search")
        self.gridLayout.addWidget(self.button_search, 0, 4, 1, 1)
        self.table_note_list = QtWidgets.QTableWidget(self.centralwidget)
        self.table_note_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_note_list.setObjectName("table_note_list")
        self.table_note_list.setColumnCount(5)
        self.table_note_list.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_note_list.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_note_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_note_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_note_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_note_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_note_list.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.table_note_list, 3, 0, 1, 5)
        main_dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_dashboard)
        QtCore.QMetaObject.connectSlotsByName(main_dashboard)

        # Event
        self.button_logout.clicked.connect(self.logout)
        self.button_create.clicked.connect(self.open_ui_editor)
        self.button_search.clicked.connect(self.search_note)

        self.table_note_list.cellClicked.connect(self.clickded_cell)

        self.combo_time.currentIndexChanged.connect(self.change_time)

        # this ui
        self.this_ui = main_dashboard

    def retranslateUi(self, main_dashboard):
        _translate = QtCore.QCoreApplication.translate
        main_dashboard.setWindowTitle(_translate("main_dashboard", "Prinost"))
        self.button_create.setText(_translate("main_dashboard", "Create new note"))
        self.button_logout.setText(_translate("main_dashboard", "Log out"))
        self.input_keyword.setPlaceholderText(_translate("main_dashboard", "Keyword"))
        self.label_welcome.setText(_translate("main_dashboard", "Welcome, "))
        self.combo_time.setItemText(0, _translate("main_dashboard", "Any time"))
        self.combo_time.setItemText(1, _translate("main_dashboard", "Past 24 hours"))
        self.combo_time.setItemText(2, _translate("main_dashboard", "Past week"))
        self.combo_time.setItemText(3, _translate("main_dashboard", "Past month"))
        self.combo_time.setItemText(4, _translate("main_dashboard", "Past year"))
        self.button_search.setText(_translate("main_dashboard", "Search"))
        item = self.table_note_list.verticalHeaderItem(0)
        item.setText(_translate("main_dashboard", "1"))
        item = self.table_note_list.horizontalHeaderItem(0)
        item.setText(_translate("main_dashboard", "Title"))
        item = self.table_note_list.horizontalHeaderItem(1)
        item.setText(_translate("main_dashboard", "Created date"))
        item = self.table_note_list.horizontalHeaderItem(2)
        item.setText(_translate("main_dashboard", "Updated date"))
        item = self.table_note_list.horizontalHeaderItem(3)
        item.setText(_translate("main_dashboard", "Action update"))
        item = self.table_note_list.horizontalHeaderItem(4)
        item.setText(_translate("main_dashboard", "Action delete"))

    def set_previous_ui(self, previous_ui):
        self.previous_ui = previous_ui

    def set_user(self, user):
        self.user = user
        self.label_welcome.setText("Welcome, " + self.user["username"])
        self.search_keyword = ""
        self.search_from = datetime.datetime.min

    # Action
    def logout(self):
        self.user = None
        self.previous_ui.show()
        self.this_ui.hide()

    def open_ui_editor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_main_editor()
        self.ui.setupUi(self.window)
        self.ui.set_previous_ui(self)
        self.ui.set_user(user=self.user)
        self.window.show()
        self.this_ui.hide()

    def get_all_note(self):
        self.render_note_list(find_from_search(self.user["_id"]))

    def get_some_note(self):
        try:
            self.render_note_list(find_from_search(self.user["_id"], self.search_keyword, self.search_from))
        except:
            self.table_note_list.setRowCount(0)

    def render_note_list(self, note_list):
        self.table_note_list.setRowCount(0)
        self.user_note = []
        num_row = note_list.count()
        self.table_note_list.setRowCount(num_row)
        for row, n in enumerate(note_list):
            self.table_note_list.setItem(row, 0, QtWidgets.QTableWidgetItem(n["title"]))
            self.table_note_list.setItem(row, 1,
                                         QtWidgets.QTableWidgetItem(n["createdDate"].strftime("%d/%m/%Y %H:%M")))
            self.table_note_list.setItem(row, 2,
                                         QtWidgets.QTableWidgetItem(n["updatedDate"].strftime("%d/%m/%Y %H:%M")))
            self.table_note_list.setItem(row, 3, QtWidgets.QTableWidgetItem("Edit"))
            self.table_note_list.setItem(row, 4, QtWidgets.QTableWidgetItem("Delete"))
            self.user_note.append(n["_id"])

    def clickded_cell(self, row, col):
        user_note = self.user_note[row]
        if col == 3:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_main_editor()
            self.ui.setupUi(self.window)
            self.ui.set_previous_ui(self)
            self.ui.set_user(user=self.user, status="update", note=user_note)
            self.window.show()
            self.this_ui.hide()
        elif col == 4:
            need_to__delete = self.show_question("Delete note", "Do you want to delete this note ?",
                                                 "This action can not be undone.")
            if need_to__delete == QMessageBox.Yes:
                delete_note_by_id(user_note)
                self.show_info("Delete note", "Delete a note completed.")
                self.get_some_note()

    def search_note(self):
        self.search_keyword = self.input_keyword.text().strip()
        self.get_some_note()

    def change_time(self):
        now = datetime.datetime.utcnow()
        choice = self.combo_time.currentIndex()
        if choice == 1:
            self.search_from = now - datetime.timedelta(hours=24)
        elif choice == 2:
            self.search_from = now - datetime.timedelta(weeks=1)
        elif choice == 3:
            self.search_from = now - datetime.timedelta(days=30)
        elif choice == 4:
            self.search_from = now - datetime.timedelta(days=365)
        else:
            self.search_from = datetime.datetime.min
        self.get_some_note()

    # Pop up
    def show_question(self, title, message, description=""):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setInformativeText(description)
        return  msg.exec_()

    def show_info(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     main_dashboard = QtWidgets.QMainWindow()
#     ui = Ui_main_dashboard()
#     ui.setupUi(main_dashboard)
#     main_dashboard.show()
#     sys.exit(app.exec_())
