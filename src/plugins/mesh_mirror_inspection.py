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
from CPMel.api.OpenMaya import MGlobal

ui = (
    [item.Help, u"多边形模型顶点镜像检查工具"],
    [item.Label, u"误差:"],
    [item.FloatSlider, 0.001, 0.1, 0.001],
)


def meshMirrorCheck(_, __, mistake):
    meshs = selected()
    _meshs = list()
    for i in meshs:
        ss = listRelatives(i, s=True)
        if ss is None:
            _meshs.append(i)
        else:
            for t in ss:
                _meshs.append(t)
    meshs = [i for i in _meshs if i.type == u"mesh"]
    sel_vtx = list()
    for i in meshs:
        MGlobal.displayInfo(u"检查: %s" % i.fullPathName())
        refresh()
        pts = i.getPoints(space=Space.world)
        reverse_pts = tuple((Double3((i.x * -1, i.y, i.z)) for i in pts))
        sel_vtx.append(
            [i.vtx[Id] for Id, pt in enumerate(pts) if min((r_pt.dis(pt) for r_pt in reverse_pts)) > mistake])
    select([t for i in sel_vtx for t in i])


def init():
    print(u"mesh mirror inspection")


def doit():
    build(form=ui, func=meshMirrorCheck, title=name(), doit_text=u"选择模型执行")


def name():
    return u"模型镜像检查工具"
