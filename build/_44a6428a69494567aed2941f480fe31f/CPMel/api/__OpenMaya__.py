
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import maya.OpenMaya as OpenMaya
from maya.OpenMaya import *
__all__ = ['MMatrix', 'MPoint', 'MFloatPoint', 'MVector', 'MFloatVector']
ScriptUtil = OpenMaya.MScriptUtil()

class MDagPath(OpenMaya.MDagPath, ):

    def __repr__(self):
        return 'MDagPath("{}")'.format(self.fullPathName())

    def __str__(self):
        return 'MDagPath("{}")'.format(self.fullPathName())

def newMatrix(matrix=(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1), cls=OpenMaya.MMatrix):
    u'\n    \u521b\u5efaMMatrix\u7c7b\u7684\u65b9\u6cd5\n    :param matrix: None \u6216 MMatrix \u6216 \uff08[[...], [...]...] 4*4\uff09\n    :return: MMatrix\n    '
    if isinstance(matrix, cls):
        return cls(matrix)
    if (matrix is None):
        new_obj = cls()
        return new_obj
    if (len(matrix) == 4):
        matrix = [t for i in matrix for t in i]
    if (len(matrix) == 16):
        new_obj = cls()
        ScriptUtil.createMatrixFromList(matrix, new_obj)
        return new_obj
    else:
        raise RuntimeError(u'\u6784\u5efa\u77e9\u9635\u9700\u898116\u4e2a\u503c')

def newFloatMatrix(matrix=(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1), cls=OpenMaya.MMatrix):
    return newMatrix(matrix, OpenMaya.MFloatMatrix)

class MMatrix(OpenMaya.MMatrix, ):

    @classmethod
    def newMatrix(cls, matrix=None):
        u'\n        \u521b\u5efaMMatrix\u7c7b\u7684\u65b9\u6cd5\n        :param matrix: None \u6216 MMatrix \u6216 \uff08[[...], [...]...] 4*4 \u6216 4*3\uff09\n        :return: MMatrix\n        '
        if isinstance(matrix, cls):
            return cls(matrix)
        if (matrix is None):
            new_obj = cls()
            return new_obj
        if (len(matrix) == 4):
            matrix = [t for i in matrix for t in i]
        if (len(matrix) == 16):
            new_obj = cls()
            ScriptUtil.createMatrixFromList(matrix, new_obj)
            return new_obj
        else:
            raise RuntimeError(u'\u6784\u5efa\u77e9\u9635\u9700\u898116\u4e2a\u503c')

    def __str__(self):
        return ('Matrix%s' % str(tuple(self)))

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        if isinstance(item, int):
            return (self(item, 0), self(item, 1), self(item, 2), self(item, 3))
        else:
            return self(*item)

class MPoint(OpenMaya.MPoint, ):

    def __str__(self):
        return ('MPoint%s' % str((self.x, self.y, self.z)))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, OpenMaya.MPoint):
            other = OpenMaya.MVector(other)
        return OpenMaya.MPoint.__add__(self, other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

class MFloatPoint(OpenMaya.MFloatPoint, ):

    def __str__(self):
        return ('MFloatPoint%s' % str((self.x, self.y, self.z)))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, OpenMaya.MFloatPoint):
            other = OpenMaya.MFloatVector(other)
        return OpenMaya.MFloatPoint.__add__(self, other)

class MVector(OpenMaya.MVector, ):

    def __str__(self):
        return ('MVector%s' % str((self.x, self.y, self.z)))

    def __repr__(self):
        return self.__str__()

class MFloatVector(OpenMaya.MFloatVector, ):

    def __str__(self):
        return ('MFloatVector%s' % str((self.x, self.y, self.z)))

    def __repr__(self):
        return self.__str__()
