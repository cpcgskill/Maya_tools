
u'\n:\u521b\u5efa\u65f6\u95f4: 2021/1/21 22:21\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _44a6428a69494567aed2941f480fe31f.CPMel.cmds import *

def init():
    pass

def doit():
    sel = selected()
    try:
        select('*')
        all_node = selected()
        for i in all_node:
            if (not i.isDefaultNode()):
                lockNode(i, lock=True, ic=True)
    except Exception as ex:
        raise CPMelToolError(str(ex))
    finally:
        select(sel, r=True)

def name():
    return u'\u4e00\u952e\u9501\u5b9a\u573a\u666f'
