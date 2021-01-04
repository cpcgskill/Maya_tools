#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/30 21:55
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import json
from CPMel.ui import *


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.setWindowFlags(Qt.Window)
        self.setWindowTitle(u"setup")
        self.setMinimumSize(QSize(200, 200))

        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(2)


        up_setup_bn = QPushButton(u"保存设置")
        up_setup_bn.clicked.connect(self.upSetup)
        self._main_layout.addWidget(up_setup_bn)
    def upSetup(self, *args):
        self.close()

win = None


def show(parent=None):
    win = MainWindow(parent)
    win.exec_()
