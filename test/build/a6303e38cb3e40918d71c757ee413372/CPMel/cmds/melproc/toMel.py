
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import array
from ...cmds.node import nodedata
from ... import core as cmcore

def toString(val):
    return (u'"%s"' % unicode(val))

def toInt(val):
    return str(val)

def toFloat(val):
    return str(val)

def toMel(val):
    if isinstance(val, nodedata.CPObject):
        val = val.compile()
    if isinstance(val, nodedata.BaseData):
        val = val.compile()
    for i in object_mel_type:
        if isinstance(val, i):
            return object_mel_type[i](val)
    raise cmcore.CPMelError(u'\u65e0\u6cd5\u6b63\u786e\u8f6c\u5316\u8f93\u5165')

def toArray(val):
    return ('{%s}' % ','.join([toMel(i) for i in val]))
object_mel_type = {basestring: toString, int: toInt, float: toFloat, tuple: toArray, list: toArray, array.array: toArray}
