
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
from . import __OpenMayaAnim__ as OpenMayaAnim
from .__ALL import MAyyayIt

class MAnimCurveClipboardItemArray(OpenMayaAnim.MAnimCurveClipboardItemArray, ):

    def __len__(self):
        return self.length()

    def __iter__(self):
        return MAyyayIt(self)

    def __repr__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__repr__(i) for i in self]))

    def __str__(self):
        return '{}[{}]'.format(str(self.__class__), ', '.join([i.__class__.__str__(i) for i in self]))
__all__ = ['MAnimCurveClipboardItemArray']
