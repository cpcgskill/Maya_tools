
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'
import maya.cmds as cmds
from ..api import OpenMayaUI
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except ImportError:
    try:
        from PySide2.QtGui import *
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *
    except ImportError:
        from PySide.QtGui import *
        from PySide.QtCore import *
try:
    from shiboken2 import *
except ImportError:
    from shiboken import *
try:
    mui = wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QWidget)
except:
    mui = None
deleteWidget = delete

class CPwindow(QWidget, ):

    @staticmethod
    def newMui():
        win = cmds.window()
        return wrapInstance(long(OpenMayaUI.MQtUtil.findWindow(win)), QWidget)

    def __init__(self):
        self.maya_window = self.newMui()
        self._main_layout = QVBoxLayout(self.maya_window)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        super(CPwindow, self).__init__()
        self._main_layout.addWidget(self)
        self.main_layout = QVBoxLayout(self)

    def show(self):
        super(CPwindow, self).show()
        self.maya_window.show()

    def close(self):
        super(CPwindow, self).close()
        self.maya_window.close()

    def setWindowTitle(self, p_str):
        self.maya_window.setWindowTitle(p_str)

    def windowTitle(self):
        return self.maya_window.windowTitle()

    def setWindowIcon(self, icon):
        return self.maya_window.setWindowIcon(icon)

    def windowIcon(self):
        return self.maya_window.windowIcon()

    def resize(self, size):
        self.maya_window.resize(size)

    def size(self):
        return self.maya_window.size()

    def paintEvent(self, event):
        super(CPwindow, self).resize(self.maya_window.size())

    def deleteWindow(self):
        super(CPwindow, self).close()
        delete(self.maya_window)

class CPQWindow(QWidget, ):
    u'\n    \u7531CPMel\u91cd\u5efa\u7684QWidget\u5bf9\u8c61\u53ef\u4ee5\u81ea\u52a8\u7684\u5c06\u81ea\u8eab\u8bbe\u7f6e\u4e3aMaya\u4e3b\u7a97\u53e3\u7684\u5b50\u5bf9\u8c61\n\n    '

    def __init__(self, *args):
        super(CPQWindow, self).__init__(*args)
        self.setParent(mui)
        self.setWindowFlags(Qt.Window)
        self.main_layout = QVBoxLayout(self)

    def deleteWindow(self):
        super(CPQWindow, self).close()
        delete(self)

class CPQWidget(QWidget, ):
    u'\n    \u5bf9CPQWindow\u7684\u91cd\u5199\n    \u4e0d\u518d\u6784\u5efaself.main_layout\n    '

    def __init__(self, *args):
        super(CPQWidget, self).__init__(*args)
        self.setParent(mui)
        self.setWindowFlags(Qt.Window)

    def deleteWindow(self):
        super(CPQWidget, self).close()
        delete(self)

class FrameBlock(QWidget, ):
    u'\n    \u53ef\u6298\u53e0\u6846\u67b6\u5b9e\u73b0\n\n    '

    class Bn(QPushButton, ):

        def __init__(self, *args):
            super(FrameBlock.Bn, self).__init__()
            self.__is_turn_on = False

            def _(*args):
                self.__is_turn_on = (not self.__is_turn_on)
            self.clicked.connect(_)
            self.setStyleSheet('text-align: left;')
            self.setMaximumHeight(20)

        def setIsTurnOn(self, bool):
            self.__is_turn_on = bool

        def isTurnOn(self):
            return self.__is_turn_on

    class Block(QWidget, ):

        def __init__(self, widget=QWidget):
            super(FrameBlock.Block, self).__init__()
            self.main_layout = QVBoxLayout(self)
            self.main_layout.addWidget(widget)

        def paintEvent(self, event):
            super(FrameBlock.Block, self).paintEvent(event)
            p = QPainter(self)
            p.setPen(Qt.NoPen)
            p.setBrush(QBrush(QColor(0, 0, 0, 15)))
            p.drawRoundRect(self.rect(), 5, 5)
            p.end()

    def __init__(self, name, widget, status=False):
        u'\n\n\n        :param name: \u6807\u9898\n        :param widget: QWidget \u5bf9\u8c61\n        :param status: \u9ed8\u8ba4\u72b6\u6001\n        '
        super(FrameBlock, self).__init__()
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.__bn = FrameBlock.Bn()
        self.__bn.setIsTurnOn(status)
        self.name = name
        self.__bn.clicked.connect(self.upwidget)
        self.main_layout.addWidget(self.__bn)
        self.widget = FrameBlock.Block(widget)
        self.main_layout.addWidget(self.widget)
        self.upwidget()

    def unfold(self):
        self.__bn.setIsTurnOn(True)
        self.upwidget()

    def fold(self):
        self.__bn.setIsTurnOn(False)
        self.upwidget()

    def upwidget(self, *args):
        if self.__bn.isTurnOn():
            self.__bn.setText(self.name)
            self.widget.show()
        else:
            self.__bn.setText((self.name + u'...'))
            self.widget.close()

def getFileName():
    u'\n    \u83b7\u5f97\u6587\u4ef6\u8def\u5f84\n\n    :return: unicode is None\n    '
    path = QFileDialog.getOpenFileName()
    if (len(path) < 3):
        return None
    return path

def getDirectoryName():
    u'\n    \u83b7\u5f97\u6587\u4ef6\u5939\u8def\u5f84\n\n    :return: unicode is None\n    '
    path = QFileDialog.getExistingDirectory()
    if (len(path) < 3):
        return None
    return path

def input(title=u'\u8f93\u5165', message=u'>>>', text=u''):
    u'\n    \u521b\u5efa\u4e00\u4e2a\u63a5\u53d7\u5b57\u7b26\u4e32\u8f93\u5165\u7684\u8f93\u5165\u6846\n\n    :param title: \u6807\u9898\n    :param message: \u6d88\u606f\n    :param text: \u9ed8\u8ba4\u53c2\u6570\n    :return: unicode is None\n    '
    (v, is_ok) = QInputDialog.getText(mui, title, message, text)
    if is_ok:
        return v
    return None

def inputInt(title=u'\u8f93\u5165', message=u'>>>', text=0):
    u'\n    \u521b\u5efa\u4e00\u4e2a\u63a5\u53d7\u6574\u6570\u8f93\u5165\u7684\u8f93\u5165\u6846\n\n    :param title: \u6807\u9898\n    :param message: \u6d88\u606f\n    :param text: \u9ed8\u8ba4\u53c2\u6570\n    :return: unicode is None\n    '
    (v, is_ok) = QInputDialog.getInt(mui, title, message, text)
    if is_ok:
        return v
    return None

def inputDouble(title=u'\u8f93\u5165', message=u'>>>', text=0.0):
    u'\n    \u521b\u5efa\u4e00\u4e2a\u63a5\u53d7\u6d6e\u70b9\u8f93\u5165\u7684\u8f93\u5165\u6846\n\n    :param title: \u6807\u9898\n    :param message: \u6d88\u606f\n    :param text: \u9ed8\u8ba4\u53c2\u6570\n    :return: unicode is None\n    '
    (v, is_ok) = QInputDialog.getDouble(mui, title, message, text)
    if is_ok:
        return v
    return None

def inputFloat(title=u'\u8f93\u5165', message=u'>>>', text=0.0):
    u'\n    \u521b\u5efa\u4e00\u4e2a\u63a5\u53d7\u6d6e\u70b9\u8f93\u5165\u7684\u8f93\u5165\u6846\n\n    :param title: \u6807\u9898\n    :param message: \u6d88\u606f\n    :param text: \u9ed8\u8ba4\u53c2\u6570\n    :return: unicode is None\n    '
    return inputDouble(title, message, text)

def inputMultiLineText(title=u'\u8f93\u5165', message=u'>>>', text=u''):
    u'\n    \u521b\u5efa\u4e00\u4e2a\u63a5\u53d7\u5b57\u7b26\u4e32\u8f93\u5165\u7684\u591a\u884c\u8f93\u5165\u6846\n\n    :param title: \u6807\u9898\n    :param message: \u6d88\u606f\n    :param text: \u9ed8\u8ba4\u53c2\u6570\n    :return: unicode is None\n    '
    (v, is_ok) = QInputDialog.getMultiLineText(mui, title, message, text)
    if is_ok:
        return v
    return None

def confirm(title=u'\u786e\u8ba4', message=u''):
    u'\n    \u786e\u8ba4\u5bf9\u8bdd\u6846\n\n    :param title: \u6807\u9898\n    :param message: \u6d88\u606f\n    :return: bool\n    '
    reply = QMessageBox.question(mui, title, message, (QMessageBox.Yes | QMessageBox.No), QMessageBox.No)
    if (reply == QMessageBox.StandardButton.No):
        return False
    else:
        return True
