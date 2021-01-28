#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/21 22:17
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel_Form import build, item
from CPMel.cmds import *
from CPMel.api.OpenMaya import MGlobal

ui = (
    [item.Help, u"选择需要解锁的节点，然后提交"],
)


def main(*args):
    sel = selected()
    for i in sel:
        lockNode(i, lock=False, ic=True)


def init():
    print(u"mesh mirror inspection")


def doit():
    build(form=ui, func=main, title=name(), doit_text=u"执行")


def name():
    return u"节点解锁工具"
