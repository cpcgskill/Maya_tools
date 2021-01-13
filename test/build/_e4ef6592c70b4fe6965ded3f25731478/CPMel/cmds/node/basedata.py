
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\nCPMel\u3002cmds\u7684\u6570\u636e\u7c7b\u578b\u5b9a\u4e49\n'
import array
from array import array
from ... import ISDEBUG
import maya.cmds as cmds
from ...api import OpenMaya
from ... import core as cmcore
from ...cppplug import Double3, Matrix, NewMatrixs, NewDouble3s, BaseData

class Space:
    u'\n    \u5bf9\u8c61\u7a7a\u95f4 object\n    \u4e16\u754c\u7a7a\u95f4 world\n    \u53d8\u6362\u77e9\u9635\uff08\u76f8\u5bf9\uff09\u7a7a\u95f4 transform\n    \u9884\u8f6c\u6362\u77e9\u9635\uff08\u51e0\u4f55\uff09preTransform\n    \u8f6c\u6362\u540e\u7684\u77e9\u9635\uff08\u4e16\u754c\uff09\u7a7a\u95f4 postTransform\n    '
    object = OpenMaya.MSpace.kObject
    world = OpenMaya.MSpace.kWorld
    transform = OpenMaya.MSpace.kTransform
    preTransform = OpenMaya.MSpace.kPreTransform
    postTransform = OpenMaya.MSpace.kPostTransform

class ValueArray(array, ):

    def __str__(self):
        return ('%s[%s]' % (self.__class__.__name__, ', '.join([str(i) for i in self])))

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return unicode(self.__str__())

class IntArray(ValueArray, ):

    def __new__(cls, value):
        return array.__new__(cls, 'i', value)

class DoubleArray(ValueArray, ):

    def __new__(cls, value):
        return array.__new__(cls, 'd', value)

class FloatArray(ValueArray, ):

    def __new__(cls, value):
        return array.__new__(cls, 'f', value)
