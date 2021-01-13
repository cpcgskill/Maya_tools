
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\nCPMel.cmds \u811a\u672c\u6a21\u5757\n'
from collections import Iterable
from collections import Iterable
import maya.cmds as mc
from ...api import OpenMaya
from ... import core as cmcore
from . import basedata
from . import nodedata
from . import nodetypes
from ...tool import decode
from .basedata import *
from .nodedata import *
from .nodetypes import *
from .nodedata import newObject
__all__ = ['CPMelToCmds', 'cmdsToCPMel', 'commandWrap']
__ToTuple__ = (list, tuple)

def CPMelToCmds(val):
    u'\n    \u7528\u4e8e\u5c06CPMel\u7684\u5bf9\u8c61\u8f6c\u5316\u4e3acmds\u53ef\u4ee5\u7406\u89e3\u7684\u503c\u7684\u51fd\u6570\n\n    :param val:\tCmds\u6a21\u5757\u8f93\u5165\u53c2\u6570\u5217\u8868\u4e2d\u7684\u5143\u7d20\n    :return: \u8f6c\u5316\u5b8c\u6210\u7684\u5bf9\u8c61\n    '
    if isinstance(val, BaseData):
        return val.compile()
    if isinstance(val, CPObject):
        return val.compile()
    for i in __ToTuple__:
        if isinstance(val, i):
            return tuple((CPMelToCmds(t) for t in val))
    return val

def cmdsToCPMel(val):
    u'\n    \u5c06cmds\u7684\u8fd4\u56de\u503c\u8f6c\u5316\u4e3aCPMel\u4f7f\u7528\u7684\u5bf9\u8c61\u7684\u51fd\u6570\n\n    :param val: Cmds\u6a21\u5757\u8fd4\u56de\u53c2\u6570\u5217\u8868\u4e2d\u7684\u5143\u7d20\n    :return: \u8f6c\u5316\u5b8c\u6210\u7684\u5bf9\u8c61\n    '
    if isinstance(val, tuple):
        if (len(val) == 3):
            try:
                return basedata.Double3(val)
            except Exception:
                return val
        return val
    if isinstance(val, basestring):
        try:
            return newObject(val)
        except Exception:
            return val
    if isinstance(val, list):
        return [cmdsToCPMel(i) for i in val]
    return val

def inCommandWrap(fn):
    u'\n    \u547d\u4ee4\u5305\u88f9\u51fd\u6570\n\n    :param fn:\n    :return:\n    '

    def test(*args, **kwargs):
        args = tuple((CPMelToCmds(i) for i in args))
        kwargs = {i: CPMelToCmds(kwargs[i]) for i in kwargs}
        try:
            return fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError((u'Command error >> ' + u'\n'.join([decode(i) for i in ex.args])))
    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test

def runCommandWrap(fn):
    u'\n    \u547d\u4ee4\u8fd4\u56de\u5305\u88f9\u51fd\u6570\n\n    :param fn:\n    :return:\n    '

    def test(*args, **kwargs):
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError((u'Command error >> ' + u'\n'.join([decode(i) for i in ex.args])))
        if (isinstance(out_args, Iterable) and (not isinstance(out_args, basestring))):
            return type(out_args)((cmdsToCPMel(i) for i in out_args))
        return cmdsToCPMel(out_args)
    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test

def runUiCommandWrap(fn):
    u'\n    gui\u547d\u4ee4\u8fd4\u56de\u503c\u5305\u88f9\u51fd\u6570\n    :param fn:\n    :return: fn\n    '

    def test(*args, **kwargs):
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError((u'Command error >> ' + u'\n'.join([decode(i) for i in ex.args])))
        if ((not ('q' in kwargs)) and (not ('query' in kwargs)) and isinstance(out_args, basestring)):
            return nodedata.UIObject(out_args)
        else:
            return out_args
    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test

def commandWrap(fn):
    u'\n    \u547d\u4ee4\u5305\u88f9\u51fd\u6570\n\n    :param fn:\n    :return:\n    '

    def test(*args, **kwargs):
        args = tuple((CPMelToCmds(i) for i in args))
        kwargs = {i: CPMelToCmds(kwargs[i]) for i in kwargs}
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError((u'Command error >> ' + u'\n'.join([decode(i) for i in ex.args])))
        if (isinstance(out_args, Iterable) and (not isinstance(out_args, basestring))):
            return type(out_args)((cmdsToCPMel(i) for i in out_args))
        return cmdsToCPMel(out_args)
    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test

def uiCommandWrap(fn):
    u'\n    gui\u547d\u4ee4\u5305\u88f9\u51fd\u6570\n    :param fn:\n    :return: fn\n    '

    def test(*args, **kwargs):
        args = tuple((CPMelToCmds(i) for i in args))
        kwargs = {i: CPMelToCmds(kwargs[i]) for i in kwargs}
        try:
            out_args = fn(*args, **kwargs)
        except Exception as ex:
            raise cmcore.CPMelError((u'Command error >> ' + u'\n'.join([decode(i) for i in ex.args])))
        if ((not ('q' in kwargs)) and (not ('query' in kwargs)) and isinstance(out_args, basestring)):
            return nodedata.UIObject(out_args)
        else:
            return out_args
    test.__name__ = fn.__name__
    test.__doc__ = fn.__doc__
    return test
