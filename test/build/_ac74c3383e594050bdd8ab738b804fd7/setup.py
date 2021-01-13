
import sys
import _ac74c3383e594050bdd8ab738b804fd7
_ac74c3383e594050bdd8ab738b804fd7.setup = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/12/30 21:55\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
import json
from _ac74c3383e594050bdd8ab738b804fd7.CPMel.ui import *

class MainWindow(QDialog, ):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(u'setup')
        self.setMinimumSize(QSize(200, 200))
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setMargin(0)
        self._main_layout.setSpacing(2)
        up_setup_bn = QPushButton(u'\u4fdd\u5b58\u8bbe\u7f6e')
        up_setup_bn.clicked.connect(self.upSetup)
        self._main_layout.addWidget(up_setup_bn)

    def upSetup(self, *args):
        self.close()
win = None

def show(parent=None):
    win = MainWindow(parent)
    win.exec_()
