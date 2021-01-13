
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/27 23:26\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n\u4e00\u4e2a\u63d0\u4f9b\u4e86Python\u5f00\u53d1\u4e2d\u7684\u4fbf\u5229\u529f\u80fd\u7684\u6a21\u5757\n'
import re
import sys
import json
import functools
import maya.api.OpenMaya as OpenMaya
import maya.cmds as cmds
from .. import core as cmcore

def undoBlock(fn):
    u'\n    \u64a4\u9500\u5757\u88c5\u9970\u5668\u5c06\u6240\u6709maya\u547d\u4ee4\u7684\u64a4\u9500\u6253\u5305\u5230\u4e00\u4e2a\u5757\u91cc\n\n    :param fn:\n    :return:\n    '

    def _(*args, **kwargs):
        cmds.undoInfo(ock=True)
        try:
            return fn(*args, **kwargs)
        except:
            OpenMaya.MGlobal.displayError(cmcore.error.formatGuiException(*sys.exc_info()))
        finally:
            cmds.undoInfo(cck=True)
    _.__name__ = fn.__name__
    _.__doc__ = fn.__doc__
    _.__module__ = fn.__module__
    return _
funcs = list()

def scriptStringFunc(fn, *args, **kwargs):
    u'\n    \u53ef\u4ee5\u5c06Python\u51fd\u6570\u5305\u88c5\u4e3aMel\u811a\u672c\n    \u7528\u4e8eMaya\u6ca1\u6709\u63d0\u4f9b\u51fd\u6570\u8f93\u5165\u7684\u811a\u672c\u53c2\u6570\n\n    :param fn:\n    :param args:\n    :param kwargs:\n    :return:\n    '
    fn = functools.partial(fn, *args, **kwargs)
    funcs.append(fn)
    return u'python "__import__(\\"ctypes\\").cast({}, __import__(\\"ctypes\\").py_object).value()";'.format(id(fn))

def scriptStringString(s=u''):
    u'\n    \u53ef\u4ee5\u5c06Python \u56de\u8c03\u5b57\u7b26\u4e32\u5305\u88c5\u4e3aMel\u811a\u672c\n    \u7528\u4e8eMaya\u6ca1\u6709\u63d0\u4f9b\u51fd\u6570\u8f93\u5165\u7684\u811a\u672c\u53c2\u6570\n\n    :param fn:\n    :return:\n    :rtype:bool\n    '
    return (u'python "%s";' % s.replace('"', '\\"').replace('\n', '\\n'))

def decode(s=''):
    u'\n    \u5b57\u7b26\u4e32\u89e3\u7801\u51fd\u6570\n\n    :param s:\n    :return:\n    '
    if (not isinstance(s, basestring)):
        try:
            s = str(s)
        except:
            s = unicode(s)
    if (type(s) == str):
        try:
            return s.decode('UTF-8')
        except UnicodeDecodeError:
            try:
                return s.decode('GB18030')
            except UnicodeDecodeError:
                try:
                    return s.decode('Shift-JIS')
                except UnicodeDecodeError:
                    try:
                        return s.decode('EUC-KR')
                    except UnicodeDecodeError:
                        return unicode(s)
    return s.encode('UTF-8').decode('UTF-8')

class Dict(object, ):
    u'\n    \u4e00\u4e2a\u4e0eMayaObjectData\u4ea4\u4e92\u7684\u4e3adict\u7c7b\n\n    '

    def __init__(self, datacore, name, updatafuncs):
        self.datacore = datacore
        self.name = name
        self.updatafuncs = updatafuncs

    def this(self):
        return self.datacore.value[self.name]

    def __iter__(self):
        return self.datacore.value[self.name].__iter__()

    def __setitem__(self, key, value):
        self.datacore.value[self.name].__setitem__(key, value)
        self.updata()

    def __getitem__(self, item):
        self.datacore.read()
        return self.datacore.value[self.name].__getitem__(item)

    def __str__(self):
        return self.datacore.value[self.name].__str__()

    def __repr__(self):
        return self.datacore.value[self.name].__repr__()

    def __unicode__(self):
        return self.datacore.value[self.name].__unicode__()

    def updata(self):
        for i in self.updatafuncs:
            i(self.datacore.value[self.name])
        self.datacore.write()

    def clear(self, *args):
        return self.datacore.value[self.name].clear(*args)

    def copy(self, *args):
        return self.datacore.value[self.name].copy(*args)

    def fromkeys(self, *args):
        return self.datacore.value[self.name].fromkeys(*args)

    def get(self, *args):
        return self.datacore.value[self.name].get(*args)

    def has_key(self, *args):
        return self.datacore.value[self.name].has_key(*args)

    def items(self, *args):
        return self.datacore.value[self.name].items(*args)

    def iteritems(self, *args):
        return self.datacore.value[self.name].iteritems(*args)

    def iterkeys(self, *args):
        return self.datacore.value[self.name].iterkeys(*args)

    def itervalues(self, *args):
        return self.datacore.value[self.name].itervalues(*args)

    def keys(self, *args):
        return self.datacore.value[self.name].keys(*args)

    def pop(self, *args):
        return self.datacore.value[self.name].pop(*args)

    def popitem(self, *args):
        return self.datacore.value[self.name].popitem(*args)

    def setdefault(self, *args):
        return self.datacore.value[self.name].setdefault(*args)

    def update(self, *args):
        return self.datacore.value[self.name].update(*args)

    def values(self, *args):
        return self.datacore.value[self.name].values(*args)

    def viewitems(self, *args):
        return self.datacore.value[self.name].viewitems(*args)

    def viewkeys(self, *args):
        return self.datacore.value[self.name].viewkeys(*args)

    def viewvalues(self, *args):
        return self.datacore.value[self.name].viewvalues(*args)

class MayaObjectData(object, ):
    re_compile = re.compile('_')

    def __init__(self, obj=u'', name=u'default'):
        obj = str(obj)
        if (not cmds.objExists(obj)):
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        name_hash = hash(name)
        if (name_hash < 0):
            self.name = (u'CPMEL_MayaObjectData__%d' % (name_hash * (-1)))
        else:
            self.name = (u'CPMEL_MayaObjectData_%d' % name_hash)
        sel = OpenMaya.MSelectionList()
        sel.add(obj)
        obj = sel.getDependNode(0)
        fn = OpenMaya.MFnDependencyNode(obj)
        self.uuid = fn.uuid()
        if (not cmds.objExists(self.__name)):
            cmds.addAttr(self.__path, ln=self.name, dt='string')
            self.value = dict()
            self.write()
        else:
            self.read()

    @property
    def __path(self):
        sel = OpenMaya.MSelectionList()
        sel.add(self.uuid)
        if (sel.length() < 1):
            raise cmcore.CPMelError(u'\u8282\u70b9\u4e0d\u5b58\u5728')
        return sel.getSelectionStrings()[0]

    @property
    def __name(self):
        return (u'%s.%s' % (self.__path, self.name))

    def write(self):
        json_string = decode(json.dumps(self.value))
        cmds.setAttr((u'%s.%s' % (self.__path, self.name)), json_string, type='string')

    def read(self):
        try:
            json_string = cmds.getAttr((u'%s.%s' % (self.__path, self.name)))
        except RuntimeError:
            raise cmcore.CPMelError(u'\u65e0\u6cd5\u6b63\u786e\u8bfb\u53d6\u6570\u636e')
        try:
            self.value = json.loads(json_string)
        except ValueError:
            raise cmcore.CPMelError(u'\u65e0\u6cd5\u6b63\u786e\u89e3\u6790\u6570\u636e')

    def addValueBlock(self, name):
        name = (u'@VALUE->%s' % name)
        return MayaObjectData._VlaueBlock(self, name)

    def addDict(self, name, d_v, updata_funcs):
        name = (u'@DICT->%s' % name)
        if (name in self.value):
            o = self.value[name]
        else:
            o = dict()
            self.value[name] = o
        for i in d_v:
            if (not (i in o)):
                o[i] = d_v[i]
        self.write()
        return Dict(self, name, updata_funcs)

    def getDict(self, name):
        if (name in self.value):
            o = self.value[name]
        else:
            o = dict()
            self.value[name] = o
        return o

    class _VlaueBlock(object, ):

        def __init__(self, core_object, name=u''):
            self.core_object = core_object
            self.name = name
            if (not (self.name in self.core_object.value)):
                self.core_object.value[self.name] = None
                self.core_object.write()

        def setV(self, v):
            self.core_object.value[self.name] = v
            self.core_object.write()

        def getV(self):
            self.core_object.read()
            return self.core_object.value[self.name]
        v = property(getV, setV)

    class Block(object, ):

        def upDataFunc(self):
            pass

    def metaclass(self, name='default'):
        _block_name = name

        def _metaclass(name, bases, attrs):
            try:
                upDataFunc = attrs['upDataFunc']
                attrs.pop('upDataFunc')
            except KeyError:
                try:
                    upDataFunc = attrs[u'upDataFunc']
                    attrs.pop(u'upDataFunc')
                except KeyError:

                    def upDataFunc(self):
                        pass
            upDataFunc.is_do_new_updatafunc = False

            def newUpDataFunc(this):
                if (not upDataFunc.is_do_new_updatafunc):
                    upDataFunc.is_do_new_updatafunc = True
                    upDataFunc(this)
                    upDataFunc.is_do_new_updatafunc = False
            cls = type(name, bases, attrs)
            block_name = (u'@CLS->%s_%s_%s' % (cls.__module__, name, _block_name))
            if (not (block_name in self.value)):
                this_value_block = dict()
                self.value[block_name] = this_value_block
            else:
                this_value_block = self.value[block_name]
            for i in dir(cls):
                if (not self.re_compile.match(i)):
                    if (not (i in this_value_block)):
                        this_value_block[i] = getattr(cls, i)

                    def __get(k, this):
                        self.read()
                        return self.value[block_name][k]

                    def __set(k, this, v):
                        try:
                            if (v == self.value[block_name][k]):
                                return None
                        except KeyError:
                            pass
                        self.value[block_name][k] = v
                        self.write()
                        newUpDataFunc(this)
                    setattr(cls, i, property(functools.partial(__get, i), functools.partial(__set, i)))
            self.write()
            return cls()
        return _metaclass
