from PySide2.QtWidgets import QDialog, QWidget, QLabel, QTextBrowser

import widget.funtion


class Title_Cont(QWidget):

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()
        self.dialog_close()

    def initUI(self):
        function = widget.funtion.Function
        row = function.setting.number  # 저장된 행 값 출력
        self.update()

        edt_title = QLabel(self.dialog)
        edt_title.setText(self.content_chunk[row][0])
        edt_title.setStyleSheet('background-color: white;'
                                'border-style: solid;'
                                'border-width: 1px;'
                                'border-color: #111111;')
        edt_title.setGeometry(35, 10, 300, 30)

        edt_contents = QTextBrowser(self.dialog)  # QTextBrowser은 QTextEdit의 확장형 다양한 기능을 더 많이 활용 가능
        edt_contents.append(self.content_chunk[row][1])     # ui 이쁘게 안하면 더 많이 사용할 것 같음
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

        self.dialog.setWindowTitle('내용 확인')
        self.dialog.setGeometry(600, 500, 350, 190)

        self.dialog.exec()

    def update(self):
        function = widget.funtion.Function
        function.update_todo(self, 3)

    def dialog_close(self):
        self.dialog.close()


class Title_Cont_Com(Title_Cont):
    def __init__(self):
        super().__init__()

    def update(self):
        function = widget.funtion.Function
        function.complete_todo(self, 4)
