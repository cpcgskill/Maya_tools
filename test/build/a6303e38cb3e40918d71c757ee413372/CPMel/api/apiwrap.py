
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import maya.cmds as cmds
from .. import core as cmcore
from . import OpenMaya

class MeshVertex(object, ):
    u'\n\n    Meshapi\u5305\u88c5\n    '

    def __init__(self, obj_name):
        sel = OpenMaya.MSelectionList()
        sel.add(obj_name)
        path = OpenMaya.MDagPath()
        obj = OpenMaya.MObject()
        sel.getDagPath(path, obj)
        self.it = OpenMaya.MItMeshVertex(path, obj)
        self.fn = OpenMaya.MFnMesh(path)
        self.init_points = OpenMaya.MPointArray()
        self.fn.getPoints(self.init_points)
        self.init_us = OpenMaya.MFloatArray()
        self.init_vs = OpenMaya.MFloatArray()
        self.fn.getUVs(self.init_us, self.init_vs)

    def end(self):
        u'\n        \u7ed3\u675f\u65b9\u6cd5\n\n        :return:\n        '
        self.end_points = OpenMaya.MPointArray()
        self.fn.getPoints(self.end_points)
        self.end_us = OpenMaya.MFloatArray()
        self.end_vs = OpenMaya.MFloatArray()
        self.fn.getUVs(self.end_us, self.end_vs)

    def redoIt(self):
        u'\n        \u6267\u884c\n\n        :return:\n        '
        self.fn.setPoints(self.end_points)
        self.fn.setUVs(self.end_us, self.end_vs)

    def undoIt(self):
        u'\n        \u64a4\u9500\n\n        :return:\n        '
        self.fn.setPoints(self.init_points)
        self.fn.setUVs(self.init_us, self.init_vs)

    def __enter__(self):
        return self.it

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end()
        cmcore.defAddCommandList(self.redoIt, self.undoIt)
