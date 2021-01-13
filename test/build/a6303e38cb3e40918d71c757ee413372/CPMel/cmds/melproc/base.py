
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
from collections import Iterable
from functools import partial
import maya.mel
import maya.cmds as mc
from toMel import toMel, toArray, toFloat, toInt, toString
eval = maya.mel.eval

def melProc(item, *args):
    return eval('{}({});'.format(item, ', '.join([(toArray(i) if (isinstance(i, Iterable) and (not isinstance(i, basestring))) else toMel(i)) for i in args])))

class melbase(object, ):

    def __getattribute__(self, item):
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            return partial(melProc, item)
