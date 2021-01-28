#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/27 23:49
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel.ui import *
from CPMel.cmds import *


def init():
    pass


def doit():
    text, ok = QInputDialog().getText(mui,
                                      u"选择",
                                      u"*为通配符\n例：curve*",
                                      QLineEdit.Normal,
                                      u"")
    if not ok:
        return
    select(ls(text))


def name():
    return u"节点快速选择器"
