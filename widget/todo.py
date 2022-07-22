from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

import widget.calendar
import widget.main
import datetime


class Todo(QWidget):

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()
        self.dialog_close()

    def initUI(self):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간
        self.dates = nowDatetime

        date = widget.calendar.Calendar

        btn_date = QPushButton(self.dialog)
        btn_date.setText("날짜시간 설정")
        btn_date.clicked.connect(date)
        btn_date.clicked.connect(self.Time_change)
        btn_date.move(150, 180)

        btn_save = QPushButton(self.dialog)
        btn_save.setText("저장")
        btn_save.clicked.connect(self.btn_clicked)
        btn_save.move(250, 180)

        self.edt_title = QLineEdit(self.dialog)
        self.edt_title.setGeometry(35, 10, 300, 30)

        self.edt_contents = QLineEdit(self.dialog)
        self.edt_contents.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.edt_contents.setGeometry(35, 50, 300, 90)

        self.label_time_set = QLabel(self.dialog)
        self.label_time_set.setText(self.dates)
        self.label_time_set.setGeometry(35, 140, 300, 30)

        self.label_title = QLabel(self.dialog)
        self.label_title.setText('제목')
        self.label_title.move(10, 20)

        self.label_contents = QLabel(self.dialog)
        self.label_contents.setText('내용')
        self.label_contents.move(10, 75)

        self.label_time = QLabel(self.dialog)
        self.label_time.setText('일시')
        self.label_time.move(10, 150)

        self.dialog.setWindowTitle('todo')
        self.dialog.setGeometry(300, 350, 350, 250)

        self.dialog.exec()

    def Time_change(self):
        txt = open("C:/woo_project/todolist/widget/timedate.txt", 'r')
        self.dates = txt.read()
        txt.close()
        self.label_time_set.setText(self.dates)

    def btn_clicked(self):
        if self.edt_title.text() != '':
            txt = open("C:/woo_project/todolist/widget/content.txt", 'a')
            title = self.edt_title.text()
            contents = self.edt_contents.text()
            daytime = self.dates
            todolist = title, contents, daytime
            txt.write('\n'.join(todolist)+'\n')
            txt.close()
            self.dialog_close()
        else:
            signBox = QMessageBox()
            signBox.setWindowTitle("Warning")
            signBox.setText('제목을 입력하세요')

            signBox.setIcon(QMessageBox.Information)
            signBox.setStandardButtons(QMessageBox.Ok)
            signBox.exec_()

    def dialog_close(self):
        self.dialog.close()