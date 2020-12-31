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
    [item.Label, u"选择模型 -- 以左边为基准检查右边"],
    [item.SelectList],
)


def meshMirrorCheck(_, meshs):
    meshs = [newObject(i) for i in meshs]
    _meshs = list()
    for i in meshs:
        ss = listRelatives(i, s=True)
        if ss is None:
            _meshs.append(i)
        else:
            for t in ss:
                _meshs.append(t)
    meshs = [i for i in _meshs if i.type == u"mesh"]
    select([i.vtx for i in meshs])
    no_sel_vtx = set()
    for i in meshs:
        MGlobal.displayInfo(u"检查: %s" % i.fullPathName())
        pts = i.getPoints(space=Space.world)
        for Id, pt in enumerate(pts):
            if pt.x > 0.01:
                pt.x = pt.x * -1
                for Id_r, pt_r in enumerate(pts):
                    if pt.dis(pt_r) < 0.01:
                        no_sel_vtx.add(i.vtx[Id])
                        no_sel_vtx.add(i.vtx[Id_r])
            elif pt.x < -0.01:
                pass
            else:
                no_sel_vtx.add(i.vtx[Id])
    select(list(no_sel_vtx), d=True)


def init():
    print(u"mesh mirror")


def doit():
    build(u"TestApp", form=ui, func=meshMirrorCheck, title=name())


def name():
    return u"模型镜像检查工具"
