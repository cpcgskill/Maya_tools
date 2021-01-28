#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/30 17:44
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import json
import datetime
from functools import partial
import config

reload(config)
from config import *

if DEBUG:
    import CPMel_Form

    reload(CPMel_Form)
    import plugins

    reload(plugins)
    import setup

    reload(setup)

    import update

    reload(update)

from CPMel.ui import *
from CPMel.tool import *
from plugins import plugins
import update


class HeadPixButton(QPushButton):
    def __init__(self, parent=None):
        super(HeadPixButton, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = QLabel()
        pix = QPixmap(HEAD_IMG)
        head_label.setPixmap(pix)
        self._main_layout.addWidget(head_label)
        self.setFixedSize(pix.size())
        self.clicked.connect(lambda *args: QDesktopServices.openUrl(QUrl(u'https://www.cpcgskill.com')))

    def paintEvent(self, event):
        pass


class Head(QWidget):
    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.setFixedHeight(36)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = HeadPixButton()
        self._main_layout.addWidget(head_label)
        self._main_layout.addStretch(0)



class _Body(QWidget):
    def __init__(self, parent=None):
        super(_Body, self).__init__(parent)
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(2)
        pix = QPixmap(IMAGES + u"/button.png")
        for i in plugins:
            try:
                i.init()
                name = i.name()
            except Exception as ex:
                print(ex)
            else:
                bn = QPushButton(u" " + name)
                bn.setIcon(pix)
                bn.clicked.connect(undoBlock(i.doit))
                h_layout = QHBoxLayout()
                h_layout.addWidget(bn)
                self._main_layout.addLayout(h_layout)
        self._main_layout.addStretch(0)


class UpdateThread(QThread):
    sinOut = Signal(str)

    def __init__(self, parent=None):
        super(UpdateThread, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        info = update.updateinfo()
        self.sinOut.emit(info)


class Body(QWidget):
    def __init__(self, parent=None):
        super(Body, self).__init__(parent)
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(0)

        self._body = _Body(self)
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(self._body)
        self._main_layout.addWidget(scrollArea)


class Footer(QWidget):
    def __init__(self, parent=None):
        super(Footer, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(0)
        v_label = QLabel(
            START_TIME + u"-" + str(datetime.datetime.now().year) + u" Version " + u"{:.1f}".format(Version))
        self._main_layout.addWidget(v_label)
        self._main_layout.addStretch(0)
    #     self._news = QLabel()
    #     self._news.setText(u"loading...")
    #     self._main_layout.addWidget(self._news)
    #     self._update_thread = UpdateThread()
    #     self._update_thread.sinOut.connect(self._updateVersion)
    #     self._update_thread.start()
    #
    #     self.update_bn = QPushButton(u"更新")
    #     self.update_bn.clicked.connect(lambda *args: update.update())
    #     self._main_layout.addWidget(self.update_bn)
    #     self.update_bn.close()
    #
    # def _updateVersion(self, data):
    #     data = json.loads(data)
    #     if int(Version * 10) < int(data.get(u"version", -1) * 10):
    #         self._news.setText(u"存在新的版本 : " + str(data.get(u"version", -1)))
    #         self.update_bn.show()
    #         return
    #     self._news.setText(u"已经是最新的版本了!")
    #     return


class MainWindow(CPQWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(Title)
        icon = QIcon(IMAGES + u"/icon.png")
        self.setWindowIcon(icon)
        with open(ASSETS + u"/qss.qss", "r") as f:
            self.setStyleSheet(f.read())

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(5)

        self._head = Head(self)
        self._body = Body(self)
        self._footer = Footer(self)
        self._main_layout.addWidget(self._head)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._main_layout.addWidget(self._body)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._main_layout.addWidget(self._footer)
        self.setMinimumWidth(240)
        self.setMinimumHeight(400)

        # self._main_layout.setSpacing(0)
        # self._main_window = _MainWindow(self)
        # scrollArea = QScrollArea(self)
        # scrollArea.setWidgetResizable(True)
        # scrollArea.setWidget(self._main_window)
        # self._main_layout.addWidget(scrollArea)


win = None


def main():
    global win
    if not win is None:
        deleteWidget(win)
    win = MainWindow()
    win.show()
