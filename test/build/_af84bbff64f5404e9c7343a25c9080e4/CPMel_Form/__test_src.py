
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/11/9 11:24\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
import _af84bbff64f5404e9c7343a25c9080e4.CPMel_Form as CPMel_Form, _af84bbff64f5404e9c7343a25c9080e4.CPMel_Form as _
reload(CPMel_Form)
import _af84bbff64f5404e9c7343a25c9080e4.CPMel_Form as CPMel_Form, _af84bbff64f5404e9c7343a25c9080e4.CPMel_Form.item as _
reload(CPMel_Form.item)
from _af84bbff64f5404e9c7343a25c9080e4.CPMel_Form import build, item

def test(*args):
    print args
ui = ((item.Text, u'Test1'), (item.Select, u'Test1'), (item.SelectList,), (item.Is, u'\u786e\u8ba4', True))
build(title=u'CPMel_Form\u6d4b\u8bd5', form=ui, func=test)