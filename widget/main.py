import sys

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt

import widget.funtion
import widget.edit
import widget.todo
import widget.complete
import widget.title_cont
import datetime
from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, \
    QAbstractItemView, QMessageBox


class Main(QWidget):
    number = 0

    def __init__(self):
        super().__init__()
        self.update_todo()
        self.initUI()

    def initUI(self):
        txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
        self.value = txt.read()
        self.row_list = []

        todo = widget.todo.Todo
        edit = widget.edit.Edit
        complete = widget.complete.Complete
        function = widget.funtion.Function

        # main UI
        self.table = QTableWidget(len(self.content_chunk), 4, self)

        # self.table.setSortingEnabled(False)  # 정렬기능
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()  # 이것만으로는 checkbox 열 은 잘 조절안됨.
        self.table.setColumnWidth(0, 5)  # checkbox 열 폭 강제 조절.
        self.table.setColumnWidth(1, 130)
        self.table.setColumnWidth(2, 282)
        self.table.setColumnWidth(3, 65)

        btn_add = QPushButton(self)
        btn_add.setText("할 일 추가")
        btn_add.clicked.connect(self.inital)
        btn_add.clicked.connect(todo)
        btn_add.clicked.connect(self.add_content)
        btn_add.setGeometry(100, 25, 100, 30)

        btn_confirm = QPushButton(self)
        btn_confirm.setText("완료 내용 확인")
        btn_confirm.clicked.connect(complete)
        btn_confirm.setGeometry(300, 25, 100, 30)

        btn_complete = QPushButton(self)
        btn_complete.setText("선택된 항목 완료로 이동")
        btn_complete.clicked.connect(self.complete)
        btn_complete.setGeometry(100, 400, 160, 30)

        btn_delete = QPushButton(self)
        btn_delete.setText("선택된 항목 삭제")
        btn_delete.clicked.connect(self.delete)
        btn_delete.setGeometry(300, 400, 160, 30)

        # main 동작
        self.table.doubleClicked.connect(self.check2)

        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간
        self.dates = nowDatetime

        for i in range(len(self.content_chunk) - 1):  # 내용 확인후 테이블에 버튼, 체크박스 등록
            btn = QPushButton('수정')
            cb = QCheckBox()
            self.table.setItem(i, 1, QTableWidgetItem(self.content_chunk[i][2]))
            self.table.setItem(i, 2, QTableWidgetItem(self.content_chunk[i][0]))
            self.table.setCellWidget(i, 0, cb)
            self.table.setCellWidget(i, 3, btn)

            cb.stateChanged.connect(self.cb_change)
            btn.clicked.connect(self.check)
            btn.clicked.connect(edit)
            btn.clicked.connect(self.edit_content)

        self.table.setGeometry(10, 70, 530, 300)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)   # 열 선택
        self.table.verticalHeader().setVisible(False)       # 행 해더 안보이게함
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   # 수정 불가능 하게 함
        self.table.setHorizontalHeaderLabels(["", "일시", "제목", ""])

        self.setWindowTitle('Todo list')
        self.setGeometry(500, 300, 550, 450)
        self.show()

    def current(self):
        aa = self.table.selectedIndexes()
        cell = set((idx.row(), idx.column()) for idx in aa)
        # print(cell)
        txt1 = "selected cells ; {0}".format(cell)
        msg = QMessageBox.information(self, 'selectedIndexes()...', txt1)

    def cb_change(self, state):     # 리스트 에 저장함
        if state == Qt.Checked:
            self.row_list.append(self.table.currentRow())
        else:
            self.row_list.remove(self.table.currentRow())
        self.row_list.sort()
        self.row_list.reverse()

    def delete(self):       # 삭제
        new_text_content = ''

        for p in range(len(self.row_list)):

            txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
            lines = txt.readlines()
            for i, l in enumerate(lines):
                if i == self.row_list[p] * 3:
                    new_string = ''
                elif i == self.row_list[p] * 3 + 2:
                    new_string = ''
                elif i == self.row_list[p] * 3 + 1:
                    new_string = ''
                else:
                    new_string = l.strip()
                if new_string:
                    new_text_content += new_string + '\n'
                else:
                    new_text_content += ''
            print(self.row_list[p])
            self.table.removeRow(self.row_list[p])
            txt.close()

            txt = open("C:/woo_project/todolist/widget/content.txt", 'w')
            txt.write(new_text_content)
            txt.close()
            new_text_content = ''
            self.update_todo()

        self.row_list = []

    def complete(self):
        self.row_list.reverse()
        self.update_todo()
        txt = open("C:/woo_project/todolist/widget/finish.txt", 'a')
        for j in self.row_list:
            for i in range(3):
                txt.write(''.join(self.content_chunk[j][i]) + '\n')
                print(self.content_chunk[j][i])
            txt.write(''.join(self.dates) + '\n')
        txt.close()
        self.row_list.reverse()
        self.delete()

    def check(self):        # 클릭된 버튼의 행 값 저장
        function = widget.funtion.Function
        aa = self.table.currentItem()
        if aa is None:
            function.setting.number = self.table.currentRow()
        print(function.setting.number)

    def check2(self):
        ffff = widget.title_cont.Title_Cont
        function = widget.funtion.Function
        aa = self.table.selectedIndexes()
        function.setting.number = aa[0].row()
        print(function.setting.number)
        ffff()
    def update_todo(self):
        txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * 3:(i + 1) * 3] for i in range((len(self.content_list) + 3 - 1) // 3)]
        txt.close()

    def edit_content(self):     # 내용 수정
        self.update_todo()
        for i in range(len(self.content_chunk)-1):      # 내용 확인후 테이블에 버튼, 체크박스 등록
            self.table.setItem(i, 1, QTableWidgetItem(self.content_chunk[i][2]))
            self.table.setItem(i, 2, QTableWidgetItem(self.content_chunk[i][0]))

    def inital(self):
        txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
        self.value = txt.read()

    def add_content(self):      # 내용 추가, 버튼 추가, 줄 추가,
        edit = widget.edit.Edit
        self.update_todo()

        if self.value != self.content:      # 처음 값과 추가된 값이 달라야 add 추가 안하면 그냥 꺼도 줄이 추가됨
            line = len(self.content_chunk)-2    # 빈줄 1칸 있어서 -2 해야됨
            btn = QPushButton('수정')      # 동적 변수로 추가함
            cb = QCheckBox()

            self.table.setItem(line, 1, QTableWidgetItem(self.content_chunk[line][2]))
            self.table.setItem(line, 2, QTableWidgetItem(self.content_chunk[line][0]))
            self.table.setCellWidget(line, 0, cb)
            self.table.setCellWidget(line, 3, btn)

            self.table.setRowCount(self.table.rowCount() + 1)

            cb.stateChanged.connect(self.cb_change)
            btn.clicked.connect(self.check)
            btn.clicked.connect(edit)
            btn.clicked.connect(self.edit_content)

            print(self.table.rowCount())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
