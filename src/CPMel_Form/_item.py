#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/9 11:03
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from functools import partial

import CPMel.cmds as cc
from CPMel.tool import decode, undoBlock
from CPMel.ui import *


class Object(QWidget):
    def __init__(self):
        super(Object, self).__init__()

    def run(self):
        return None




class Help(Object):
    def __init__(self, text=u""):
        text = decode(text)
        super(Help, self).__init__()
        self.setMinimumHeight(40)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setMargin(0)
        text = QLabel(text)
        text.setWordWrap(True)
        text.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(text)
        self.main_layout.addStretch(0)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(75, 75, 75)))
        p.drawRoundedRect(self.rect(), 4, 4)

    def run(self):
        return None


class Label(Object):
    def __init__(self, text=u""):
        text = decode(text)
        super(Label, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setMargin(0)
        self.main_layout.addWidget(QLabel(text))
    def run(self):
        return None


class Text(Object):
    def __init__(self, text=u""):
        text = decode(text)
        super(Text, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setMargin(0)
        self.text = QLineEdit(text)
        self.main_layout.addWidget(self.text)

    def run(self):
        return self.text.text()


class Select(Object):
    def __init__(self, text=u""):
        text = decode(text)
        super(Select, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setMargin(0)
        self.text = QLineEdit(text)
        self.load_bn = QPushButton(u"载入")
        _ = partial(self.load)
        self.load_bn.clicked.connect(lambda *args: _())
        self.main_layout.addWidget(self.text)
        self.main_layout.addWidget(self.load_bn)

    @undoBlock
    def load(self):
        sel = cc.ls(sl=True)
        if len(sel) < 1:
            raise cc.CPMelToolError(u"选择一个物体")
        self.text.setText(str(sel[0]))

    def run(self):
        return self.text.text()


class SelectList(Object):
    def __init__(self):
        super(SelectList, self).__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setMargin(0)
        self.texts = QTextEdit()
        self.load_bn = QPushButton(u"载入")
        self.load_bn.clicked.connect(lambda *args: self.load())
        self.main_layout.addWidget(self.texts)
        self.main_layout.addWidget(self.load_bn)

    @undoBlock
    def load(self):
        sel = cc.ls(sl=True)
        self.texts.setText(u"\n".join([str(i) for i in sel]))

    def run(self):
        return self.texts.toPlainText().split("\n")


class Is(Object):
    def __init__(self, info=u"", default_state=False):
        info = decode(info)
        super(Is, self).__init__()
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setMargin(0)
        self.query = QCheckBox(info, self)
        self.query.setChecked(default_state)
        self.main_layout.addWidget(self.query)

    def run(self):
        return self.query.isChecked()


class FloatSlider(Object):
    def __init__(self, min=0, max=1, def_=0):
        self.min = float(min)
        self.max = float(max)
        super(FloatSlider, self).__init__()
        self._main_layout = QHBoxLayout(self)
        self._text = QLabel()
        self._text.setFixedWidth(60)

        self._slider = QSlider(Qt.Horizontal, self)
        self._slider.setMinimum(0)
        self._slider.setMaximum(1000000)
        self._slider.sliderMoved.connect(self.updateSlider)
        self._main_layout.addWidget(self._text)
        self._main_layout.addWidget(self._slider)

        self.setText(str(def_))

    def run(self):
        return max(min(float(self.text()), self.max), self.min)

    def updateSlider(self, v):
        size = self.max - self.min
        v = max(min(float(v) / 1000000, 1), 0)
        v = (v * size) + self.min
        v = max(min(v, self.max), self.min)
        self.setText(u"%f" % v)

    def setText(self, s):
        self._text.setText(s)

    def text(self):
        return self._text.text()
