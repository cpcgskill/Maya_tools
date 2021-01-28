
u'\n:\u521b\u5efa\u65f6\u95f4: 2021/1/21 22:16\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _44a6428a69494567aed2941f480fe31f.CPMel_Form import build, item
from _44a6428a69494567aed2941f480fe31f.CPMel.cmds import *
from _44a6428a69494567aed2941f480fe31f.CPMel.api.OpenMaya import MGlobal
ui = ([item.Help, u'\u9009\u62e9\u9700\u8981\u9501\u5b9a\u7684\u8282\u70b9\uff0c\u7136\u540e\u63d0\u4ea4'],)

def main(*args):
    sel = selected()
    for i in sel:
        lockNode(i, lock=True, ic=True)

def init():
    print u'mesh mirror inspection'

def doit():
    build(form=ui, func=main, title=name(), doit_text=u'\u6267\u884c')

def name():
    return u'\u8282\u70b9\u9501\u5b9a\u5de5\u5177'
