from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QDialog, QPushButton, QAbstractItemView, QTableWidget, QTableWidgetItem, \
    QCheckBox

import widget.funtion
import widget.title_cont

class Complete(QWidget):
    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()
        self.dialog_close()

    def initUI(self):
        self.row_list = []
        txt = open("C:/woo_project/todolist/widget/finish.txt", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * 4:(i + 1) * 4] for i in
                              range((len(self.content_list) + 4 - 1) // 4)]
        txt.close()

        self.table = QTableWidget(len(self.content_chunk), 4, self.dialog)

        self.table.setSortingEnabled(False)  # 정렬기능
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()  # 이것만으로는 checkbox 열 은 잘 조절안됨.
        self.table.setColumnWidth(0, 5)  # checkbox 열 폭 강제 조절.
        self.table.setColumnWidth(1, 130)
        self.table.setColumnWidth(2, 130)
        self.table.setColumnWidth(3, 200)

        for i in range(len(self.content_chunk) - 1):  # 내용 확인후 테이블에 버튼, 체크박스 등록
            cb = QCheckBox()
            self.table.setItem(i, 1, QTableWidgetItem(self.content_chunk[i][2]))
            self.table.setItem(i, 3, QTableWidgetItem(self.content_chunk[i][0]))
            self.table.setItem(i, 2, QTableWidgetItem(self.content_chunk[i][3]))
            self.table.setCellWidget(i, 0, cb)

            cb.stateChanged.connect(self.cb_change)

        self.table.setGeometry(10, 10, 530, 200)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)  # 열 선택
        self.table.verticalHeader().setVisible(False)  # 행 해더 안보이게함
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)  # 수정 불가능 하게 함
        self.table.setHorizontalHeaderLabels(["", "설정 일시", "완료일시", "제목"])

        btn = QPushButton(self.dialog)
        btn.setText('선택된 항목 삭제')
        btn.clicked.connect(self.delete)
        btn.move(170, 215)

        self.table.doubleClicked.connect(self.content_widget)

        self.dialog.setWindowTitle('Todo list')
        self.dialog.setGeometry(500, 500, 550, 250)
        self.dialog.exec()

    def delete(self):       # 삭제
        new_text_content = ''

        for p in range(len(self.row_list)):

            txt = open("C:/woo_project/todolist/widget/finish.txt", 'r')
            lines = txt.readlines()
            for i, l in enumerate(lines):
                if i == self.row_list[p] * 3:
                    new_string = ''
                elif i == self.row_list[p] * 3 + 2:
                    new_string = ''
                elif i == self.row_list[p] * 3 + 1:
                    new_string = ''
                elif i == self.row_list[p] * 3 + 3:
                    new_string = ''
                else:
                    new_string = l.strip()
                if new_string:
                    new_text_content += new_string + '\n'
                else:
                    new_text_content += ''
            self.table.removeRow(self.row_list[p])
            txt.close()

            txt = open("C:/woo_project/todolist/widget/finish.txt", 'w')
            txt.write(new_text_content)
            txt.close()
            new_text_content = ''
            self.update_todo()

        self.row_list = []

    def cb_change(self, state):     # 리스트 에 저장함
        if state == Qt.Checked:
            self.row_list.append(self.table.currentRow())
        else:
            self.row_list.remove(self.table.currentRow())
        self.row_list.sort()
        self.row_list.reverse()

    def update_todo(self):
        txt = open("C:/woo_project/todolist/widget/finish.txt", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * 4:(i + 1) * 4] for i in range((len(self.content_list) + 4 - 1) // 4)]
        txt.close()

    def content_widget(self):
        title_con = widget.title_cont.Title_Cont
        function = widget.funtion.Function
        aa = self.table.selectedIndexes()
        function.setting.number = aa[0].row()
        if self.table.rowCount() - 1 != aa[0].row():
            title_con()
        else:
            pass

    def dialog_close(self):
        self.dialog.close()