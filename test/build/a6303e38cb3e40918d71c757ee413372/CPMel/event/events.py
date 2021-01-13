
from .. import ISDEBUG
from ..cmds.node import nodedata
from ..api import OpenMaya
from . import base
if ISDEBUG:
    reload(base)

class Dg(base.EventBase, ):

    def __init__(self):
        super(Dg, self).__init__()
        self.message_ids.append(OpenMaya.MDGMessage.addNodeAddedCallback(self.__createNode))
        self.message_ids.append(OpenMaya.MDGMessage.addNodeRemovedCallback(self.__removeNode))
        self.message_ids.append(OpenMaya.MDGMessage.addPreConnectionCallback(self.__connectMessage))
        self.message_ids.append(OpenMaya.MDGMessage.addConnectionCallback(self.__connectedMessage))

    def __createNode(self, node=OpenMaya.MObject, data=None):
        self.createNode(nodedata.Global.objToNode(node))

    def __removeNode(self, node=OpenMaya.MObject, data=None):
        self.removeNode(nodedata.Global.objToNode(node))

    def __connectedMessage(self, in_attr=OpenMaya.MPlug, out_attr=OpenMaya.MPlug, is_connect=bool, data=None):
        in_attr = nodedata.Global.plugToAttr(in_attr)
        out_attr = nodedata.Global.plugToAttr(out_attr)
        if is_connect:
            self.connected(in_attr, out_attr)
        else:
            self.disconnected(in_attr, out_attr)

    def __connectMessage(self, in_attr=OpenMaya.MPlug, out_attr=OpenMaya.MPlug, is_connect=bool, data=None):
        in_attr = nodedata.Global.plugToAttr(in_attr)
        out_attr = nodedata.Global.plugToAttr(out_attr)
        if is_connect:
            self.connect(in_attr, out_attr)
        else:
            self.disconnect(in_attr, out_attr)

    def createNode(self, node=nodedata.DgNode):
        u'\n        \u8282\u70b9\u521b\u5efa\u4e8b\u4ef6\n\n        :param node:\n        :return:\n        '
        pass

    def removeNode(self, node=nodedata.DgNode):
        u'\n        \u8282\u70b9\u79fb\u9664\u4e8b\u4ef6\n\n        :param node:\n        :return:\n        '
        pass

    def connect(self, in_attr=nodedata.AttrObject, out_attr=nodedata.AttrObject):
        u'\n        \u5c5e\u6027\u8fde\u63a5\u4e8b\u4ef6\n\n        :param in_attr:\n        :param out_attr:\n        :return:\n        '
        pass

    def disconnect(self, in_attr=nodedata.AttrObject, out_attr=nodedata.AttrObject):
        u'\n        \u5c5e\u6027\u65ad\u5f00\u8fde\u63a5\u4e8b\u4ef6\n\n        :param in_attr:\n        :param out_attr:\n        :return:\n        '
        pass

    def connected(self, in_attr=nodedata.AttrObject, out_attr=nodedata.AttrObject):
        u'\n        \u5c5e\u6027\u8fde\u63a5\u7ed3\u675f\u4e8b\u4ef6\n\n        :param in_attr:\n        :param out_attr:\n        :return:\n        '
        pass

    def disconnected(self, in_attr=nodedata.AttrObject, out_attr=nodedata.AttrObject):
        u'\n        \u5c5e\u6027\u65ad\u5f00\u8fde\u63a5\u7ed3\u675f\u4e8b\u4ef6\n\n        :param in_attr:\n        :param out_attr:\n        :return:\n        '
        pass

class Dag(Dg, ):

    def __init__(self):
        super(Dag, self).__init__()
        self.message_ids.append(OpenMaya.MDagMessage.addParentAddedCallback(self.__moveLevel))

    def __moveLevel(self, child=OpenMaya.MDagPath, parent=OpenMaya.MDagPath, data=None):
        self.moveLevel(nodedata.newObject(child.fullPathName()), nodedata.newObject(parent.fullPathName()))

    def moveLevel(self, child=nodedata.DagNode, parent=nodedata.DagNode):
        u'\n        \u5c42\u7ea7\u79fb\u52a8\n\n        :param child:\n        :param parent:\n        :return:\n        '
        pass

class Select(base.EventBase, ):

    def __init__(self):
        super(Select, self).__init__()
        self.message_ids.append(OpenMaya.MEventMessage.addEventCallback(u'SelectionChanged', self.__selected))

    def __selected(self, data=None):
        self.selected()

    def selected(self):
        u'\n        \u9009\u62e9\u4e8b\u4ef6\n\n        :return:\n        '
        pass
