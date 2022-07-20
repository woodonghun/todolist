import sys

from PySide2 import QtWidgets


import widget.funtion
import widget.edit
import widget.todo
import datetime
from PySide2.QtWidgets import QWidget, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, \
    QAbstractItemView, QMessageBox

from widget import funtion


class Main(QWidget):
    number = 0
    def __init__(self):
        super().__init__()
        self.update_todo()
        self.initUI()

    def initUI(self):
        todo = widget.todo.Todo
        edit = widget.edit.Edit
        function = widget.funtion.Function

        # main UI

        btn_add = QPushButton(self)
        btn_add.setText("할 일 추가")
        btn_add.clicked.connect(todo)
        btn_add.clicked.connect(self.update_todo)
        btn_add.clicked.connect(self.add_content)
        btn_add.move(50, 10)

        btn_confirm = QPushButton(self)
        btn_confirm.setText("완료 내용 확인")
        btn_confirm.move(50, 30)

        btn_complete = QPushButton(self)
        btn_complete.setText("선택된 항목 완료로 이동")
        btn_complete.move(50, 50)

        btn_delete = QPushButton(self)
        btn_delete.setText("선택된 항목 삭제")
        btn_delete.clicked.connect(self.delete)
        btn_delete.move(50, 70)

        self.table = QTableWidget(len(self.content_chunk), 4, self)

        self.table.setSortingEnabled(False)  # 정렬기능
        self.table.resizeRowsToContents()
        self.table.resizeColumnsToContents()  # 이것만으로는 checkbox 컬럼은 잘 조절안됨.
        self.table.setColumnWidth(0, 5)  # checkbox 컬럼 폭 강제 조절.
        self.table.setColumnWidth(1, 130)
        self.table.setColumnWidth(2, 282)
        self.table.setColumnWidth(3, 65)

        # main 동작

        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간
        dates = nowDatetime

        for i in range(len(self.content_chunk)-1):      # 동적 변수를 통해서 버튼, 체크박스 생성
            globals()['self.btn%d' % i] = QPushButton('수정')
            globals()['self.cb%d' % i] = QCheckBox()

        for i in range(len(self.content_chunk)-1):      # 내용 확인후 테이블에 버튼, 체크박스 등록
            self.table.setItem(i, 1, QTableWidgetItem(self.content_chunk[i][2]))
            self.table.setItem(i, 2, QTableWidgetItem(self.content_chunk[i][0]))
            self.table.setCellWidget(i, 0, globals()['self.cb{}'.format(i)])
            self.table.setCellWidget(i, 3, globals()['self.btn{}'.format(i)])

        for i in range(len(self.content_chunk)-1):
            globals()[f'self.btn{i}'].clicked.connect(self.check)
            globals()[f'self.btn{i}'].clicked.connect(edit)
            globals()[f'self.btn{i}'].clicked.connect(self.edit_content)     # 버튼 클릭됬을때 잘됨

        self.table.setGeometry(10, 100, 530, 300)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)   # 열 선택
        self.table.verticalHeader().setVisible(False)       # 행 해더 안보이게함
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   # 수정 불가능 하게 함
        self.table.setHorizontalHeaderLabels(["", "일시", "제목", ""])

        self.setWindowTitle('Todo list')
        self.setGeometry(500, 500, 550, 500)
        self.show()

    def delete(self):
        pass

    def toggle(self):
        pass

    def check(self):
        function = widget.funtion.Function
        aa = self.table.currentItem()
        if aa is None:
            function.setting.number = self.table.currentRow()
        print(function.setting.number)

    def update_todo(self):
        txt = open("C:/woo_project/todolist/widget/content", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * 3:(i + 1) * 3] for i in range((len(self.content_list) + 3 - 1) // 3)]
        txt.close()

    def edit_content(self):
        self.update_todo()
        for i in range(len(self.content_chunk)-1):      # 내용 확인후 테이블에 버튼, 체크박스 등록
            self.table.setItem(i, 1, QTableWidgetItem(self.content_chunk[i][2]))
            self.table.setItem(i, 2, QTableWidgetItem(self.content_chunk[i][0]))



    def add_content(self):
        line = len(self.content_chunk)-2
        globals()['self.btn%d' % line] = QPushButton('수정')      # 동적 변수로 추가함
        globals()['self.cb%d' % line] = QCheckBox()
        self.table.setItem(line, 1, QTableWidgetItem(self.content_chunk[line][2]))
        self.table.setItem(line, 2, QTableWidgetItem(self.content_chunk[line][0]))
        self.table.setCellWidget(line, 0, globals()['self.cb%d' % line])
        self.table.setCellWidget(line, 3, globals()['self.btn%d' % line])

        for i in globals():
            print(i)

        row_count = self.table.rowCount()
        self.table.setRowCount(row_count+1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
