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
import datetime

import config

reload(config)
from config import *

if DEBUG:
    import plugins

    reload(plugins)
    import setup

    reload(setup)

from CPMel.ui import *
from plugins import plugins
from setup import show


class Head(QWidget):
    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.setFixedHeight(36)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = QLabel()
        head_label.setPixmap(QPixmap(HEAD_IMG))
        self._main_layout.addWidget(head_label)
        v_label = QLabel(START_TIME + u"-" + str(datetime.datetime.now().year) + u" Version " + Version)
        self._main_layout.addWidget(v_label)
        self._main_layout.addStretch(0)

        setup_bn = QPushButton(u"设置")
        setup_bn.clicked.connect(lambda *args: show(self))
        self._main_layout.addWidget(setup_bn)


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
        self._news.setText(u"---------")
        self._main_layout.addWidget(self._news)


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
        self.setMinimumWidth(300)
        icon = QIcon(IMAGES + u"/icon.png")
        self.setWindowIcon(icon)
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)

        self._head = Head(self)
        self._body = Body(self)
        self._main_layout.addWidget(self._head)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        self._main_layout.addWidget(self._body)

        # self._main_layout.setSpacing(0)
        # self._main_window = _MainWindow(self)
        # scrollArea = QScrollArea(self)
        # scrollArea.setWidgetResizable(True)
        # scrollArea.setWidget(self._main_window)
        # self._main_layout.addWidget(scrollArea)

    def closeEvent(self, *args, **kwargs):
        deleteWidget(self)
