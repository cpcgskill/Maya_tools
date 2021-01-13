
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import functools

def newClass(name, bases, attrs):
    u'\n    \u6784\u5efa\u5143\u7c7b\u4f7f\u7528\u6b64\u5143\u7c7b\u7684\u7c7b\u5728\u521b\u5efa\u65f6\u81ea\u52a8\u521b\u5efa\u5bf9\u8c61\n\n    :param name:\n    :param bases:\n    :param attrs:\n    :return:\n    '
    cls = type(name, bases, attrs)
    return cls()

def createClass(name, bases, attrs):
    u'\n    \u521b\u5efa\u5668\u5143\u7c7b\n    \u4ee5\u6b64\u4e3a\u5143\u7c7b\u7684\u7c7b\u5728\u521b\u5efa\u65f6\u5c06\u4e0d\u4f1a\u81ea\u52a8\u8c03\u7528__init__\n\n    :param name:\n    :param bases:\n    :param attrs:\n    :return:\n    '
    cls = type(name, bases, attrs)
    return functools.partial(cls.__new__, cls)
