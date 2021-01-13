
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import maya.cmds as cmds
from ..mayaPlug import CPMeldoIt_Name
from .error import CPMelErrorBase, CPMelScriptError, CPMelToolError, CPMelError
if hasattr(cmds, CPMeldoIt_Name):
    CPMeldoIt = getattr(cmds, CPMeldoIt_Name)
else:
    CPMeldoIt = cmds.CPMeldoIt

def defAddCommandList(doIt, undoIt):
    u'\n    \u5c06\u4e24\u4e2a\u51fd\u6570\u6dfb\u52a0\u5230\u547d\u4ee4\u961f\u5217\u91cc\n\n    :param doIt:\n    :param undoIt:\n    :return:\n    '
    if (callable(doIt) and callable(undoIt)):
        try:
            CPMeldoIt(d=id(doIt), ud=id(undoIt))
        except Exception as ex:
            raise CPMelError(u'\u6dfb\u52a0\u547d\u4ee4\u9519\u8bef')
        return
    else:
        raise CPMelError(u'doIt \u6216\u8005 undoIt \u662f\u4e0d\u53ef\u6267\u884c\u7684\u5bf9\u8c61')

def addCommand(doIt, undoIt):
    u'\n    \u5c06\u4e24\u4e2a\u51fd\u6570\u8f6c\u5316\u4e3a\u547d\u4ee4\u5e76\u6267\u884c\n\n    :param doIt:\n    :param undoIt:\n    :return:\n    '
    if (callable(doIt) and callable(undoIt)):
        try:
            CPMeldoIt(d=id(doIt), ud=id(undoIt))
        except Exception as ex:
            raise CPMelError(u'\u6dfb\u52a0\u547d\u4ee4\u9519\u8bef')
        return doIt()
    else:
        raise CPMelError(u'doIt \u6216\u8005 undoIt \u662f\u4e0d\u53ef\u6267\u884c\u7684\u5bf9\u8c61')

def addCommands(doIts, undoIts):
    u'\n    \u5c06\u4e24\u4e2a\u51fd\u6570\u5217\u8868\u8f6c\u5316\u4e3a\u547d\u4ee4\u5e76\u6267\u884c\n\n    :param doIt:\n    :param undoIt:\n    :return:\n    '

    def doIt():
        tuple((i() for i in doIts if callable(i)))

    def undoIt():
        tuple((i() for i in undoIts if callable(i)))
    try:
        CPMeldoIt(d=id(doIt), ud=id(undoIt))
    except Exception as ex:
        raise CPMelError(u'\u6dfb\u52a0\u547d\u4ee4\u9519\u8bef')
    return doIt()

class Command(object, ):
    u'\n    \u547d\u4ee4\u7c7b\n    \u793a\u4f8b\uff1a\n    class CommandTest(Command):\n        def doIt(self, *args, **kwargs):\n            print "doIt"\n\n        def redoIt(self, *args, **kwargs):\n            print "redoIt"\n            return None\n\n        def undoIt(self, *args, **kwargs):\n            print "undoIt"\n\n    '
    isundo = True

    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls)
        if self.isundo:
            self.doIt(*args, **kwargs)
            return addCommand(self.redoIt, self.undoIt)
        else:
            return self.doIt(*args, **kwargs)

    def doIt(self, *args, **kwargs):
        u'\n        \u6267\u884c\n\n        :param args:\n        :param kwargs:\n        :return:\n        '
        pass

    def redoIt(self, *args, **kwargs):
        u'\n        \u91cd\u505a\n\n        :param args:\n        :param kwargs:\n        :return:\n        '
        pass

    def undoIt(self, *args, **kwargs):
        u'\n        \u64a4\u9500\n\n        :param args:\n        :param kwargs:\n        :return:\n        '
        pass
