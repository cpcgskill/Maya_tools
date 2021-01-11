#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/7 22:44
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
import re
import shutil
import glob
import codecs
import uuid
import hashlib
import ast
import astunparse

import utils
from utils import *


def formattedPath(path):
    path = decode(path)
    path = path.replace(u"\\", u"/")
    if path[-1] == u"/":
        path = path[:-1]
    return path.replace(u"\\", u"/")


def uid():
    return uuid.uuid4().hex


def hashString(string):
    u"""

    :param string:
    :type string: str
    :return:
    """
    md5 = hashlib.md5()
    md5.update(bytes(decode(string).encode("utf-8")))
    return md5.hexdigest()


class Node(object):
    type = ""
    data = dict()

    def __init__(self, type, parent=None):
        u"""

        :param type:
        :type type: unicode
        :param data:
        :type data: dict
        """
        self.type = type
        self.data = dict()
        if not parent is None:
            if isinstance(parent, Node):
                for k, v in parent.data.items():
                    self.data[k] = v


class DC(dict):
    def __setitem__(self, k, v):
        print "!!! DC >> ", k, ": ", v
        if k == "CPMel.core.Command":
            pass
        super(DC, self).__setitem__(k, v)


class BuildPython(object):
    def __init__(self, main_module=u"main", src=r"D:\Development\tools\test\build\mid"):
        self.main_module = main_module
        self.src = formattedPath(src)
        self.current_src = self.src
        self.current_file = None
        self.n_id = uid()
        self.files = list()
        for root, dirs, files in os.walk(self.src):
            for file in files:
                self.files.append(formattedPath(u"%s/%s" % (root, file)))

        self.Root = Node("root")
        self.modules = DC()

        self.Import(self.main_module)

        #
        print self.modules
        values = list(set([v.path for v in self.modules.values()]))

        def sort(i):
            names = i.split(u"/")
            size = len(names)
            if names[-1] == u"__init__.py":
                size -= 1
            return size * -1

        values.sort(key=sort)
        for v in values:
            print v
            names = v.split(u"/")
            if names[-1] == "__init__.py":
                names.pop(-1)
                original_name = u"/".join(names)
                names[-1] = self.hashName(names[-1])
                abspath = u"/".join(names)
                # 不知道为啥 pycharm 使用debug模式运行到这会报错
                os.rename(original_name, abspath)
            else:
                sp_filename = names[-1].split(u".")
                sp_filename[0] = self.hashName(sp_filename[0])
                names[-1] = u".".join(sp_filename)
                abspath = u"/".join(names)
                os.rename(v, abspath)

    def hashName(self, s):
        v = u"_DEBUG_" + s
        return v

    def isfile(self, file):
        file = formattedPath(file)
        return file in self.files

    def searchModuleFile(self, root, module):
        u"""

        :param root:
        :param module:
        :return:
        :rtype: unicode|None
        """
        if module is None:
            if self.isfile(u"%s/__init__.py" % root):
                return u"%s/__init__.py" % root
            return None
        module_file = module.replace(u".", u"/")
        if self.isfile(u"%s/%s/__init__.py" % (root, module_file)):
            return u"%s/%s/__init__.py" % (root, module_file)
        if self.isfile(u"%s/%s.py" % (root, module_file)):
            return u"%s/%s.py" % (root, module_file)
        if self.isfile(u"%s/%s.pyd" % (root, module_file)):
            return u"%s/%s.pyd" % (root, module_file)
        if self.isfile(u"%s/%s.pyw" % (root, module_file)):
            return u"%s/%s.pyw" % (root, module_file)
        if self.isfile(u"%s/%s.pyo" % (root, module_file)):
            return u"%s/%s.pyo" % (root, module_file)
        if self.isfile(u"%s/%s.pyc" % (root, module_file)):
            return u"%s/%s.pyc" % (root, module_file)
        if self.isfile(u"%s/%s.pyz" % (root, module_file)):
            return u"%s/%s.pyz" % (root, module_file)
        return None

    def fileModuleName(self, root, module_file):
        names = module_file[len(root) + 1:].split(u"/")
        if names[-1] == u"__init__.py":
            names.pop(-1)
        names[-1] = names[-1].split(u".")[0]
        return u".".join(names)

    def absModuleName(self, module, root, current_src, level=0):
        if level <= 0:
            module_file = self.searchModuleFile(current_src, module)
            if not module_file is None:
                return self.fileModuleName(root, module_file)
            module_file = self.searchModuleFile(root, module)
            if not module_file is None:
                return self.fileModuleName(root, module_file)
        else:
            current_dir_path_sps = current_src.split(u"/")
            for i in range(level - 1):
                current_dir_path_sps.pop(-1)
            path = u"/".join(current_dir_path_sps)
            module_file = self.searchModuleFile(path, module)
            if not module_file is None:
                return self.fileModuleName(root, module_file)
        return None

    def gotoFile(self, path):
        self.current_file = formattedPath(path)
        self.current_src = u"/".join(self.current_file.split(u"/")[:-1])

    def build_Import(self, node, gl_space, loc_space):
        for t in node.names:
            # 如果之前操作模块对象就删除
            if t.asname is None:
                n = t.name.split(".")[0]
                if n in loc_space.data:
                    loc_space.data.pop(n)
            else:
                if t.asname in loc_space.data:
                    loc_space.data.pop(t.asname)
            # 导入模块对象
            modules = self.Import(t.name)
            if not modules is None:
                # self.Import(t.name)
                if t.asname is None:
                    n = t.name.split(".")[0]
                    loc_space.data[n] = modules[0]
                t.name = u".".join(
                    [self.hashName(name) if ID < len(modules) else name
                     for ID, name in enumerate(t.name.split(u"."))]
                )

    def build_ImportFrom(self, node, gl_space, loc_space):
        module_name = self.absModuleName(node.module, self.src, self.current_src, node.level)
        if module_name is None:
            return
        modules = self.Import(module_name)
        if modules is None:
            return
        if not node.module is None:
            abs_module_name_sp = module_name.split(u".")
            noabs_module_name_sp = node.module.split(u".")
            abs_head_size = len(abs_module_name_sp) - len(noabs_module_name_sp)
            if not abs_head_size >= len(modules):
                rename_size = len(modules[abs_head_size:])
                node.module = u".".join(
                    [self.hashName(i) if ID < rename_size else i for ID, i in
                     enumerate(node.module.split(u"."))]
                )
        module = modules[-1]
        for i in node.names:
            if self.current_file == "D:/Development/tools/test/build/mid/main.py" and i.name == "plugins":
                print "! E"
            if i.asname is None:
                if i.name in gl_space.data:
                    gl_space.data.pop(i.name)
            else:
                if i.asname in gl_space.data:
                    gl_space.data.pop(i.asname)
            if i.name == u"*":
                for k, v in module.data.items():
                    gl_space.data[k] = v
                return
            if i.name in module.data:
                if i.asname is None:
                    gl_space.data[i.name] = module.data[i.name]
                i.name = self.hashName(i.name)
            else:
                from_module_name = u"%s.%s" % (module_name, i.name)
                from_modules = self.Import(from_module_name)
                if not modules is None:
                    if len(from_modules) == len(from_module_name.split(u".")):
                        module.data[i.name] = from_modules[-1]
                        if i.asname is None:
                            gl_space.data[i.name] = from_modules[-1]
                        i.name = self.hashName(i.name)

    def build_Assign(self, node, gl_space, loc_space):
        self.buildNode(node.value, gl_space, loc_space)

    def build_Call(self, node, gl_space, loc_space):
        n = Node("object")
        if node.func in loc_space.data:
            obj = loc_space.data[node.func]
            n.data = obj.data
        elif node.func in gl_space.data:
            obj = gl_space.data[node.func]
            n.data = obj.data
        self.buildNode(node.func, gl_space, loc_space)
        return n

    def build_Return(self, node, gl_space, loc_space):
        self.buildNode(node.value, gl_space, loc_space)

    def build_Tuple(self, node, gl_space, loc_space):
        for i in node.elts:
            self.buildNode(i, gl_space, loc_space)

    def build_List(self, node, gl_space, loc_space):
        for i in node.elts:
            self.buildNode(i, gl_space, loc_space)

    def build_Set(self, node, gl_space, loc_space):
        for i in node.elts:
            self.buildNode(i, gl_space, loc_space)

    def build_Dict(self, node, gl_space, loc_space):
        for k, v in zip(node.keys, node.values):
            self.buildNode(k, gl_space, loc_space)
            self.buildNode(v, gl_space, loc_space)

    def build_Name(self, node, gl_space, loc_space):
        if node.id in loc_space.data:
            v = loc_space.data.get(node.id)
            node.id = self.hashName(node.id)
            return v
        if node.id in gl_space.data:
            v = gl_space.data.get(node.id)
            node.id = self.hashName(node.id)
            return v

    def build_Attribute(self, node, gl_space, loc_space):
        attrs = list()
        n = node
        while True:
            attrs.insert(0, n)
            if not isinstance(n, ast.Attribute):
                break
            n = n.value
        _g_space = gl_space
        space = loc_space
        for attr in attrs:
            if isinstance(attr, ast.Name):
                v = self.buildNode(attr, gl_space, space)
                if v is None:
                    return
                space = v
            elif isinstance(attr, ast.Attribute):
                if attr.attr in space.data:
                    space = space.data[attr.attr]
                    attr.attr = self.hashName(attr.attr)
                else:
                    return
            else:
                return
        return

    def build_Class(self, node, gl_space, loc_space):
        node_name = node.name
        next_space = Node("class")

        for i in node.bases:
            self.buildNode(i, gl_space, loc_space)

        # 编译类的body部分
        for i in node.body:
            print "class >>", i
            self.buildNode(i, gl_space, next_space)

    def build_Function(self, node, gl_space, loc_space):
        # next_space = Node("function")

        # loc_space.data[node.name] = next_space

        temporary_space = Node("temporary")

        # node.name = self.hashName(node.name)
        for i in node.args.args:
            self.buildNode(i, gl_space, temporary_space)
        for i in node.body:
            print "fucn >>", i
            self.buildNode(i, gl_space, temporary_space)

    def build_If(self, node, gl_space, loc_space):
        for i in node.body:
            print "if >>", i
            self.buildNode(i, gl_space, loc_space)

    def buildNode(self, node, gl_space, loc_space):
        # line
        # import from
        if isinstance(node, ast.Import):
            return self.build_Import(node, gl_space, loc_space)
        if isinstance(node, ast.ImportFrom):
            return self.build_ImportFrom(node, gl_space, loc_space)
        if isinstance(node, ast.Attribute):
            return self.build_Attribute(node, gl_space, loc_space)
        if isinstance(node, ast.Name):
            return self.build_Name(node, gl_space, loc_space)
        return

    def buildPy(self, module_node):
        code = readFile(self.current_file)
        nodes = ast.parse(code)
        for i in ast.walk(nodes):
            self.buildNode(i, module_node, module_node)
        # if isinstance(i, ast.Name):
        #     i.id = self.hashName(i.id)
        code = astunparse.unparse(nodes)
        writeFile(self.current_file, code)
        return module_node

    def buildAll(self, module_node):
        names = module_node.path.split(u"/")
        module_name = names[-1].split(u".")[0]
        _ = names[-1].split(u".")
        _[-1] = u"py"
        names[-1] = u".".join(_)
        py_filename = u"/".join(names)
        temporary = u"""\
#!/usr/bin/python
# -*-coding:utf-8 -*-
from .<<module_name>> import *
"""
        temporary = temporary.replace(u"<<module_name>>", module_name)

        with codecs.open(py_filename, "w", encoding="utf-8") as f:
            f.write(temporary)
        module_node.path = py_filename
        return module_node

    def _Import(self, module_name):
        if module_name in self.modules:
            return self.modules.get(module_name)
        path = self.searchModuleFile(self.current_src, module_name)
        if path is None:
            path = self.searchModuleFile(self.src, module_name)
            if path is None:
                return
        path = formattedPath(path)
        print "!!!! _Import >> ", path
        current_file = self.current_file
        current_src = self.current_src
        self.current_file = path
        self.current_src = u"/".join(self.current_file.split(u"/")[:-1])

        file_type = path.split(u".")[-1]
        module_node = Node("module")
        module_node.path = path
        module_node.name = module_name
        self.modules[module_name] = module_node
        if file_type == u"py":
            self.buildPy(module_node)
        else:
            self.buildAll(module_node)

        self.current_file = current_file
        self.current_src = current_src
        return module_node

    def Import(self, module_name):
        names = module_name.split(".")
        modules = list()
        for i in range(len(names)):
            name = ".".join(names[:i + 1])
            module = self._Import(name)
            if module is None:
                break
            modules.append(module)
        if len(modules) <= 0:
            return None
        for i in range(1, len(modules)):
            up_module = modules[i - 1]
            up_module.data[names[i]] = modules[i]
        return modules

    def FormImport(self, module_name, gl_space, level=0, format=list()):
        module_name = self.absModuleName(module_name, self.src, self.current_src, level)
        module = self.Import(module_name)
        if module is None:
            return
        pass


#
# def Import(self, module_name):
#     v = searchModuleFile(self._current_src, module_name)
#     if v is None:
#         v = searchModuleFile(self._src, module_name)
#         if v is None:
#             return
#     current_file = self._current_file
#     self.gotoFile(v)
#     code = readFile(self._current_file)
#     nodes = ast.parse(code)
#     for i in ast.walk(nodes):
#         if isinstance(i, ast.Import):
#             pass
#     code = astunparse.unparse(nodes)
#     self.gotoFile(current_file)
#     writeFile(self._current_file, code)


BuildPython()
