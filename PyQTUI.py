import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QDateTimeEdit, QMessageBox, QToolTip
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtGui import QFont

from ViewModel import ViewMode


class MyWindow(QMainWindow):
    on_confirm_login = None
    Buy = None
    is_login = False

    def __init__(self, onlogin, Buy):
        super().__init__()
        self.on_confirm_login = onlogin
        self.Buy = Buy
        self.setWindowTitle("淘宝抢购")
        self.resize(400, 200)

        QToolTip.setFont(QFont('微软雅黑', 16))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        label = QLabel("请扫码登录，后点击确认登录")
        layout.addWidget(label)

        button = QPushButton("确认登录")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        # 日期选择控件
        datetime = QDateTimeEdit()
        datetime.setDateTime(QDateTime.currentDateTime())
        datetime.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        layout.addWidget(datetime)

        btn = QPushButton('确认抢购时间')
        btn.setToolTip('输入抢购时间后点击确认')
        # 连接按钮点击事件到信号
        btn.clicked.connect(self.selectDateTime)
        layout.addWidget(btn)

        central_widget.setLayout(layout)


        # 尝试居中
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = int((screen.width()-size.width())/2)
        new_top = int((screen.height()-size.height())/2)
        print(new_left, new_top)
        self.move(new_left, new_top)

    def on_button_click(self):
        self.statusBar().showMessage("用户确认登录")
        self.is_login = True
        if not self.on_confirm_login():
            self.showErrorMessageUnLogin()
            self.is_login = False

    def selectDateTime(self):
        datetime = self.sender().parent().findChild(
            QDateTimeEdit).dateTime().toString('yyyy-MM-dd HH:mm:ss')
        QMessageBox.information(self, '确认抢购时间', datetime)
        view_mode = ViewMode()
        view_mode.set_selected_date(datetime)
        if self.is_login:
            self.Buy(view_mode.get_selected_date())
        else:
            self.showErrorMessageUnLogin()

    def showErrorMessageUnLogin(self):
        error_message = QMessageBox()
        error_message.setIcon(QMessageBox.Critical)
        error_message.setWindowTitle("未登录错误")
        error_message.setText("请先登录！！！！")
        error_message.resize(600, 600)
        error_message.exec_()


def UIInit(onConfirmLogin, buy):
    app = QApplication(sys.argv)
    window = MyWindow(onConfirmLogin, buy)
    window.show()
    sys.exit(app.exec_())


def handler():
    print('确认登录')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow(handler)
    window.show()
    sys.exit(app.exec_())
