
import sys
import _e5cb8849a8e74c07aaf094a6518fe1a0
_e5cb8849a8e74c07aaf094a6518fe1a0.CPMel_Form = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/11/9 11:01\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n*\u5173\u4e8e\u672c\u5e93:\n    \u672c\u5e93\u57fa\u4e8eCPMel2.5\u7248\u672c\u5f00\u53d1\u8bf7\u786e\u4fdd\u4f60\u7684\u73af\u5883\u91cc\u6709\u8fd9\u4e2a\u5e93\n    :\u4e0b\u8f7d\u94fe\u63a5: https://www.cpcgskill.com/cpmel\n    \u672c\u5e93\u7684\u8bbe\u5b9a\u662f\u53ef\u4ee5\u4ee5\u5c3d\u53ef\u80fd\u5feb\u7684\u901f\u5ea6\u5b8c\u6210\u754c\u9762\u5f00\u53d1\u3002\n    \u4ee5\u4e0a\u786e\u8ba4\u9700\u8981\u4f7f\u7528\u8fd9\u4e2a\u5e93\u4e4b\u540e\u5f80\u4e0b\n\n*\u4e00\u4e2a\u7b80\u5355\u7684\u6848\u4f8b:\nfrom CPMel_Form import build, item\ndef test(*args):\n    print args\nui = (\n    (item.Text, u"Test1"),\n    (item.Select, u"Test1"),\n    (item.SelectList, ),\n)\nbuild(u\'TestAPP\', form=ui, func=test)\n*ui\u5143\u7ec4:\n    \u4ece\u4e0a\u9762\u53ef\u4ee5\u770b\u5230ui\u53d8\u91cf\u4e2d\u6ca1\u4e00\u4e2a\u5143\u7d20\u90fd\u662f\u4e00\u4e2a\u5143\u7ec4\u5176\u4e2d\u7b2c\u4e00\u4e2a\u90fd\u662fCPMel_Form.item\u6a21\u5757\u4e0b\u7684\u5c5e\u6027\u8fd9\u4e2a\u662f\u7528\u6765\u6307\u5b9a\u6784\u5efa\u4ec0\u4e48\u7ec4\u4ef6\u7684,\n    \u4f8b\u5982item.Text\u5c06\u4f1a\u6784\u5efa\u4e00\u4e2a\u6587\u672c\u8f93\u5165\u6846\u5177\u4f53\u89c1\u6700\u540e\u4ecb\u7ecd\n    \u800c\u4e4b\u540e\u7684\u53c2\u6570\u7686\u4e3a\u53c2\u6570\n    \u4f8b\u5982(item.Text, u"Test1")\u4e2du\u201cTest1\u201d\u5c31\u4f1a\u6307\u5b9a\u9ed8\u8ba4\u503c\n*build\u51fd\u6570:\n    \u4ece\u4e0a\u9762\u53ef\u4ee5\u770b\u5230build\u63d0\u4f9b\u4e86\u5c06\u4e00\u4e2a\u5143\u7ec4\u8f6c\u5316\u4e3a\u754c\u9762\u7684\u529f\u80fd\n    *\u4ee5\u4e0b\u662fbuild\u51fd\u6570\u7684\u4ecb\u7ecd\uff1a\n        build\u51fd\u6570\u63d0\u4f9b\u5c06\u8868\u5355(\u5217\u8868 or \u5143\u7ec4)\u7f16\u8bd1\u4e3a\u754c\u9762\u7684\u529f\u80fd\n\n        :param icon: \u56fe\u6807\u8def\u5f84\n        :param title: \u6807\u9898\n        :param form: \u8868\u5355\n        :param func: \u6267\u884c\u51fd\u6570 func(\u8868\u5355\u7ed3\u679c1, \u8868\u5355\u7ed3\u679c2, ...)\n        :return:\n*build\u51fd\u6570\u4e2d\u7684func:\n    \u8f93\u5165\u7684\u6267\u884c\u51fd\u6570\u4f1a\u5728\u7528\u6237\u5bf9\u8868\u5355\u586b\u5145\u5b8c\u6210\u4e4b\u540e\u7531\u7528\u6237\u4e3b\u52a8\u6267\u884c\u3002\n    \u8fd9\u4e2a\u51fd\u6570\u9700\u8981\u63a5\u53d7\u4e0e\u8f93\u5165\u7684\u8868\u5355\u5bf9\u5e94\u7684\u53c2\u6570\uff0c\u6bcf\u4e00\u4e2a\u7ec4\u4ef6\u63d0\u4f9b\u4e00\u4e2a\u53c2\u6570\u3002\n    \u6bcf\u4e2a\u7ec4\u4ef6\u5bf9\u5e94\u4ec0\u4e48\u503c\u89c1\u6700\u540e\n*\u7ec4\u4ef6:\n    \u5728CPMel_Form\u4e2d\u6bcf\u4e00\u4e2a\u7ec4\u4ef6\u5bf9\u5e94\u4e00\u4e2a\u7a97\u53e3\u7ec4\u4ef6\u4e0e\u6267\u884c\u51fd\u6570\u53c2\u6570\u4ee5\u4e0b\u4e3a\u5bf9\u5e94\u5217\u8868\uff1a\n    item.Text \u4e00\u4e2a\u6587\u672c\u8f93\u5165\u6846 unicode\u5b57\u7b26\u4e32  \u53c2\u6570 \u53ef\u9009\u7684\u9ed8\u8ba4\u5b57\u7b26\u4e32\n    item.Select \u4e00\u4e2a\u63a5\u53d7\u9009\u62e9\u7684\u6587\u672c\u8f93\u5165\u6846 unicode\u5b57\u7b26\u4e32 \u53c2\u6570 \u53ef\u9009\u7684\u9ed8\u8ba4\u5b57\u7b26\u4e32\n    item.SelectList \u4e00\u4e2a\u63a5\u53d7\u9009\u62e9\u5217\u8868\u7684\u591a\u884c\u6587\u672c\u8f93\u5165\u6846 unicode\u5b57\u7b26\u4e32\u5217\u8868 \u53c2\u6570 \u65e0\n    item.Is \u4e00\u4e2a\u5355\u9009\u6309\u94ae True or False \u53c2\u6570 \u65e0\n'
import os
DEBUG = True
PATH = os.path.dirname(os.path.abspath(__file__))
import _e5cb8849a8e74c07aaf094a6518fe1a0.CPMel_Form.item as item
import _e5cb8849a8e74c07aaf094a6518fe1a0.CPMel_Form.core as core
if DEBUG:
    reload(item)
    reload(core)
from _e5cb8849a8e74c07aaf094a6518fe1a0.CPMel_Form.core import build
import _e5cb8849a8e74c07aaf094a6518fe1a0.CPMel_Form.item as item
