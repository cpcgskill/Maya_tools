
u"\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n* \u672c\u6a21\u5757\u63d0\u4f9b\u4e86\u5bf9Maya Api\u6570\u7ec4\u7684\u5c01\u88c5\u8ba9\u5176\u53ef\u4ee5\u987a\u5229\u7684\u878d\u5165Python\u5faa\u73af\u673a\u5236\u4e2d\n    >>> import CPMel.api as api\n    >>> api.OpenMaya.MFloatArray(10, 0)\n    <class 'CPMel.api.__OpenMaya_array__.MFloatArray'>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]\n    >>> arr = api.OpenMaya.MFloatArray(10, 0)\n    >>> [i for i in arr]\n    [<CPMel.api.__OpenMaya_it__.MItDag; proxy of <Swig Object of type 'MItDag *' at 0x0000000016A16E10> >,...]\n\n* \u4e0d\u4ec5\u5982\u6b64\u8fd8\u63d0\u4f9b\u4e86\u8fed\u4ee3\u5668\u7684\u5c01\u88c5\n    >>> from CPMel.api.OpenMaya import MItDag\n    >>> itdg = MItDag()\n    >>> [i for i in itdg] # \u6ce8\u610f\u8fed\u4ee3\u5668\u5faa\u73af\u7684 \u201ci\u201d\u662f\u8fed\u4ee3\u5668\u672c\u8eab\n\n\n"
import maya.OpenMaya
import maya.OpenMayaAnim
import maya.OpenMayaUI
import maya.OpenMayaFX
import maya.OpenMayaRender
import maya.OpenMayaMPx
del maya
from . import __OpenMaya__
from . import __OpenMaya__
from . import __OpenMayaAnim__
from . import __OpenMayaRender__
from . import __OpenMayaFX__
from . import __OpenMayaUI__
from . import __OpenMayaMPx__
from . import __OpenMaya_it__
from . import __OpenMayaAnim_it__
from . import __OpenMaya_array__
from . import __OpenMayaAnim_array__
from . import OpenMaya
from . import OpenMayaAnim
from . import OpenMayaFX
from . import OpenMayaRender
from . import OpenMayaUI
from . import OpenMayaMPx
