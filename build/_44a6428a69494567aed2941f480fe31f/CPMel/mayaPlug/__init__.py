
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
from .. import MAYAPLUG
import maya.cmds as cmds
PLUG_Path = u'{}\\MeldoIt.py'.format(MAYAPLUG)
PLUG_NAME = (u'CPMel_' + str(hash(MAYAPLUG)).replace(u'-', u'_'))
from .. import ISDEBUG
if ISDEBUG:
    if cmds.pluginInfo(PLUG_NAME, query=True, loaded=True):
        cmds.unloadPlugin(PLUG_NAME)
if (not cmds.pluginInfo(PLUG_NAME, query=True, loaded=True)):
    cmds.loadPlugin(PLUG_Path, n=PLUG_NAME)
import sys
CPMeldoIt_Name = str(sys.cpmel_data.get(u'CPMeldoIt'))
