
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\nCPMel.cmds\u7684\u57fa\u672c\u7c7b\u578b\u5b9a\u4e49\n'
import re
import itertools
import maya.cmds as cmds
import functools
try:
    from PySide2.QtWidgets import QWidget
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtGui import QWidget
    from shiboken import wrapInstance
from ...api import OpenMaya
from ...api import OpenMayaUI
from ...api.OpenMaya import *
from ...api.OpenMayaUI import *
from ... import core as cmcore
from . import basedata
from .basedata import *
from ... import MAYAINDEX
__all__ = ['newObject', 'CPObject', 'DgNode', 'DagNode', 'AttrObject', 'ArrayAttrObject', 'UIObject', 'Components1Base', 'Components2Base', 'Components3Base', 'Global', 'ObjectMetadef', 'componentsTypesMetadef']

class Global(object, ):
    u'\n    \u5168\u5c40\u9759\u6001\u65b9\u6cd5\u7c7b\n\n    '
    DependencyNode_o = MFnDependencyNode()
    NewNodes = dict()
    new_object = None
    DependencyNodeTypes = dict()
    DgTypes = list()
    ComponentsTypes = list()
    re_object = re.compile('\\[([\\d:\\*]*?)\\]')

    @staticmethod
    def nameToApiObject(obj_name):
        u'\n        \u83b7\u5f97\u5bf9\u5e94\u7684api\u5bf9\u8c61\n\n        :param obj_name: \u5bf9\u8c61\u540d\u79f0\u5b57\u7b26\u4e32\n        :return: MObject or (MObject, MPlug) or (MObject, MObject)\n        '
        sel = MSelectionList()
        try:
            sel.add(obj_name)
        except Exception:
            if ('.' in obj_name):
                try:
                    buf = obj_name.split('.')
                    obj = Global.nameToApiObject(buf[0])
                    mfn = MFnDependencyNode(obj)
                    plug = mfn.findPlug(buf[(-1)], False)
                    return (obj, plug)
                except (RuntimeError, ValueError):
                    pass
            return None
        else:
            if (sel.length() != 1):
                return None
            if ('.' in obj_name):
                try:
                    plug = MPlug()
                    sel.getPlug(0, plug)
                    return (plug.node(), plug)
                except RuntimeError:
                    dag = MDagPath()
                    comp = MObject()
                    try:
                        sel.getDagPath(0, dag, comp)
                    except RuntimeError:
                        pass
                    if (not comp.isNull()):
                        return (dag.node(), comp)
                    splitName = obj_name.split('.')
                    if (len(splitName) == 2):
                        obj = MObject()
                        try:
                            sel.add(splitName[0])
                            sel.getDependNode(1, obj)
                        except RuntimeError:
                            pass
                        else:
                            mfn = MFnDependencyNode(obj)
                            aliases = []
                            if mfn.getAliasList(aliases):
                                this_iter = iter(aliases)
                                for (aliasName, trueName) in itertools.izip(this_iter, this_iter):
                                    if (aliasName == splitName[1]):
                                        return Global.nameToApiObject('.'.join((splitName[0], trueName)))
            else:
                obj = MObject()
                sel.getDependNode(0, obj)
                return obj

    @staticmethod
    def nameToMObject(obj_name):
        sel = MSelectionList()
        sel.add(obj_name)
        obj = MObject()
        sel.getDependNode(0, obj)
        return obj

    @staticmethod
    def nameToMDagPath(obj_name):
        sel = MSelectionList()
        sel.add(obj_name)
        path = MDagPath()
        obj = MObject()
        sel.getDagPath(0, path, obj)
        return (path, obj)

    @staticmethod
    def nameToComponentsMObject(obj_name):
        sel = MSelectionList()
        sel.add(obj_name)
        obj = MObject()
        sel.getDagPath(0, MDagPath(), obj)
        return obj

    @staticmethod
    def objToNode(obj):
        u'\n        \u5c06Maya\u5bf9\u8c61\u8f6c\u5316\u4e3aNode\n        :param obj: MObject\n        :return:\n        '
        Global.DependencyNode_o.setObject(obj)
        uuid = Global.DependencyNode_o.uuid()
        uuid_s = uuid.asString()
        try:
            return Global.NewNodes[uuid_s]
        except KeyError:
            pass
        api_type = obj.apiType()
        try:
            o = Global.DependencyNodeTypes[api_type](obj, uuid, uuid_s)
            Global.NewNodes[uuid_s] = o
            return o
        except KeyError:
            for i in Global.DgTypes:
                if obj.hasFn(i):
                    cla = Global.DependencyNodeTypes[i]
                    Global.DependencyNodeTypes[api_type] = cla
                    o = cla(obj, uuid, uuid_s)
                    Global.NewNodes[uuid_s] = o
                    return o
            raise cmcore.CPMelError(u'\u627e\u4e0d\u5230\u5bf9\u5e94\u7684\u8282\u70b9\u7c7b\u578b')

    @staticmethod
    def nameToObject(name):
        return newObject(name)

    @staticmethod
    def nameToNode(name):
        u'\n        \u521b\u5efa\u4e00\u4e2a\u8282\u70b9\u5bf9\u8c61\u6839\u636e\u4e0d\u540c\u7684\u8282\u70b9\u521b\u5efa\u4e0d\u540c\u7684\u5bf9\u8c61\u7684\u65b9\u6cd5\n\n        :param name: Str \u6216 Unicode \u8f93\u5165\u7684\u8282\u70b9\u540d\u79f0\n        :return:\n        '
        try:
            obj = Global.nameToMObject(name)
        except RuntimeError:
            raise cmcore.CPMelError(u'\u8282\u70b9\u4e0d\u5b58\u5728')
        return Global.objToNode(obj)

    @staticmethod
    def nameToAttr(attr_name):
        u'\n        \u521b\u5efaAttrObject\u5bf9\u8c61\n\n        :param name: Str \u6216 Unicode \u8f93\u5165\u7684\u5c5e\u6027\u540d\u79f0\n        :return:\n        :rtype:AttrObject|ArrayAttrObject\n        '
        names = attr_name.split('.')
        node = Global.nameToNode(names[0])
        current_obj = node
        for i in names[1:]:
            current_obj = current_obj.attr(i)
        return current_obj

    @staticmethod
    def nameToComponents(name, components_val):
        u'\n        \u521b\u5efa\u7ec4\u4ef6\u5bf9\u8c61\n\n        :param name: Str \u6216 Unicode \u8f93\u5165\u7684\u8282\u70b9\u540d\u79f0\n        :param components_val: Str \u6216 Unicode \u8f93\u5165\u7684\u7ec4\u4ef6\u540d\u79f0\n        :return:\n        :rtype:Components1Base|Components2Base|Components3Base\n        '
        find = components_val.find('[')
        if (find > 0):
            try:
                components_type = components_val[0:find]
                no_compile = components_val[find:]
                compile = Global.re_object.findall(no_compile)
                node = Global.nameToNode(name)
                if (compile[0] == '*'):
                    return getattr(node, components_type)
                split_s = tuple((tuple((int(t) for t in i.split(':'))) for i in compile))
                cur_o = getattr(node, components_type)
            except Exception:
                raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
            for i in split_s:
                if (len(i) > 1):
                    cur_o = cur_o[i[0]:i[1]]
                else:
                    cur_o = cur_o[i[0]]
            return cur_o
        else:
            raise cmcore.CPMelError(u'\u65e0\u6cd5\u521b\u5efa\u7ec4\u4ef6')

    @staticmethod
    def plugToAttr(plug=MPlug):
        u'\n        MPlug\u8f6c\u5316\u4e3aAttr\n\n        :param plug: MPlug\n        :return:\n        :rtype:AttrObject|ArrayAttrObject\n        '
        if plug.isNull():
            raise cmcore.CPMelError(u'\u65e0\u6cd5\u521b\u5efaCPMel\u5c5e\u6027')
        if plug.isArray():
            return ArrayAttrObject(plug)
        return AttrObject(plug)
    NoWrapHead = ('__', 'cp__')

    @staticmethod
    def objectMetadef(api_type=MFn.kBase):

        def metadef(name, bases, attrs):

            def _(k):
                for t in Global.NoWrapHead:
                    if (k.find(t) == 0):
                        return True
            for (k, v) in attrs.items():
                if (k == 'isNull'):
                    continue
                elif _(k):
                    continue
                elif callable(v):
                    try:
                        NullType = v.NullType
                    except AttributeError:
                        NullType = Global.NullErr
                    if (NullType == Global.NullErr):
                        attrs[k] = Global._NullErrFunc(v)
                    elif (NullType == Global.NullUp):
                        attrs[k] = Global._NullGetUpFunc(v)
                    else:
                        attrs[k] = Global._NullDoItFunc(v)
                else:
                    attrs[k] = v
            cls = type(name, bases, attrs)
            Global.DependencyNodeTypes[api_type] = cls
            Global.DgTypes.insert(0, api_type)
            return cls
        return metadef

    @staticmethod
    def componentsTypesMetadef(name, bases, attrs):
        cls = type(name, bases, attrs)
        Global.ComponentsTypes.append(cls.components_type_str)
        return cls
    (NullErr, NullUp, NullDo) = range(3)

    @staticmethod
    def NullErrFunc(fn):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u8282\u70b9\u5bf9\u8c61\u7c7b\u6240\u64cd\u4f5c\u7684\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u88c5\u9970\u5668\n        \u5982\u679c\u4e0d\u5b58\u5728\u5c31\u62a5\u9519\n\n        :param fn:\n        :return:\n        '
        fn.NullType = Global.NullErr
        return fn

    @staticmethod
    def NullGetUpFunc(fn):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u8282\u70b9\u5bf9\u8c61\u7c7b\u6240\u64cd\u4f5c\u7684\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u88c5\u9970\u5668\n        \u5982\u679c\u4e0d\u5b58\u5728\u5c31\u4f7f\u7528\u4e0a\u4e00\u4e2a\u6570\u636e\n\n        :param fn:\n        :return:\n        '
        fn.NullType = Global.NullUp
        return fn

    @staticmethod
    def NullDoItFunc(fn):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u8282\u70b9\u5bf9\u8c61\u7c7b\u6240\u64cd\u4f5c\u7684\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u88c5\u9970\u5668\n        \u5982\u679c\u4e0d\u5b58\u5728\u4ecd\u7136\u6267\u884c\n\n        :param fn:\n        :return:\n        '
        fn.NullType = Global.NullDo
        return fn

    @staticmethod
    def _NullErrFunc(fn):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u8282\u70b9\u5bf9\u8c61\u7c7b\u6240\u64cd\u4f5c\u7684\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u88c5\u9970\u5668\n        \u5982\u679c\u4e0d\u5b58\u5728\u5c31\u62a5\u9519\n\n        :param fn:\n        :return:\n        '

        def _(self, *args, **kwargs):
            if self.isNull():
                cmcore.CPMelError(u'\u8282\u70b9\u5bf9\u8c61\u81ea\u8eab\u5df2\u4e0d\u5b58\u5728\u65e0\u6cd5\u64cd\u4f5c')
            else:
                return fn(self, *args, **kwargs)
        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    @staticmethod
    def _NullGetUpFunc(fn):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u8282\u70b9\u5bf9\u8c61\u7c7b\u6240\u64cd\u4f5c\u7684\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u88c5\u9970\u5668\n        \u5982\u679c\u4e0d\u5b58\u5728\u5c31\u4f7f\u7528\u4e0a\u4e00\u4e2a\u6570\u636e\n\n        :param fn:\n        :return:\n        '

        def _(self, *args, **kwargs):
            if self.isNull():
                try:
                    return _.data
                except AttributeError:
                    return None
            else:
                _.data = fn(self, *args, **kwargs)
                return _.data
        _.data = None
        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    @staticmethod
    def _NullDoItFunc(fn):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u8282\u70b9\u5bf9\u8c61\u7c7b\u6240\u64cd\u4f5c\u7684\u5bf9\u8c61\u662f\u5426\u5b58\u5728\u7684\u88c5\u9970\u5668\n        \u5982\u679c\u4e0d\u5b58\u5728\u5c31\u4f7f\u7528\u4e0a\u4e00\u4e2a\u6570\u636e\n\n        :param fn:\n        :return:\n        '
        return fn

class CPObject(object, ):
    u'\n    \u6240\u6709CPObject\u7684\u57fa\u7c7b\n    '
    Globalfunction = Global
    Object_List = None

    def __add__(self, other):
        u'\n        this + oyher\n\n        :param other:\n        :return:\n        '
        if isinstance(other, basestring):
            return (u'%s%s' % (str(self), other))
        if isinstance(other, DgNode):
            return (u'%s%s' % (str(self), str(other)))

    def __radd__(self, other):
        u'\n        other + this\n\n        :param other:\n        :return:\n        '
        if isinstance(other, basestring):
            return (u'%s%s' % (other, str(self)))
        if isinstance(other, DgNode):
            return (u'%s%s' % (str(other), str(self)))

    def __repr__(self):
        return repr(self.__str__())

    def isNull(self):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u53ef\u4ee5\u4f7f\u7528\n        \u6240\u6709\u65b9\u6cd5\u9ed8\u8ba4\u90fd\u4f1a\u68c0\u67e5\u662f\u5426\u53ef\u4ee5\u8c03\u7528\uff08\u8fd9\u4e2a\u9664\u5916\uff09\n        :return:\n        :rtype:bool\n        '
        return True

    def compile(self):
        return unicode(self)

class DgNode(CPObject, ):
    u'\n    \u8282\u70b9\u5bf9\u8c61\u57fa\u7c7b\n    '
    __metaclass__ = Global.objectMetadef(MFn.kDependencyNode)

    def __init__(self, obj=MObject, uuid=MUuid, uuid_s=u''):
        if obj.isNull():
            return
        self.obj = obj
        self.uuid = uuid
        self.uuid_s = uuid_s
        self.objecthandle = MObjectHandle(obj)
        self.fn = self.cp__getFnClass()
        self.type = self.fn.typeName()

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n\n        :return: MFn\n        :rtype:MFnDependencyNode\n        '
        return MFnDependencyNode(self.obj)

    def isNull(self):
        u'\n        \u68c0\u67e5\u5bf9\u8c61\u662f\u5426\u53ef\u4ee5\u4f7f\u7528\n\n        :return:\n        :rtype:bool\n        '
        return (not self.uuid.valid())

    def __unicode__(self):
        u'\n        __unicode__\u8f93\u51fa\n\n        :return:\n        '
        return self.name()

    def __str__(self):
        u'\n        str\u8f93\u51fa\n\n        :return:\n        '
        return self.name()

    def __repr__(self):
        u'\n        repr\u8f93\u51fa\n\n        :return:\n        '
        return ('%s(%s)' % (self.type, repr(self.name())))

    def __eq__(self, other):
        u'\n        ==\u5224\u65ad\n\n        :param other:\n        :return:\n        '
        if isinstance(other, DgNode):
            return (self.uuid_s == other.uuid_s)
        return False

    def __ne__(self, other):
        u'\n        !=\u5224\u65ad\n\n        :param other:\n        :return:\n        '
        return (not self.__eq__(other))

    def __getitem__(self, item):
        u'\n        []\u8bbf\u95ee\u64cd\u4f5c\n\n        :param item:\n        :return:\n        :rtype:int|float|bool|tuple|list\n        '
        if isinstance(item, basestring):
            return self.attr(item).get()
        else:
            raise cmcore.CPMelError(u'\u4ec5\u652f\u6301\u5b57\u7b26\u4e32\u8bbf\u95ee')

    def __setitem__(self, key, value):
        if isinstance(key, basestring):
            return self.attr(key).set(value)
        else:
            raise cmcore.CPMelError(u'\u4ec5\u652f\u6301\u5b57\u7b26\u4e32\u8bbf\u95ee')

    def __getattribute__(self, item):
        u'\n        .\u8bbf\u95ee\u64cd\u4f5c\n\n        :param item:\n        :return:\n        '
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            return object.__getattribute__(self, 'attr')(item)

    @staticmethod
    def isCurrentNodeType(obj=MObject):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param obj: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        '
        return True

    def _attr(self, attr):
        find = attr.find('[')
        if (find < 0):
            try:
                plug = self.fn.findPlug(attr)
                attr_obj = self.Globalfunction.plugToAttr(plug)
            except RuntimeError:
                raise cmcore.CPMelError(u'\u5c5e\u6027\u4e0d\u5b58\u5728')
            return attr_obj
        else:
            find = attr.find('[')
            if (find < 0):
                raise cmcore.CPMelError(u'\u5c5e\u6027\u4e0d\u5b58\u5728')
            else:
                try:
                    arr_attr_obj = self.Globalfunction.plugToAttr(self.fn.findPlug(attr[:find]))
                    if (not isinstance(arr_attr_obj, ArrayAttrObject)):
                        raise cmcore.CPMelError(u'\u8981\u83b7\u5f97\u7684\u5c5e\u6027\u4e0d\u662f\u6570\u7ec4\u5c5e\u6027')
                    finde = attr.find(']')
                    if (finde < 0):
                        raise cmcore.CPMelError(u'\u5b57\u7b26\u4e32\u7ed3\u6784\u9519\u8bef attr \u6216 attr[?]')
                    index = int(attr[(find + 1):finde])
                    return arr_attr_obj[index]
                except RuntimeError:
                    raise cmcore.CPMelError(u'\u5c5e\u6027\u4e0d\u5b58\u5728')

    def attr(self, attr):
        u'\n        \u83b7\u5f97maya\u5c5e\u6027\u7684CPMel\u5bf9\u8c61\n\n        :param attr:\n        :return:\n        :rtype: AttrObject|ArrayAttrObject\n        '
        try:
            sel = MSelectionList()
            sel.add((u'%s.%s' % (str(self), attr)))
            plug = MPlug()
            sel.getPlug(0, plug)
            attr_obj = self.Globalfunction.plugToAttr(plug)
        except RuntimeError:
            attr_obj = self
            for i in attr.split('.'):
                if (attr_obj is self):
                    attr_obj = attr_obj._attr(i)
                else:
                    attr_obj.attr(i)
        setattr(self, attr, attr_obj)
        return attr_obj

    def functionSet(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u51fd\u6570\u96c6\n\n        :return:\n        '
        sel_l = MSelectionList()
        sel_l.add(self.uuid)
        self.obj = MObject()
        sel_l.getDependNode(0, self.obj)
        self.objecthandle = MObjectHandle(self.obj)
        self.cp__fn = self.cp__getFnClass()
        return self.cp__fn

    @Global.NullGetUpFunc
    def name(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u6700\u77ed\u540d\u79f0\n\n        :return: Unicode \u8282\u70b9\u6700\u77ed\u540d\u79f0\n        :rtype: unicode\n        '
        return self.fn.name()

    def rename(self, p_str):
        u'\n        \u91cd\u547d\u540d\n\n        :return: Unicode \u65b0\u540d\u79f0\n        '
        cmds.rename(str(self), p_str)

    def listAttr(self, *args, **kwargs):
        u'\n        \u83b7\u5f97\u6240\u6709\u5c5e\u6027\u5bf9\u8c61\n\n        :return:\n        :rtype: list\n        '
        attrs = cmds.listAttr(str(self), *args, **kwargs)
        if (attrs is None):
            return []
        else:
            return [self.attr(i) for i in attrs]

    def copy(self):
        u'\n\n        :return:\n        :rtype: DgNode:DagNode\n        '
        return self.Globalfunction.nameToNode(cmds.duplicate(str(self), rc=True)[0])

    def isFromReferencedFile(self):
        u'\n        \u6b64\u8282\u70b9\u662f\u5426\u6765\u81ea\u5f15\u7528\u7684\u6587\u4ef6\n\n        :return:\n        :rtype: bool\n        '
        return self.fn.isFromReferencedFile()

    def isDefaultNode(self):
        u'\n        \u5982\u679c\u8be5\u8282\u70b9\u662f\u9ed8\u8ba4\u8282\u70b9\u8fd4\u56detrue\n\n        :return:\n        :rtype:bool\n        '
        return self.fn.isDefaultNode()

    def getNamespace(self):
        u'\n        \u8fd4\u56de\u6b64\u8282\u70b9\u6240\u5728\u7684\u540d\u79f0\u7a7a\u95f4\u7684\u540d\u79f0\n\n        :return:\n        :rtype:unicode\n        '
        return self.fn.parentNamespace()

    def setLocked(self, bool):
        u'\n        \u8bbe\u7f6e\u8282\u70b9\u9501\u5b9a\u72b6\u6001\n\n        :param bool:\n        :return:\n        '

        def doIt():
            self.functionSet().setLocked(bool)

        def undoIt():
            self.functionSet().setLocked((not bool))
        return cmcore.addCommand(doIt, undoIt)

    def getLocked(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u9501\u5b9a\u72b6\u6001\n\n        :return:\n        :rtype:bool\n        '
        return self.fn.isLocked()

class DagNode(DgNode, ):
    __metaclass__ = Global.objectMetadef(MFn.kDagNode)

    def __init__(self, obj=MObject, uuid=MUuid, uuid_s=u''):
        super(DagNode, self).__init__(obj, uuid, uuid_s)

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n\n        :return: MFn\n        :rtype:MFnDagNode\n        '
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnDagNode(path)

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param path: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        :rtype:bool\n        '
        return True

    @Global.NullGetUpFunc
    def nodeName(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u540d\u79f0\n\n        :return: Unicode \u8282\u70b9\u540d\u79f0\n        :rtype:unicode\n        '
        return self.fn.name()

    @Global.NullGetUpFunc
    def name(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u6700\u77ed\u540d\u79f0\n\n        :return: Unicode \u8282\u70b9\u6700\u77ed\u540d\u79f0\n        :rtype:unicode\n        '
        return self.fn.partialPathName()

    @Global.NullGetUpFunc
    def fullPathName(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u7edd\u5bf9\u8def\u5f84\n\n        :return: Unicode \u8282\u70b9\u7edd\u5bf9\u8def\u5f84\n        :rtype:unicode\n        '
        return self.fn.fullPathName()

    def childCount(self):
        u'\n        \u83b7\u5f97\u5b50\u5bf9\u8c61\u7684\u6570\u91cf\n\n        :return:\n        :rtype:int\n        '
        return self.fn.childCount()

    def addChild(self, obj):
        u'\n        \u6dfb\u52a0\u5b50\u5bf9\u8c61\n\n        :param obj:\n        :return:\n        '
        if isinstance(obj, DagNode):
            obj = str(obj)
        if isinstance(obj, basestring):
            cmds.parent(str(obj), str(self))
        else:
            raise cmcore.CPMelError(u'\u4e0d\u662fDag\u8282\u70b9')

    def getChilds(self):
        u'\n\n        :return:\n        :rtype:list\n        '
        return [self.Globalfunction.objToNode(self.fn.child(i)) for i in xrange(self.childCount())]

    def getParent(self):
        u'\n        \u83b7\u5f97\u7236\u5bf9\u8c61\n\n        :return:\n        :rtype: DagNode\n        '
        parents = self.fullPathName().split('|')
        if (len(parents) > 2):
            return self.Globalfunction.nameToNode('|'.join(parents[0:(-1)]))
        else:
            return

    def setParent(self, obj):
        u'\n        \u8bbe\u7f6e\u7236\u5bf9\u8c61\n\n        :param obj:\n        :return:\n        '
        if isinstance(obj, DagNode):
            obj = str(obj)
        if isinstance(obj, basestring):
            cmds.parent(str(self), str(obj))
        else:
            raise cmcore.CPMelError(u'\u4e0d\u662fDag\u8282\u70b9')
    parent = property(getParent, setParent)

    def getParents(self):
        u'\n        \u83b7\u5f97\u6240\u6709\u7236\u5bf9\u8c61\n\n        :return:\n        :rtype:list\n        '
        parents = self.fullPathName().split('|')
        return [self.Globalfunction.nameToNode('|'.join(parents[0:i])) for i in range(2, len(parents))]
    parents = property(getParents)

    def toRoot(self):
        u'\n        \u8f6c\u5230\u6839\u8def\u5f84\n\n        :return:\n        '
        cmds.parent(str(self), w=True)

    def setTranslate(self, point=basedata.Double3, is_word=True):
        u'\n        \u8bbe\u7f6e\u4f4d\u7f6e\n\n        :param point: \u4f4d\u7f6e\u53c2\u6570\n        :param is_word: \u662f\u5426\u5728\u4e16\u754c\u7a7a\u95f4\u4e0b\n        :return:\n        '
        cmds.xform(str(self), t=(point[0], point[1], point[2]), ws=is_word)
        return

    def getTranslate(self, is_word=True):
        u'\n        \u83b7\u5f97\u4f4d\u7f6e\n\n        :param is_word: \u662f\u5426\u5728\u4e16\u754c\u7a7a\u95f4\u4e0b\n        :return:\n        :rtype:Double3\n        '
        return basedata.Double3(cmds.xform(str(self), q=True, t=True, ws=is_word))

    def setRotate(self, vector=basedata.Double3, is_word=True):
        u'\n        \u8bbe\u7f6e\u65cb\u8f6c\n\n        :param vector: \u65cb\u8f6c\u503c\n        :param is_word: \u662f\u5426\u5728\u4e16\u754c\u7a7a\u95f4\u4e0b\n        :return:\n        '
        cmds.xform(str(self), ro=(vector[0], vector[1], vector[2]), ws=is_word)
        return

    def getRotate(self, is_word=True):
        u'\n        \u83b7\u5f97\u65cb\u8f6c\n\n        :param is_word: \u662f\u5426\u5728\u4e16\u754c\u7a7a\u95f4\u4e0b\n        :return:\n        :rtype:Double3\n        '
        return basedata.Double3(cmds.xform(str(self), q=True, ro=True, ws=is_word))

    def setScale(self, vector=basedata.Double3, is_word=True):
        u'\n        \u8bbe\u7f6e\u7f29\u653e\n\n        :param vector: \u7f29\u653e\u503c\n        :param is_word: \u662f\u5426\u5728\u4e16\u754c\u7a7a\u95f4\u4e0b\n        :return:\n        '
        cmds.xform(str(self), s=(vector[0], vector[1], vector[2]), ws=is_word)
        return

    def getScale(self, is_word=True):
        u'\n        \u83b7\u5f97\u7f29\u653e\n\n        :param is_word: \u662f\u5426\u5728\u4e16\u754c\u7a7a\u95f4\u4e0b\n        :return:\n        :rtype:Double3\n        '
        return basedata.Double3(cmds.xform(str(self), q=True, s=True, ws=is_word))

class AttrObject(CPObject, ):
    u'\n    \u5c5e\u6027\u5bf9\u8c61\n    '

    def __init__(self, plug=MPlug):
        self.cp__node = self.Globalfunction.objToNode(plug.node())
        self.plug = plug
        self.obj = plug.attribute()
        self.objecthandle = MObjectHandle(self.obj)
        try:
            self.type = cmds.getAttr(str(self), type=True)
        except RuntimeError as ex:

            def test_set(val, **kwargs):
                cmds.setAttr(str(self), val, **kwargs)

            def test_get(**kwargs):
                raise cmcore.CPMelError(u'\u4e0d\u53ef\u83b7\u5f97\u5c5e\u6027\u7684\u503c')
            self.type = u''
        else:

            def test_set(val, **kwargs):
                cmds.setAttr(str(self), val, **kwargs)

            def test_get(**kwargs):
                return cmds.getAttr(str(self), **kwargs)
            type_type = (u'Int32Array', u'doubleArray', u'string')
            size_array_type = (u'pointArray', u'vectorArray', u'stringArray', u'componentList')
            val3_type = (u'double3', u'float3', u'short3', u'long3', u'reflectanceRGB', u'spectrumRGB')
            if (self.type in val3_type):

                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), type=self.type, *val, **kwargs)

                def test_get(**kwargs):
                    return cmds.getAttr(str(self), **kwargs)[0]
            elif (self.type in type_type):

                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), val, type=self.type, **kwargs)
            elif (self.type in size_array_type):

                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), len(val), type=self.type, *val, **kwargs)
            elif (self.type == u'matrix'):

                def test_set(val, **kwargs):
                    cmds.setAttr(str(self), type=self.type, *[t for i in val for t in i], **kwargs)

                def test_get(**kwargs):
                    lis = cmds.getAttr(str(self), **kwargs)
                    return (lis[0:4], lis[4:8], lis[8:12], lis[12:16])
        self.__set = test_set
        self.__get = test_get

    def cp__attrPartialName(self):
        u'\n        \u83b7\u5f97\u5c5e\u6027\u540d\u79f0\n\n        :return:\n        :rtype:unicode\n        '
        return self.plug.partialName(False, True, True, False, False, True).replace('[-1]', '')

    @property
    def attrname(self):
        u'\n\n        :return:\n        :rtype:unicode\n        '
        return self.cp__attrPartialName()

    def cp__attrname(self):
        u'\n        \u83b7\u5f97CPMel\u5c5e\u6027\u5bf9\u8c61\u540d\u79f0\n\n        :return:\n        :rtype:unicode\n        '
        return (u'%s.%s' % (self.cp__node.name(), self.cp__attrPartialName()))

    def set(self, val, **kwargs):
        u'\n        \u8bbe\u7f6e\u503c\n\n        :param val:\n        :param kwargs:\n        :return:\n        '
        try:
            return self.__set(val, **kwargs)
        except RuntimeError as ex:
            raise cmcore.CPMelError(*ex.args)

    def get(self, **kwargs):
        u'\n        \u83b7\u5f97\u503c\n\n        :param kwargs:\n        :return:\n        :rtype: int|float|tuple|Double3|list\n        '
        try:
            return self.__get(**kwargs)
        except RuntimeError as ex:
            raise cmcore.CPMelError(*ex.args)
    v = property(get, set)

    def __str__(self):
        return self.cp__attrname()

    def __repr__(self):
        return ('%s(%s)' % (self.__class__.__name__, repr(self.cp__attrname())))

    def __eq__(self, other):
        u'\n        ==\u5224\u65ad\n\n        :param other:\n        :return:\n        '
        if isinstance(other, AttrObject):
            return (self.cp__attrname() == other.cp__attrname())
        return False

    def __ne__(self, other):
        u'\n        !=\u5224\u65ad\n\n        :param other:\n        :return:\n        '
        return (not self.__eq__(other))

    def __gt__(self, other):
        u'\n        this>xxx \u64cd\u4f5c\n\n        :param other:\n        :return:\n        '
        other.set(self.get())
        return

    def __lshift__(self, other):
        u'\n        this << xxx\n\n        :param other:\n        :return:\n        '
        return other.connect(self)

    def __rshift__(self, other):
        u'\n        this >> xxx\n\n        :param other:\n        :return:\n        '
        return self.connect(other)

    def attr(self, attr):
        u'\n\n        :param attr:\n        :return:\n        :rtype: AttrObject|ArrayAttrObject\n        :raise: CPMelError\n        '
        if (attr in self.__dict__):
            return self.__dict__[attr]
        find = attr.find('[')
        if (find < 0):
            for i in xrange(self.plug.numChildren()):
                test_plug = self.plug.child(i)
                test_attr_name = test_plug.partialName().split('.')[(-1)]
                if (attr == test_attr_name):
                    attr_obj = self.Globalfunction.plugToAttr(test_plug)
                    self.__dict__[attr] = attr_obj
                    return attr_obj
                test_attr_name = test_plug.partialName(False, False, False, False, False, True).split('.')[(-1)]
                if (attr == test_attr_name):
                    attr_obj = self.Globalfunction.plugToAttr(test_plug)
                    self.__dict__[attr] = attr_obj
                    return attr_obj
            raise cmcore.CPMelError(u'\u5c5e\u6027\u4e0d\u5b58\u5728')
        else:
            try:
                arr_attr_obj = self.attr(attr[:find])
                if (not isinstance(arr_attr_obj, ArrayAttrObject)):
                    raise cmcore.CPMelError(u'\u8981\u83b7\u5f97\u7684\u5c5e\u6027\u4e0d\u662f\u6570\u7ec4\u5c5e\u6027')
                finde = attr.find(']')
                if (finde < 0):
                    raise cmcore.CPMelError(u'\u5b57\u7b26\u4e32\u7ed3\u6784\u9519\u8bef attr \u6216 attr[?]')
                index = int(attr[(find + 1):finde])
                return arr_attr_obj[index]
            except RuntimeError:
                raise cmcore.CPMelError(u'\u5c5e\u6027\u4e0d\u5b58\u5728')

    def __getattribute__(self, item):
        u'\n        .\u8bbf\u95ee\u64cd\u4f5c\n\n        :param item:\n        :return:\n        '
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            if isinstance(item, basestring):
                return object.__getattribute__(self, 'attr')(item)
            else:
                raise cmcore.CPMelError(u'\u5bf9\u8c61\u6ca1\u6709\u5c5e\u6027')

    def node(self):
        u'\n        \u83b7\u5f97\u8282\u70b9\u5bf9\u8c61\n\n        :return:\n        :rtype:DgNode|DagNode\n        '
        return self.cp__node

    def connect(self, attr):
        u'\n        \u8fde\u63a5\n\n        :param attr:\n        :return:\n        '
        cmds.connectAttr(self.cp__attrname(), attr.cp__attrname(), f=True)

    def disConnect(self, attr):
        u'\n        \u65ad\u5f00\u8fde\u63a5\n\n        :param attr:\n        :return:\n        '
        cmds.disconnectAttr(self.cp__attrname(), attr.cp__attrname())

    def isConnect(self):
        u'\n        \u63d2\u70b9\u662f\u5426\u8fde\u63a5\n\n        :return:\n        :rtype:bool\n        '
        return self.plug.isConnected()
    if (MAYAINDEX > 2016):

        def getInConnect(self):
            u'\n            \u83b7\u5f97\u8f93\u5165\u8fde\u63a52016+\u7248\u672c\n\n            :return:\n            :rtype:AttrObject|ArrayAttrObject\n            '
            plug = self.plug.source()
            if plug.isNull():
                return None
            return self.Globalfunction.plugToAttr(plug)

        def getOutConnects(self):
            u'\n            \u83b7\u5f97\u8f93\u51fa\u8fde\u63a52016+\u7248\u672c\n\n            :return:\n            :rtype:tuple\n            '
            plugs = MPlugArray()
            self.plug.destinations(plugs)
            return tuple((self.Globalfunction.plugToAttr(i) for i in plugs if (not i.isNull())))
    else:

        def getInConnect(self):
            u'\n            \u83b7\u5f97\u8f93\u5165\u8fde\u63a52017-\u7248\u672c\n\n            :return:\n            :rtype:AttrObject|ArrayAttrObject\n            '
            o = cmds.listConnections(str(self), s=True, d=False, scn=True, p=True)
            if (o is None):
                return None
            return self.Globalfunction.nameToAttr(o[0])

        def getOutConnects(self):
            u'\n            \u83b7\u5f97\u8f93\u51fa\u8fde\u63a52017-\u7248\u672c\n\n            :return:\n            :rtype:tuple\n            '
            o = cmds.listConnections(str(self), s=False, d=True, scn=True, p=True)
            if (o is None):
                return tuple()
            return tuple((self.Globalfunction.nameToAttr(i) for i in o))

class ArrayAttrObject(AttrObject, ):

    def itemids(self):
        ids = MIntArray()
        self.plug.getExistingArrayAttributeIndices(ids)
        return ids

    def items(self):
        u'\n\n        :return:\n        :rtype:list\n        '
        return [self.cp__node.attr(('%s[%d]' % (self.cp__attrPartialName(), i))) for i in self.itemids()]

    def __getitem__(self, item):
        plug = self.plug.elementByLogicalIndex(item)
        return self.Globalfunction.plugToAttr(plug)

    def __iter__(self):
        return (self[i] for i in self.itemids())

class UIObject(BaseData, ):
    u'\n    UI\u5bf9\u8c61\u57fa\u7c7b\n    '

    def __init__(self, ui):
        self.ui = ui

    def getWeidget(self):
        u'\n        :return:\n        '
        return wrapInstance(long(OpenMayaUI.MQtUtil.findWindow(self.ui)), QWidget)

    def getControlWeidget(self):
        u'\n        :return:\n        '
        return wrapInstance(long(OpenMayaUI.MQtUtil.findControl(self.ui)), QWidget)

    def getLayoutWeidget(self):
        u'\n        :return:\n        '
        return wrapInstance(long(OpenMayaUI.MQtUtil.findLayout(self.ui)), QWidget)

    def getItemWeidget(self):
        u'\n        :return:\n        '
        return wrapInstance(long(OpenMayaUI.MQtUtil.findMenuItem(self.ui)), QWidget)

    def compile(self):
        u'\n        \u7f16\u8bd1\u4e3amel\u5bf9\u8c61\n\n        :return:\n        '
        return self.ui

    def __str__(self):
        return str(self.ui)

    def __unicode__(self):
        return self.ui

    def __repr__(self):
        return repr(self.ui)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def newObject(name=str):
    u'\n    \u6839\u636e\u4e0d\u540c\u7684\u8f93\u5165\u8fd4\u56de\u4e0d\u540c\u7684CPMel\u5bf9\u8c61\n    :param name:\n    :return: DgNode\u6216AttrObject\u672c\u8eab\u6216\u5176\u5b50\u7c7b\n    :rtype:CPObject|DgNode|DagNode|AttrObject|ArrayAttrObject|Components1Base|Components2Base|Components3Base\n    '
    if isinstance(name, DgNode):
        return name
    if (not isinstance(name, basestring)):
        name = str(name)
    find = name.find('.')
    if (find > 0):
        node_name = name[0:find]
        attr_or_comp = name[(find + 1):]
        comp_find = attr_or_comp.find('[')
        if (comp_find < 0):
            comp_find = len(attr_or_comp)
        if (attr_or_comp[0:comp_find] in Global.ComponentsTypes):
            return Global.nameToComponents(node_name, attr_or_comp)
        else:
            return Global.nameToAttr(name)
    return Global.nameToNode(name)
ObjectMetadef = Global.objectMetadef
componentsTypesMetadef = Global.componentsTypesMetadef

class Components1Base(CPObject, ):
    components_type_str = ''
    index = None

    def __init__(self, node=DgNode):
        self.node = node

    def cp__init_componenrs(self):
        pass

    @staticmethod
    def IsSingleComponent(fn):

        def _(self, *args, **kwargs):
            if (type(self.index) == int):
                return fn(self, *args, **kwargs)
            else:
                raise cmcore.CPMelError((fn.__name__ + u' \u65b9\u6cd5\u53ea\u80fd\u5728\u5355\u7ec4\u4ef6\u6a21\u5f0f\u4e0b\u8fd0\u884c'))
        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    def __str__(self):
        if (self.index is None):
            return ('%s.%s[*]' % (self.node.compile(), self.components_type_str))
        elif (type(self.index) == int):
            return ('%s.%s[%d]' % (self.node.compile(), self.components_type_str, self.index))
        else:
            return ('%s.%s[%d:%d]' % (self.node.compile(), self.components_type_str, self.index[0], self.index[1]))

    def cp__newIndexObject(self, index):
        u'\n\n        :param index:\n        :return:\n        :rtype:Components1Base\n        '
        obj = self.__class__(self.node)
        obj.index = index
        obj.cp__init_componenrs()
        return obj

    def __getitem__(self, item):
        u'\n\n        :param item:\n        :return:\n        :rtype:Components1Base\n        '
        obj = self.__class__(self.node)
        if (self.index is None):
            if (type(item) == int):
                obj.index = item
            else:
                obj.index = (item.start, item.stop)
        else:
            raise cmcore.CPMelError(u'\u6ca1\u6709\u66f4\u6df1\u7d22\u5f15\u7684\u7ec4\u4ef6')
        obj.cp__init_componenrs()
        return obj

    def __len__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnSingleIndexedComponent(obj)
        indexs = MIntArray()
        self.indexed_component.getElements(indexs)
        return indexs.length()

    def __iter__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnSingleIndexedComponent(obj)
        indexs = MIntArray()
        self.indexed_component.getElements(indexs)
        return (self.cp__newIndexObject(i) for i in indexs)

class Components2Base(CPObject, ):
    components_type_str = ''
    indexu = None
    indexv = None

    def __init__(self, node=DgNode):
        self.node = node

    def cp__init_componenrs(self):
        pass

    @staticmethod
    def IsSingleComponent(fn):

        def _(self, *args, **kwargs):
            if ((type(self.indexu) == int) and (type(self.indexv) == int)):
                return fn(self, *args, **kwargs)
            else:
                raise cmcore.CPMelError((fn.__name__ + u' \u65b9\u6cd5\u53ea\u80fd\u5728\u5355\u7ec4\u4ef6\u6a21\u5f0f\u4e0b\u8fd0\u884c'))
        _.__name__ = fn.__name__
        _.__doc__ = fn.__doc__
        _.__module__ = fn.__module__
        return _

    def __str__(self):
        if (self.indexu is None):
            return ('%s.%s[*][*]' % (self.node.compile(), self.components_type_str))
        elif (self.indexv is None):
            if (type(self.indexu) == int):
                return ('%s.%s[%d][*]' % (self.node.compile(), self.components_type_str, self.indexu))
            else:
                return ('%s.%s[%d:%d][*]' % (self.node.compile(), self.components_type_str, self.indexu[0], self.indexu[1]))
        elif (type(self.indexu) == int):
            if (type(self.indexv) == int):
                return ('%s.%s[%d][%d]' % (self.node.compile(), self.components_type_str, self.indexu, self.indexv))
            else:
                return ('%s.%s[%d][%d:%d]' % (self.node.compile(), self.components_type_str, self.indexu, self.indexv[0], self.indexv[1]))
        elif (type(self.indexv) == int):
            return ('%s.%s[%d:%d][%d]' % (self.node.compile(), self.components_type_str, self.indexu[0], self.indexu[1], self.indexv))
        else:
            return ('%s.%s[%d:%d][%d:%d]' % (self.node.compile(), self.components_type_str, self.indexu[0], self.indexu[1], self.indexv[0], self.indexv[1]))

    def cp__newIndexObject(self, indexu, indexv):
        u'\n\n        :param indexu:\n        :param indexv:\n        :return:\n        :rtype:Components2Base\n        '
        obj = self.__class__(self.node)
        obj.indexu = indexu
        obj.indexv = indexv
        obj.cp__init_componenrs()
        return obj

    def __getitem__(self, item):
        u'\n\n        :param item:\n        :return:\n        :rtype:Components2Base\n        '
        obj = self.__class__(self.node)
        if (self.indexu is None):
            if (type(item) == int):
                obj.indexu = item
            else:
                obj.indexu = (item.start, item.stop)
        elif (self.indexv is None):
            if (type(item) == int):
                obj.indexv = item
            else:
                obj.indexv = (item.start, item.stop)
        else:
            raise cmcore.CPMelError(u'\u6ca1\u6709\u66f4\u6df1\u7d22\u5f15\u7684\u7ec4\u4ef6')
        obj.cp__init_componenrs()
        return obj

    def __len__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnDoubleIndexedComponent(obj)
        indexus = MIntArray()
        indexvs = MIntArray()
        self.indexed_component.getElements(indexus, indexvs)
        return indexus.length()

    def __iter__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnDoubleIndexedComponent(obj)
        indexus = MIntArray()
        indexvs = MIntArray()
        self.indexed_component.getElements(indexus, indexvs)
        return (self.cp__newIndexObject(indexus[i], indexvs[i]) for i in xrange(indexus.length()))

class Components3Base(CPObject, ):
    components_type_str = ''
    indexs = None
    indext = None
    indexu = None

    def __init__(self, node=DgNode):
        self.node = node

    def cp__init_componenrs(self):
        pass

    def __str__(self):
        if (self.indexs is None):
            return ('%s.%s[*][*][*]' % (self.node.compile(), self.components_type_str))
        elif (self.indext is None):
            if (type(self.indext) == int):
                return ('%s.%s[%d][*][*]' % (self.node.compile(), self.components_type_str, self.indexs))
            else:
                return ('%s.%s[%d:%d][*][*]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1]))
        elif (self.indexu is None):
            if (type(self.indexs) == int):
                if (type(self.indext) == int):
                    return ('%s.%s[%d][%d][*]' % (self.node.compile(), self.components_type_str, self.indexs, self.indext))
                else:
                    return ('%s.%s[%d][%d:%d][*]' % (self.node.compile(), self.components_type_str, self.indexs, self.indext[0], self.indext[1]))
            elif (type(self.indext) == int):
                return ('%s.%s[%d:%d][%d][*]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext))
            else:
                return ('%s.%s[%d:%d][%d:%d][*]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext[0], self.indext[1]))
        elif (type(self.indexs) == int):
            if (type(self.indext) == int):
                if (type(self.indexu) == int):
                    return ('%s.%s[%d][%d][%d]' % (self.node.compile(), self.components_type_str, self.indexs, self.indext, self.indexu))
                else:
                    return ('%s.%s[%d][%d][%d:%d]' % (self.node.compile(), self.components_type_str, self.indexs, self.indext, self.indexu[0], self.indexu[1]))
            elif (type(self.indexu) == int):
                return ('%s.%s[%d][%d:%d][%d]' % (self.node.compile(), self.components_type_str, self.indexs, self.indext[0], self.indext[1], self.indexu))
            else:
                return ('%s.%s[%d][%d:%d][%d:%d]' % (self.node.compile(), self.components_type_str, self.indexs, self.indext[0], self.indext[1], self.indexu[0], self.indexu[1]))
        elif (type(self.indext) == int):
            if (type(self.indexu) == int):
                return ('%s.%s[%d:%d][%d][%d]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext, self.indexu))
            else:
                return ('%s.%s[%d:%d][%d][%d:%d]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext, self.indexu[0], self.indexu[1]))
        elif (type(self.indexu) == int):
            return ('%s.%s[%d:%d][%d:%d][%d]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext[0], self.indext[1], self.indexu))
        else:
            return ('%s.%s[%d:%d][%d:%d][%d:%d]' % (self.node.compile(), self.components_type_str, self.indexs[0], self.indexs[1], self.indext[0], self.indext[1], self.indexu[0], self.indexu[1]))

    def cp__newIndexObject(self, indexs, indext, indexu):
        u'\n\n        :param indexs:\n        :param indext:\n        :param indexu:\n        :return:\n        :rtype:Components3Base\n        '
        obj = self.__class__(self.node)
        obj.indexs = indexs
        obj.indext = indext
        obj.indexu = indexu
        obj.cp__init_componenrs()
        return obj

    def __getitem__(self, item):
        u'\n\n        :param item:\n        :return:\n        :rtype:Components3Base\n        '
        obj = self.__class__(self.node)
        if (self.indexs is None):
            if (type(item) == int):
                obj.indexs = item
            else:
                obj.indexs = (item.start, item.stop)
        elif (self.indext is None):
            if (type(item) == int):
                obj.indext = item
            else:
                obj.indext = (item.start, item.stop)
        elif (self.indexu is None):
            if (type(item) == int):
                obj.indexu = item
            else:
                obj.indexu = (item.start, item.stop)
        else:
            raise cmcore.CPMelError(u'\u6ca1\u6709\u66f4\u6df1\u7d22\u5f15\u7684\u7ec4\u4ef6')
        obj.cp__init_componenrs()
        return obj

    def __len__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnTripleIndexedComponent(obj)
        indexss = MIntArray()
        indexts = MIntArray()
        indexus = MIntArray()
        self.indexed_component.getElements(indexss, indexts, indexus)
        return indexus.length()

    def __iter__(self):
        obj = self.Globalfunction.nameToComponentsMObject(self.compile())
        self.indexed_component = MFnTripleIndexedComponent(obj)
        indexss = MIntArray()
        indexts = MIntArray()
        indexus = MIntArray()
        self.indexed_component.getElements(indexss, indexts, indexus)
        return (self.cp__newIndexObject(indexss[i], indexts[i], indexus[i]) for i in xrange(indexss.length()))
