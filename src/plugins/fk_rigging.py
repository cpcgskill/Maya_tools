#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/21 20:50
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
    [item.Help, u"FK绑定工具"],
)


def main(*args):
    sel = selected(type="joint")



def init():
    print(u"mesh mirror inspection")


def doit():
    build(form=ui, func=main, title=name(), doit_text=u"关节")


def name():
    return u"FK绑定工具"
