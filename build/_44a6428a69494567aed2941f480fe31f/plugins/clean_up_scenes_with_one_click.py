
u'\n:\u521b\u5efa\u65f6\u95f4: 2021/1/21 22:33\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\u4e00\u952e\u6e05\u7406\u573a\u666f\n'
from _44a6428a69494567aed2941f480fe31f.CPMel.cmds import *

def init():
    pass

def doit():
    sel = selected()
    try:
        mel.DeleteAllHistory()
        select(cl=True)
        select(ls('*', type='transform'), r=True)
        makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
        mel.CenterPivot()
        mel.DeleteAllHistory()
    except Exception as ex:
        raise CPMelToolError(str(ex))
    finally:
        select([i for i in sel if objExists(i)], r=True)

def name():
    return u'\u4e00\u952e\u6e05\u7406\u573a\u666f'
