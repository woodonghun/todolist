from PySide2.QtWidgets import QDialog, QWidget, QPushButton, QLabel, QLineEdit

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
        funtion.update_todo(self)

        dates = self.content_chunk[funtion.setting.number][2]
        title = self.content_chunk[funtion.setting.number][0]
        contents = self.content_chunk[funtion.setting.number][1]

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
        self.edt_title.setText(title)
        self.edt_title.move(10, 90)

        self.edt_contents = QLineEdit(self.dialog)
        self.edt_contents.setText(contents)
        self.edt_contents.move(10, 110)

        self.label_time = QLabel(self.dialog)
        self.label_time.setText(dates)
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
        number = widget.funtion.Function.setting.number
        txt = open("C:/woo_project/todolist/widget/content", 'r')
        title = self.edt_title.text()
        contents = self.edt_contents.text()
        time = self.label_time.text()

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

        txt = open("C:/woo_project/todolist/widget/content", 'w')
        txt.write(new_text_content)
        txt.close()

        self.dialog_close()

    def dialog_close(self):
        self.dialog.close()
