#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/21 22:33
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
一键清理场景
"""
from CPMel.cmds import *


def init():
    pass


def doit():
    sel = selected()
    try:
        mel.DeleteAllHistory()
        select(cl=True)
        select(ls("*", type="transform"), r=True)
        makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
        mel.CenterPivot()
        mel.DeleteAllHistory()
    except Exception as ex:
        raise CPMelToolError(str(ex))
    finally:
        select([i for i in sel if objExists(i)], r=True)


def name():
    return u"一键清理场景"
