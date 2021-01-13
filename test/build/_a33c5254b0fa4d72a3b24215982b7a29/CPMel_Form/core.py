
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/11/9 11:07\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.core import CPMelToolError
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.tool import decode, undoBlock
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.ui import *
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.api.OpenMaya import MGlobal
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel_Form import *
ICON = (PATH + u'/icon.ico')
QSS = (PATH + u'/qss.qss')
HEAD = (PATH + u'/head.png')

class HeadPixButton(QPushButton, ):

    def __init__(self, parent=None):
        super(HeadPixButton, self).__init__(parent)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = QLabel()
        pix = QPixmap(HEAD)
        head_label.setPixmap(pix)
        self._main_layout.addWidget(head_label)
        self.setFixedSize(pix.size())
        self.clicked.connect((lambda *args: QDesktopServices.openUrl(QUrl(u'https://www.cpcgskill.com'))))

    def paintEvent(self, event):
        pass

class Head(QWidget, ):

    def __init__(self, parent=None):
        super(Head, self).__init__(parent)
        self.setFixedHeight(36)
        self._main_layout = QHBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        head_label = HeadPixButton()
        self._main_layout.addWidget(head_label)
        self._main_layout.addStretch(0)

class Main(CPQWidget, ):

    def __init__(self, icon=ICON, title=u'CPWindow', form=tuple(), func=(lambda *args: 0)):
        icon = decode(icon)
        title = decode(title)
        self.func = undoBlock(func)
        super(Main, self).__init__()
        with open(QSS, 'r') as f:
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
            widget = i[0](*i[1:])
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
        self.doIt_bn = QPushButton(u'\u786e\u8ba4\u8868\u5355\u5df2\u586b\u5145-\u6267\u884c')
        self.doIt_bn.clicked.connect(undoBlock(self.doIt))
        self._main_layout.addWidget(self.doIt_bn)
        self._main_layout.addWidget(QLabel(u'\u672c\u7a97\u53e3\u754c\u9762\u7531CPMel_Form1.0\u5f00\u53d1'))

    def doIt(self, *args):
        value = [i.run() for i in self.weidgets]
        self.func(*value)

    def closeEvent(self, *args, **kwargs):
        for (k, v) in apps.items():
            if (v == self):
                apps.pop(k)
        deleteWidget(self)
apps = dict()

def build(icon=ICON, title=u'CPWindow', form=tuple(), func=(lambda *args: 0)):
    u'\n    build\u51fd\u6570\u63d0\u4f9b\u5c06\u8868\u5355(\u5217\u8868 or \u5143\u7ec4)\u7f16\u8bd1\u4e3a\u754c\u9762\u7684\u529f\u80fd\n\n    :param icon: \u56fe\u6807\u8def\u5f84\n    :param title: \u6807\u9898\n    :param form: \u8868\u5355\n    :param func: \u6267\u884c\u51fd\u6570 func(\u8868\u5355\u7ed3\u679c1, \u8868\u5355\u7ed3\u679c2, ...)\n    :return:\n    '
    if (hash(title) in apps):
        main_widget = apps[hash(title)]
        main_widget.close()
    import os
    if (not os.path.isfile(icon)):
        icon = ICON
        MGlobal.displayWarning(u'\u56fe\u6807\u8def\u5f84\u4e0d\u5b58\u5728')
    main_widget = Main(icon, title, form, func)
    main_widget.show()
    main_widget.update()
    main_widget.setFixedHeight(main_widget.height())
    apps[hash(title)] = main_widget
