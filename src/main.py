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
from plugins import plugins
from setup import show
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
        v_label = QLabel(START_TIME + u"-" + str(datetime.datetime.now().year) + u" Version " + u"{:.1f}".format(Version))
        self._main_layout.addWidget(v_label)
        self._main_layout.addStretch(0)

        # setup_bn = QPushButton(u"设置")
        # setup_bn.clicked.connect(lambda *args: show(self))
        # self._main_layout.addWidget(setup_bn)
        update_bn = QPushButton(u"更新")
        update_bn.clicked.connect(lambda *args: update.update())
        self._main_layout.addWidget(update_bn)


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
                label = QLabel(self)
                label.setPixmap(pix)
                label.setFixedSize(QSize(20, 20))
                bn = QPushButton(name)
                bn.clicked.connect(lambda *args: i.doit())
                h_layout = QHBoxLayout()
                h_layout.addWidget(label)
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

        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._news = QLabel()
        self._news.setText(u"loading...")
        self._main_layout.addWidget(self._news)
        self._update_thread = UpdateThread()
        self._update_thread.sinOut.connect(self._updateVersion)
        self._update_thread.start()

    def _updateVersion(self, data):
        data = json.loads(data)
        if int(Version * 10) < int(data.get(u"version", -1) * 10):
            self._news.setText(u"存在新的版本 : " + str(data.get(u"version", -1)))
            return
        self._news.setText(u"已经是最新的版本了!")
        return


class _MainWindow(QWidget):
    def __init__(self, parent=None):
        super(_MainWindow, self).__init__(parent)
        self._main_layout = QVBoxLayout(self)
        self._head = Head(self)
        self._body = Body(self)
        self._main_layout.addWidget(self._head)
        self._main_layout.addWidget(self._body)


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
        self._main_layout.addWidget(self._head)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._main_layout.addWidget(self._body)
        self.setMinimumHeight(400)

        # self._main_layout.setSpacing(0)
        # self._main_window = _MainWindow(self)
        # scrollArea = QScrollArea(self)
        # scrollArea.setWidgetResizable(True)
        # scrollArea.setWidget(self._main_window)
        # self._main_layout.addWidget(scrollArea)

    def closeEvent(self, *args, **kwargs):
        deleteWidget(self)
