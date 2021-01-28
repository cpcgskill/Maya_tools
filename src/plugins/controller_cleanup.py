#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/21 13:39
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
    [item.Help, u"用于清理模型的输入历史"],
)


def main(*args):
    sel = selected()
    select(cl=True)
    set_ints = set()
    for i in sel:
        set_ints.add(i)
        for l in listRelatives(i, s=True):
            set_ints.add(l)
            for t in listConnections(l, scn=True):
                set_ints.add(t)
        for l in listConnections(i, scn=True):
            set_ints.add(l)
    for i in set_ints:
        try:
            i.ihi.set(0)
        except:
            pass
    select(sel)
    refresh()


def init():
    print(u"mesh mirror inspection")


def doit():
    build(form=ui, func=main, title=name(), doit_text=u"选择控制器执行")


def name():
    return u"控制器链接隐藏工具"
