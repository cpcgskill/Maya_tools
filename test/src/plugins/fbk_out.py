#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/30 23:14
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel_Form import build, item
from CPMel.cmds import *

#
# class MainWindow(CPQWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle(name())
#
#         self._main_layout = QVBoxLayout(self)
#         self._label = QLabel(self)
#         self._label.setText(u"选择模型")
#
#         self._main_layout.addWidget(self._label)


ui = (
    (item.Is, u"Test1"),
)


def FBKOut(self, is_ok):
    print is_ok


def init():
    print(u"INIT FBKOUT")


def doit():
    build(u"TestApp", form=ui, func=FBKOut)


def name():
    return u"FBK导出工具"
