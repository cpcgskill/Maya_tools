#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/4 17:49
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import hashlib
import ast
import astunparse

func_def = \
"""
from CPMel.ui import *
from plugins.get import plugins
from setup import show as show_s
import update
import update as supdate_s
def sss():
    pass
@sss
class HeadPixButton(QPushButton):
    def __init__(self, parent=None):
        super(HeadPixButton, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = QLabel()
        pix = QPixmap(HEAD_IMG)
        head_label.setPixmap(pix)
        self._main_layout.addWidget(head_label)
        self.setFixedSize(pix.size())
        self.clicked.connect(lambda *args: QDesktopServices.openUrl(QUrl(u'https://www.cpcgskill.com')))

    def paintEvent(self, event):
        pass
"""
def hashName(s):
    v = "P" + str(hash(s)).replace("-", "_")
    print ">>", v
    return v

r_node = ast.parse(func_def)

for i in ast.walk(r_node):
    if isinstance(i, ast.ImportFrom):
        pass
    if isinstance(i, ast.Import):
        pass

for i in ast.walk(r_node):
    if isinstance(i, ast.ClassDef):
        i.name = hashName(i.name)
    if isinstance(i, ast.FunctionDef):
        i.name = hashName(i.name)
#
# visitor = CodeVisitor()
# visitor.visit(r_node)
# # print astunparse.dump(r_node)
print astunparse.unparse(r_node)
# exec compile(r_node, '<string>', 'exec')
