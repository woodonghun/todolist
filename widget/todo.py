from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit

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
        self.todo()

        date = widget.calendar.Calendar

        btn_date = QPushButton(self.dialog)
        btn_date.setText("날짜시간 설정")
        btn_date.clicked.connect(date)      # 캘린더, 시간 모듈로 이동
        btn_date.clicked.connect(self.Time_change)
        btn_date.move(150, 180)

        btn_save = QPushButton(self.dialog)
        btn_save.setText("저장")
        btn_save.clicked.connect(self.btn_clicked)
        btn_save.move(250, 180)

        self.edt_title = QLineEdit(self.dialog)
        self.edt_title.setText(self.title)
        self.edt_title.setGeometry(35, 10, 300, 30)

        self.edt_contents = QPlainTextEdit(self.dialog)     # QPlainTextEdit은 QLineEdit과 다르게 스타일은 바꿀수 없지만 줄은 바꿀 수 있다.
        self.edt_contents.setPlainText(self.contents)        # ui 이쁘게 안하면 더 많이 사용할 것 같음
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

        self.dialog.setWindowTitle('할일 추가')
        self.dialog.setGeometry(300, 350, 350, 230)

        self.dialog.exec()

    # 시간 설정
    def Time_change(self):
        txt = open("C:/woo_project/todolist/widget/timedate.txt", 'r')
        self.dates = txt.read()
        txt.close()
        self.label_time_set.setText(self.dates)

    # 저장 버튼 클릭
    def btn_clicked(self):
        if self.edt_title.text() != '':     # 제목에 빈칸이 아닐 때
            txt = open("C:/woo_project/todolist/widget/content.txt", 'a')
            title = self.edt_title.text()
            contents = self.edt_contents.toPlainText()
            daytime = self.dates
            todolist = title, contents, daytime
            txt.write('\n'.join(todolist)+'\n')
            txt.close()
            self.dialog_close()
        else:       # 제목에 빈칸일 때 메세지 박스 출력, 내용 없이 제목만 쓸 수 있을거라 생각해서 제목만~
            signBox = QMessageBox()
            signBox.setWindowTitle("Warning")
            signBox.setText('제목을 입력하세요')

            signBox.setIcon(QMessageBox.Information)
            signBox.setStandardButtons(QMessageBox.Ok)
            signBox.exec_()

    def dialog_close(self):
        self.dialog.close()

    def todo(self):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간

        self.dates = nowDatetime
        self.title = ''
        self.contents = ''


class Edit(Todo):
    def __init__(self):
        super().__init__()

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

    def todo(self):
        funtion = widget.funtion.Function
        funtion.update_todo(self, 3)

        self.title = self.content_chunk[funtion.setting.number][0]
        self.contents = self.content_chunk[funtion.setting.number][1]
        self.dates = self.content_chunk[funtion.setting.number][2]
        print(self.title)