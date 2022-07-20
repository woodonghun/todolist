from PySide2.QtWidgets import QDialog, QWidget, QPushButton, QLabel, QLineEdit

import widget.calendar
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
        btn_date.clicked.connect(self.change)
        btn_date.move(10, 50)

        btn_save = QPushButton(self.dialog)
        btn_save.setText("저장")
        btn_save.clicked.connect(self.btn_clicked)
        btn_save.move(10, 70)

        self.edt_title = QLineEdit(self.dialog)
        self.edt_title.move(10, 90)

        self.edt_contents = QLineEdit(self.dialog)
        self.edt_contents.move(10, 110)

        self.label_time = QLabel(self.dialog)
        self.label_time.setText(self.dates)
        self.label_time.move(10, 130)

        self.dialog.setWindowTitle('todo')
        self.dialog.setGeometry(300, 300, 200, 200)

        self.dialog.exec()

    def change(self):
        txt = open("C:/woo_project/todolist/widget/timedate", 'r')
        self.dates = txt.read()
        txt.close()
        self.label_time.setText(self.dates)

    def btn_clicked(self):
        txt = open("C:/woo_project/todolist/widget/content", 'a')
        title = self.edt_title.text()
        contents = self.edt_contents.text()
        daytime = self.dates
        todolist = title, contents, daytime
        txt.write('\n'.join(todolist)+'\n')
        txt.close()
        self.dialog_close()

    def dialog_close(self):
        self.dialog.close()


