#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:07
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPMel.core import CPMelToolError
from CPMel.tool import decode, undoBlock
from CPMel.ui import *
from CPMel.api.OpenMaya import MGlobal
from CPMel_Form import *

ICON = PATH + u"/icon.ico"
QSS = PATH + u"/qss.qss"
HEAD = PATH + u"/head.png"


class HeadPixButton(QPushButton):
    def __init__(self, parent=None):
        super(HeadPixButton, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = QLabel()
        pix = QPixmap(HEAD)
        head_label.setPixmap(pix)
        self._main_layout.addWidget(head_label)
        self.setFixedSize(pix.size())
        self.clicked.connect(lambda *args: QDesktopServices.openUrl(QUrl(u'https://www.cpcgskill.com')))

    def paintEvent(self, event):
        pass


class Head(QWidget):
    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.setFixedHeight(36)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = HeadPixButton()
        self._main_layout.addWidget(head_label)
        self._main_layout.addStretch(0)


class Main(CPQWidget):
    def __init__(self, icon=ICON, title=u"CPWindow", form=tuple(), func=lambda *args: 0):
        icon = decode(icon)
        title = decode(title)
        self.func = undoBlock(func)
        super(Main, self).__init__()
        with open(QSS, "r") as f:
            self.setStyleSheet(f.read())
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(icon))
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(5)
        self._main_layout.setSpacing(2)

        self._head = Head(self)
        self._main_layout.addWidget(self._head)

        self.weidgets = list()
        for i in form:
            widget = i[0](*(i[1:]))
            self._main_layout.addWidget(widget)
            self.weidgets.append(widget)
        h_line = QFrame(self)
        h_line.setFrameShape(QFrame.HLine)
        self._main_layout.addWidget(h_line)
        for i in range(3):
            self._main_layout.addStretch(0)
            h_line = QFrame(self)
            h_line.setFrameShape(QFrame.HLine)
            self._main_layout.addWidget(h_line)
        self.doIt_bn = QPushButton(u"确认表单已填充-执行")
        self.doIt_bn.clicked.connect(undoBlock(self.doIt))
        self._main_layout.addWidget(self.doIt_bn)
        self._main_layout.addWidget(QLabel(u"本窗口界面由CPMel_Form1.0开发"))

    def doIt(self, *args):
        value = [i.run() for i in self.weidgets]
        self.func(*value)

    def closeEvent(self, *args, **kwargs):
        for k, v in apps.items():
            if v == self:
                apps.pop(k)
        deleteWidget(self)


apps = dict()


def build(icon=ICON, title=u"CPWindow", form=tuple(), func=lambda *args: 0):
    u"""
    build函数提供将表单(列表 or 元组)编译为界面的功能

    :param icon: 图标路径
    :param title: 标题
    :param form: 表单
    :param func: 执行函数 func(表单结果1, 表单结果2, ...)
    :return:
    """
    if hash(title) in apps:
        main_widget = apps[hash(title)]
        main_widget.close()
    import os
    if not os.path.isfile(icon):
        icon = ICON
        MGlobal.displayWarning(u"图标路径不存在")
    main_widget = Main(icon, title, form, func)
    main_widget.show()
    main_widget.update()
    main_widget.setFixedHeight(main_widget.height())
    apps[hash(title)] = main_widget
