
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\u5728\u5305\u88f9\u5b8c\u6210\u4e4b\u524d\u5bfc\u5165\uff0c\u4e4b\u540e\u5c06\u4f1a\u88ab\u91cd\u65b0\u5305\u88f9\n'
from maya.cmds import *
import maya.cmds as cmds
from .node.nodedata import DagNode, AttrObject, ArrayAttrObject, UIObject
__all__ = ['spaceLocator', 'listHistory']

def spaceLocator(*args, **kwargs):
    u'\n\n    :param args:\n    :param kwargs:\n    :return:\n    :rtype: list|str|basestring|DagNode|AttrObject\n    '
    out = cmds.spaceLocator(*args, **kwargs)
    if (('q' in kwargs) or ('query' in kwargs)):
        return out
    elif isinstance(out, list):
        if (len(out) == 1):
            return out[0]
        else:
            return out
    else:
        return out

def listHistory(*args, **kwargs):
    u'\n    \u4fee\u6539\u5185\u5bb9\uff1a\n        -\u5f53\u7ed3\u679c\u4e3aNone\u65f6\u8fd4\u56de\u4e00\u4e2a\u7a7a\u5217\u8868\n        -\u5f53arg\u4e3a\u7a7a\u5217\u8868\uff0c\u5143\u7ec4\uff0c\u96c6\u5408\u6216\u7a7a\u65f6\uff0c\u5f15\u53d1RuntimeError\n         Frozenset\uff0c\u4f7f\u5176\u884c\u4e3a\u4e0e\u672a\u4f20\u9012\u65f6\u4e00\u81f4\uff0c\u6216\u8005\n         \u65e0\u53c2\u6570\u4e14\u672a\u9009\u62e9\u4efb\u4f55\u5185\u5bb9\uff08\u4ee5\u524d\u4f1a\u5f15\u53d1TypeError\uff09\n        -\u6dfb\u52a0\u4e86\u7c7b\u578b\u8fc7\u6ee4\u5668\n    :return: `CPObject` list\n    :rtype: list|str|basestring|DagNode|AttrObject\n    '
    type = None
    if ('type' in kwargs):
        type = kwargs.pop('type')
    results = cmds.listHistory(*args, **kwargs)
    if (results is None):
        return []
    if type:
        results = [i for i in results if (type in cmds.nodeType(i, inherited=True))]
    return results
