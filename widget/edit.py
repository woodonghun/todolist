from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit

import widget.calendar
import widget.funtion
import widget.main
import widget.funtion


class Edit(QWidget):

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()
        self.dialog_close()

    def initUI(self):

        funtion = widget.funtion.Function
        funtion.update_todo(self, 3)

        dates = self.content_chunk[funtion.setting.number][2]
        title = self.content_chunk[funtion.setting.number][0]
        contents = self.content_chunk[funtion.setting.number][1]

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
        self.edt_title.setText(title)
        self.edt_title.setGeometry(35, 10, 300, 30)

        self.edt_contents = QPlainTextEdit(self.dialog)
        self.edt_contents.setPlainText(contents)
        self.edt_contents.setGeometry(35, 50, 300, 90)

        self.label_time_set = QLabel(self.dialog)
        self.label_time_set.setText(dates)
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
        self.dialog.setGeometry(300, 350, 350, 300)

        self.dialog.exec()

    def Time_change(self):
        txt = open("C:/woo_project/todolist/widget/timedate.txt", 'r')
        self.dates = txt.read()
        txt.close()
        self.label_time_set.setText(self.dates)

    def btn_clicked(self):
        if self.edt_title.text() != '':
            number = widget.funtion.Function.setting.number
            txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
            title = self.edt_title.text()
            contents = self.edt_contents.toPlainText()
            time = self.label_time_set.text()

            new_text_content = ''
            lines = txt.readlines()
            for i, l in enumerate(lines):
                if i == number * 3:
                    new_string = title
                elif i == number * 3 + 2:
                    new_string = time
                elif i == number * 3 + 1:
                    new_string = contents
                else:
                    new_string = l.strip()
                if new_string:
                    new_text_content += new_string + '\n'
                else:
                    new_text_content += '\n'
            txt.close()

            txt = open("C:/woo_project/todolist/widget/content.txt", 'w')
            txt.write(new_text_content)
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
