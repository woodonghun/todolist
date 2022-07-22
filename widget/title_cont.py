from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QWidget, QPushButton, QLabel, QLineEdit

import widget.funtion
class Title_Cont(QWidget):

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()
        self.dialog_close()

    def initUI(self):
        self.update_todo()

        function = widget.funtion.Function
        row = function.setting.number

        function.update_todo(self, 3)

        edt_title = QLabel(self.dialog)
        edt_title.setText(self.content_chunk[row][0])
        edt_title.setStyleSheet('background-color: white;'
                                'border-style: solid;'
                                'border-width: 1px;'
                                'border-color: #111111;')
        edt_title.setGeometry(35, 10, 300, 30)

        edt_contents = QLabel(self.dialog)
        edt_contents.setText(self.content_chunk[row][1])
        edt_contents.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        edt_contents.setWordWrap(True)
        edt_contents.setStyleSheet('background-color: white;'
                                   'border-style: solid;'
                                   'border-width: 1px;'
                                   'border-color: #111111;')
        edt_contents.setGeometry(35, 50, 300, 90)

        label_time_set = QLabel(self.dialog)
        label_time_set.setText(self.content_chunk[row][2])
        label_time_set.setStyleSheet('background-color: white;'
                                     'border-style: solid;'
                                     'border-width: 1px;'
                                     'border-color: #111111;')
        label_time_set.setGeometry(35, 145, 300, 30)

        label_title = QLabel(self.dialog)
        label_title.setText('제목')
        label_title.move(5, 20)

        label_contents = QLabel(self.dialog)
        label_contents.setText('내용')
        label_contents.move(5, 90)

        label_time = QLabel(self.dialog)
        label_time.setText('일시')
        label_time.move(5, 155)

        self.dialog.setWindowTitle('todo')
        self.dialog.setGeometry(600, 500, 350, 190)

        self.dialog.exec()

    def update_todo(self):
        txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * 3:(i + 1) * 3] for i in range((len(self.content_list) + 3 - 1) // 3)]
        txt.close()

    def dialog_close(self):
        self.dialog.close()
