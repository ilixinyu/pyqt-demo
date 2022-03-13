#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMessageBox, QDesktopWidget, QMenu, QAction, QMainWindow,
                             qApp, QTextEdit, QFileDialog, QHBoxLayout, QLabel)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QCoreApplication, QObject, pyqtSignal

x = 100


class Communicate(QObject):
    closeApp = pyqtSignal()


# 创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # self.setGeometry(300, 300, 300, 220)
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('高光谱图像变化检测软件 V1.0')
        self.setWindowIcon(QIcon('icon.webp'))
        self.initbutton()
        self.initMenu()
        self.initTool()
        self.initStatus()
        self.initComm()
        self.show()

    def initComm(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

    def initText(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        ViewMenu = menubar.addMenu('帮助')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        ViewMenu.addAction(viewStatAct)

    def initTool(self):
        exitAct = QAction(QIcon('icon/1.1.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        exitAct = QAction(QIcon('icon/2.1.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        exitAct = QAction(QIcon('icon/3.1.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        exitAct = QAction(QIcon('icon/4.1.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        exitAct = QAction(QIcon('icon/5.1.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        exitAct = QAction(QIcon('icon/6.1.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        exitAct = QAction(QIcon('icon/7.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def initStatus(self):

        self.statusBar().showMessage('Ready')

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initbutton(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn1 = QPushButton('输入变化前图片Ix', self)
        btn1.setToolTip('This is a <b>QPushButton</b> widget')
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 10 + x)
        btn1.clicked.connect(self.buttonClicked1)

        btn2 = QPushButton('输入变化后图片Iy', self)
        btn2.setToolTip('This is a <b>QPushButton</b> widget')
        btn2.resize(btn2.sizeHint())
        btn2.move(50, 50 + x)
        btn2.clicked.connect(self.buttonClicked2)

        btn4 = QPushButton('导入模型M', self)
        btn4.setToolTip('This is a <b>QPushButton</b> widget')
        btn4.resize(btn2.sizeHint())
        btn4.move(50, 90 + x)
        btn4.clicked.connect(self.buttonClicked3)

        btn3 = QPushButton('输出变化检测结果R', self)
        btn3.setToolTip('This is a <b>QPushButton</b> widget')
        btn3.resize(btn3.sizeHint())
        btn3.move(50, 130 + x)
        btn3.clicked.connect(self.buttonClicked4)

        qbtn = QPushButton('退出E', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 170 + x)

    def buttonClicked1(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:/')
        print("已加载变化前图像Ix： " + fname[0])

        # if fname[0]:
        #     f = open(fname[0], 'r')
        #
        #     with f:
        #         data = f.read()
        #         self.textEdit.setText(data)

    def buttonClicked2(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:/')
        print("已加载变化后图像Iy： " + fname[0])

    def buttonClicked3(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:/')
        print("已加载模型M： " + fname[0])

    def buttonClicked4(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        print("输出变化检测结果R： ")

    def closeEvent(self, event):

        reply = QMessageBox.question(self, '消息',
                                     "确认退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
