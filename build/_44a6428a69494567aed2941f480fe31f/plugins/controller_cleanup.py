
u'\n:\u521b\u5efa\u65f6\u95f4: 2021/1/21 13:39\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _44a6428a69494567aed2941f480fe31f.CPMel_Form import build, item
from _44a6428a69494567aed2941f480fe31f.CPMel.cmds import *
from _44a6428a69494567aed2941f480fe31f.CPMel.api.OpenMaya import MGlobal
ui = ([item.Help, u'\u7528\u4e8e\u6e05\u7406\u6a21\u578b\u7684\u8f93\u5165\u5386\u53f2'],)

def main(*args):
    sel = selected()
    select(cl=True)
    set_ints = set()
    for i in sel:
        set_ints.add(i)
        for l in listRelatives(i, s=True):
            set_ints.add(l)
            for t in listConnections(l, scn=True):
                set_ints.add(t)
        for l in listConnections(i, scn=True):
            set_ints.add(l)
    for i in set_ints:
        try:
            i.ihi.set(0)
        except:
            pass
    select(sel)
    refresh()

def init():
    print u'mesh mirror inspection'

def doit():
    build(form=ui, func=main, title=name(), doit_text=u'\u9009\u62e9\u63a7\u5236\u5668\u6267\u884c')

def name():
    return u'\u63a7\u5236\u5668\u94fe\u63a5\u9690\u85cf\u5de5\u5177'
