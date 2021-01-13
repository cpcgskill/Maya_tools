
import sys
import _310cf17ae5ee4fa4ab433b275f30c34e
_310cf17ae5ee4fa4ab433b275f30c34e.CPMel = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://www.cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n* \u83b7\u5f97\u8def\u5f84\u6a21\u5757\n    * PATH : CPMel\u6240\u5728\u8def\u5f84\n    * MAYAPLUG : CPMel\u7684Maya\u63d2\u4ef6\u6240\u5728\u8def\u5f84\n    * ISDEBUG : \u662f\u5426\u5904\u5728Debug\u6a21\u5f0f\n\n* \u5feb\u901f\u5165\u95e8:\n\n    * \u5bfc\u5165:\n        >>> import CPMel.cmds as cc\n        >>> import CPMel.tool as ctl\n    * \u547d\u4ee4:\n\n        * maya.cmds:\n            >>> import maya.cmds as cmds\n            >>> cmds.joint()\n            u"xxx"\n\n        * CPMel.cmds\n\n            >>> cc.joint()\n            joint(u"xxx")\n\n    * \u547d\u4ee4\u53c2\u6570\u8f6c\u5316\u89c4\u5219:\n\n        * CPObject = str \uff0cDouble3 = \uff08x,y,z\uff09\uff0c Matrix = (x,x,x,..*16)\n\n    * \u66f4\u52a0\u65b9\u4fbf\u7684\u521b\u5efa\u8282\u70b9\u7684\u65b9\u6cd5:\n        >>> cc.createNode.transform()\n        transform(u"transform")\n\n    * mel\u65b9\u6cd5\u8bbf\u95ee:\n        >>> cc.mel.SmoothSkinWeights()\n        None\n    * \u4e8b\u4ef6\u5f15\u64ce:\n        >>> class printDg(cevent.Dg):\n        ...     def createNode(self, node):\n        ...         print(node)\n        ...     def removeNode(self, node):\n        ...         print(node)\n\n        >>> obj = printDg()\n\n        >>> cc.createNode.transform()\n        transform1 << \u6253\u5370\n        transform(u\'transform1\')\n\n    * \u5de5\u5177:\n        >>> ctl.decode("\u4f60\u597d\u4e16\u754c")\n        u\'\u4f60\u597d\u4e16\u754c\'\n        >>> ctl.MayaObjectData(u"time1")\n        <CPMel.tool.MayaObjectData object at 0x0000000053CB32E8>\n        >>> ctl.undoBlock(xxx type = func)# Qt\u64a4\u9500\u7684\u5b9e\u73b0\n        xxx type = func\n\n    * \u89c6\u9891\u7248\u6559\u7a0b:\thttps://www.aboutcg.org/courseDetails/1031/introduce\n    * 2.5\u7248\u672c\u66f4\u65b0 \uff1a\n        * \u4f7f\u7528\u4e86\u9884\u7f16\u8bd1\u811a\u672c\u4f18\u5316\u4e86\u6587\u4ef6\u4f53\u79ef\n        * \u4fee\u590d\u4e86\u4e00\u4e9bBUG\n    * 2.6\u7248\u672c\u66f4\u65b0 \uff1a\n        * \u89e3\u51b3\u4e86qt\u9519\u8bef\u5904\u7406\u95ee\u9898\n        * \u9519\u8bef\u4e0emayaplug\u53ef\u4ee5\u8fd0\u884c\u591a\u4e2a\u4e86\n        * \u5b9e\u73b0\u4e86\u76f8\u5bf9\u8fd0\u884c\n        * \u533a\u5206debug\u7248\u4e0erelease\u7248\n        * \u53bb\u9664\u4e86static_cmds\u4e2d\u65e0\u7528\u7684\u6ce8\u91ca\n        * \u901a\u8fc7\u6587\u6863\u6ce8\u91ca\u8fdb\u884c\u7c7b\u578b\u6307\u5b9a\u4f18\u5316\u4e86\u5728pycharm\u4e2d\u7f16\u5199\u7a0b\u5e8f\u7684\u8865\u5168\u6548\u679c\n        * \u53bb\u9664\u4e86mayaPlug\u6a21\u5757\u4e0b\u65e0\u7528\u7684\u7a0b\u5e8f\n'
from . import initializeMaya
import os
import sys
import maya.cmds
sys.cpmel_data = dict()
MAYAINDEX = int(maya.cmds.about(v=True))
ISDEBUG = False
try:
    PATH = os.path.dirname(os.path.abspath(__file__))
    if (type(PATH) == str):
        try:
            PATH = PATH.decode('utf8')
        except UnicodeDecodeError:
            try:
                PATH = PATH.decode('gbk')
            except UnicodeDecodeError:
                try:
                    PATH = PATH.decode('GB18030')
                except UnicodeDecodeError:
                    try:
                        PATH = PATH.decode('GB2312')
                    except UnicodeDecodeError:
                        PATH = unicode(PATH)
    PATH = PATH.encode('utf8').decode('utf8')
except:
    PATH = os.path.dirname(os.path.abspath(__file__))
MAYAPLUG = (u'%s\\mayaPlug' % PATH)
from . import mayaPlug
from . import core
from . import api
from . import cmds
from . import event
from . import ui
from . import tool
cmds.upcommands()
maya.cmds.pluginInfo(cc=cmds.upcommands)
del maya
if hasattr(sys, 'cpmel_data'):
    del sys.cpmel_data
