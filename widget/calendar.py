import sys
import widget.todo

from PySide2.QtCore import QTime
from PySide2.QtWidgets import QApplication, QCalendarWidget, QLabel, QWidget, QDialog, QPushButton, \
    QTimeEdit


class Calendar(QWidget):

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()
        self.dialog_close()

    def initUI(self):


        label1 = QLabel(self)
        label1.setText('날짜 시간 선택')
        label1.move(100, 200)

        btn1 = QPushButton(self.dialog)
        btn1.setText('ok')
        btn1.clicked.connect(self.btn_clicked)
        btn1.move(150, 200)

        self.cal = QCalendarWidget(self.dialog)
        self.cal.setGridVisible(True)
        self.cal.selectionChanged.connect(self.showDate)

        self.lbl = QLabel(self.dialog)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString('yyyy-MM-dd'))
        self.lbl.move(20, 200)

        self.timeedit = QTimeEdit(self.dialog)
        self.timeedit.setTime(QTime.currentTime())
        self.timeedit.setTimeRange(QTime(0, 00, 00), QTime(23, 59, 59))
        self.timeedit.setDisplayFormat('hh:mm:ss')
        self.timeedit.move(80, 200)

        self.dialog.setWindowTitle('날짜 설정')
        self.dialog.setGeometry(300, 300, 300, 300)
        self.dialog.exec()

    def showDate(self):
        cal_date = self.cal.selectedDate()
        self.strDate = cal_date.toString('yyyy-MM-dd')
        self.lbl.setText(self.strDate)

    def btn_clicked(self):
        cal_date = self.cal.selectedDate()
        self.strDate = cal_date.toString('yyyy-MM-dd')
        txt = open("C:/woo_project/todolist/widget/timedate.txt", 'w')
        day = self.strDate
        time = self.timeedit.text()
        self.dates = day+' '+time
        txt.write(self.dates)
        txt.close()

        self.dialog_close()

    def dialog_close(self):
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calendar()
    sys.exit(app.exec_())
