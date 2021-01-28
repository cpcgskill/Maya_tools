#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/21 22:21
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel.cmds import *


def init():
    pass


def doit():
    sel = selected()
    try:
        select("*")
        all_node = selected()
        for i in all_node:
            if not i.isDefaultNode():
                lockNode(i, lock=True, ic=True)
    except Exception as ex:
        raise CPMelToolError(str(ex))
    finally:
        select(sel, r=True)


def name():
    return u"一键锁定场景"
