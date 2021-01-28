
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import warnings
from .. import ISDEBUG
if ISDEBUG:
    from . import node
    from . import FrontPackage
    from . import static_cmds
    from . import AfterPackage
    from . import melproc
    reload(node)
    reload(FrontPackage)
    reload(static_cmds)
    reload(AfterPackage)
    reload(melproc)
from . import node
from .node.basedata import *
from .node.nodedata import newObject, Global, Components1Base, Components2Base, Components3Base
from .FrontPackage import *
from .static_cmds import *
from .AfterPackage import *
from ..core import addCommand, Command
from .melproc import mel
from ..core import *

def upcommands():

    def _(v):
        if (v is None):
            return []
        return v
    commands = {t for i in _(cmds.pluginInfo(q=True, ls=True)) for t in ((_(cmds.pluginInfo(i, q=True, c=True)) + _(cmds.pluginInfo(i, q=True, cnc=True))) + _(cmds.pluginInfo(i, q=True, ctc=True)))}
    module = globals()
    cpmel_commands = set(module.keys())
    for i in (commands - cpmel_commands):
        try:
            module[i] = node.commandWrap(getattr(cmds, i))
        except KeyError as ex:
            warnings.warn(((u'\u6ce8\u518c\u65b0CPMel\u547d\u4ee4\u5931\u8d25\uff01' + str(ex)) + u'\n'))
