
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
from . import __OpenMaya__ as OpenMaya
from .__ALL import MAyyayIt

class MAttributePatternArray(OpenMaya.MAttributePatternArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MAttributeSpecArray(OpenMaya.MAttributeSpecArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MCallbackIdArray(OpenMaya.MCallbackIdArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MColorArray(OpenMaya.MColorArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MDagPathArray(OpenMaya.MDagPathArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MDoubleArray(OpenMaya.MDoubleArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MFloatArray(OpenMaya.MFloatArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MFloatPointArray(OpenMaya.MFloatPointArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MFloatVectorArray(OpenMaya.MFloatVectorArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MInt64Array(OpenMaya.MInt64Array, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MIntArray(OpenMaya.MIntArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MMatrixArray(OpenMaya.MMatrixArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MObjectArray(OpenMaya.MObjectArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MPlugArray(OpenMaya.MPlugArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MPointArray(OpenMaya.MPointArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MTimeArray(OpenMaya.MTimeArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MTrimBoundaryArray(OpenMaya.MTrimBoundaryArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MUint64Array(OpenMaya.MUint64Array, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MUintArray(OpenMaya.MUintArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))

class MVectorArray(OpenMaya.MVectorArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))
__all__ = ['MAttributePatternArray', 'MAttributeSpecArray', 'MCallbackIdArray', 'MColorArray', 'MDagPathArray', 'MDoubleArray', 'MFloatArray', 'MFloatPointArray', 'MFloatVectorArray', 'MInt64Array', 'MIntArray', 'MMatrixArray', 'MObjectArray', 'MPlugArray', 'MPointArray', 'MTimeArray', 'MTrimBoundaryArray', 'MUint64Array', 'MUintArray', 'MVectorArray']
