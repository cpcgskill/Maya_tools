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


def searchModuleFile(root, module):
    u"""

    :param root:
    :param module:
    :return:
    :rtype: unicode|None
    """
    module_file = module.replace(u".", u"/")
    if os.path.isfile(u"%s/%s/__init__.py" % (root, module_file)):
        return u"%s/%s/__init__.py" % (root, module_file)
    if os.path.isfile(u"%s/%s.py" % (root, module_file)):
        return u"%s/%s.py" % (root, module_file)
    if os.path.isfile(u"%s/%s.pyd" % (root, module_file)):
        return u"%s/%s.pyd" % (root, module_file)
    if os.path.isfile(u"%s/%s.pyw" % (root, module_file)):
        return u"%s/%s.pyw" % (root, module_file)
    if os.path.isfile(u"%s/%s.pyo" % (root, module_file)):
        return u"%s/%s.pyo" % (root, module_file)
    if os.path.isfile(u"%s/%s.pyc" % (root, module_file)):
        return u"%s/%s.pyc" % (root, module_file)
    if os.path.isfile(u"%s/%s.pyz" % (root, module_file)):
        return u"%s/%s.pyz" % (root, module_file)
    return None


def formattedPath(path):
    path = decode(path)
    path = path.replace(u"\\", u"/")
    if path[-1] == u"/":
        path = path[:-1]
    return path.replace(u"\\", u"/")


n_id = uid()


def hashName(s):
    v = u"P" + hashString(n_id + s)
    return v


def fileModuleName(root, module_file):
    names = module_file[len(root) + 1:].split(u"/")
    if names[-1] == u"__init__.py":
        names.pop(-1)
    names[-1] = names[-1].split(u".")[0]
    return u".".join(names)


def absModuleName(module, current_file, level=0):
    if level <= 0:
        current_dir_path_sps = current_file.split(u"/")
        current_dir_path_sps.pop(-1)
    else:
        current_dir_path_sps = current_file.split(u"/")
        for i in range(level):
            current_dir_path_sps.pop(-1)
    path = u"/".join(current_dir_path_sps)
    module_file = searchModuleFile(path, module)
    if not module_file is None:
        return (fileModuleName(module_file), module_file)
    module_file = searchModuleFile(root_dir, module)
    if not module_file is None:
        return (fileModuleName(module_file), module_file)


class CompilePython(object):
    def __init__(self, module, current_src, root):
        u"""

        :param module:
        :type module: unicode
        :param current_src:
        :type current_src: unicode
        :param root:
        :type root: unicode
        """
        self.module = module
        self.current_src = formattedPath(current_src)
        self.root = formattedPath(root)

        self.attrs = dict()

        path = searchModuleFile(self.current_src, module)
        if path is None:
            path = searchModuleFile(self.root, module)
            if path is None:
                pass
        self.name = fileModuleName(self.root, path)


class Node(object):
    type = ""
    data = dict()

    def __init__(self, type):
        u"""

        :param type:
        :type type: unicode
        :param data:
        :type data: dict
        """
        self.type = type
        self.data = dict()


Root = Node("root")
modules = dict()


class BuildPython(object):
    def __init__(self, main_module=u"main", src=r"D:\Development\tools\test\build\mid"):
        self.main_module = main_module
        self.src = formattedPath(src)
        self.current_src = self.src
        self.current_file = None
        self.n_id = uid()

        self.Root = Node("root")
        self.modules = dict()

        self.Import(self.main_module)
        #
        # for k,v in self.modules.items():

        print self.modules

    def hashName(self, s):
        v = u"_" + hashString(self.n_id + s)
        return v

    def gotoFile(self, path):
        self.current_file = formattedPath(path)
        self.current_src = u"/".join(self.current_file.split(u"/")[:-1])

    def buildLine_Import(self, node, gl_space, loc_space):
        i = node
        for t in i.names:
            if not self.Import(t.name) is None:
                # self.Import(t.name)
                if not t.asname is None:
                    loc_space.data[t.asname] = self.modules.get(t.name)
                else:
                    n = t.name.split(".")[0]
                    loc_space.data[n] = self.modules.get(n)
                t.name = ".".join([self.hashName(n) for n in t.name.split(".")])

    def buildLine_Assign(self, node, gl_space, loc_space):
        py_value_re = re.compile(r"__.*__")
        for t in node.targets:
            if isinstance(t, ast.Tuple):
                for l in t.elts:
                    if py_value_re.match(l.id) is None:
                        n = Node("value")
                        n.value = l.id
                        loc_space.data[l.id] = n
                        l.id = self.hashName(l.id)
            else:
                if py_value_re.match(t.id) is None:
                    n = Node("value")
                    n.value = t.id
                    loc_space.data[t.id] = n
                    t.id = self.hashName(t.id)
        self.buildToken(node.value, gl_space, loc_space)
        self.buildValue(node.value, gl_space, loc_space)

    def buildLine_Call(self, node, gl_space, loc_space):
        self.buildToken(node, gl_space, loc_space)
        self.buildValue(node, gl_space, loc_space)

    def buildLine_Return(self, node, gl_space, loc_space):
        self.buildToken(node, gl_space, loc_space)
        self.buildValue(node, gl_space, loc_space)

    def buildVlaue_Tuple(self, node, gl_space, loc_space):
        for i in node.elts:
            self.buildValue(i, gl_space, loc_space)
            self.buildToken(i, gl_space, loc_space)

    def buildVlaue_List(self, node, gl_space, loc_space):
        for i in node.elts:
            self.buildValue(i, gl_space, loc_space)
            self.buildToken(i, gl_space, loc_space)

    def buildVlaue_Set(self, node, gl_space, loc_space):
        for i in node.elts:
            self.buildValue(i, gl_space, loc_space)
            self.buildToken(i, gl_space, loc_space)

    def buildVlaue_Dict(self, node, gl_space, loc_space):
        for k, v in zip(node.keys, node.values):
            self.buildValue(k, gl_space, loc_space)
            self.buildValue(v, gl_space, loc_space)
            self.buildToken(k, gl_space, loc_space)
            self.buildToken(v, gl_space, loc_space)

    def buildToken_Name(self, node, gl_space, loc_space):
        if node.id in loc_space.data:
            node.id = self.hashName(node.id)
        if node.id in gl_space.data:
            node.id = self.hashName(node.id)

    def buildToken_Attribute(self, node, gl_space, loc_space):
        attrs = list()
        n = node
        while True:
            attrs.insert(0, n)
            if not isinstance(n, ast.Attribute):
                break
            n = n.value
        space = loc_space
        for attr in attrs:
            if isinstance(attr, ast.Name):
                if attr.id in space.data:
                    space = space.data[attr.id]
                    attr.id = self.hashName(attr.id)
            elif isinstance(attr, ast.Attribute):
                if attr.attr in space.data:
                    space = space.data[attr.attr]
                    attr.attr = self.hashName(attr.attr)
            else:
                break

    def buildBlock_Class(self, node, gl_space, loc_space):
        next_space = Node("class")
        loc_space.data[node.name] = next_space

        # 修改类名称与基类名称
        node.name = self.hashName(node.name)
        for i in node.bases:
            self.buildToken(i, gl_space, loc_space)

        # 编译类的body部分
        for i in node.body:
            print "class >>", i
            self.buildLine(i, gl_space, next_space)
            self.buildBlock(i, gl_space, next_space)

    def buildBlock_Function(self, node, gl_space, loc_space):
        next_space = Node("function")

        loc_space.data[node.name] = next_space

        temporary_space = Node("temporary")

        node.name = self.hashName(node.name)
        for i in node.args.args:
            self.buildToken(i, gl_space, temporary_space)
        for i in node.body:
            print "fucn >>", i
            self.buildLine(i, gl_space, temporary_space)
            self.buildBlock(i, gl_space, temporary_space)

    def buildValue(self, node, gl_space, loc_space):
        if isinstance(node, ast.Tuple):
            self.buildVlaue_Tuple(node, gl_space, loc_space)
        elif isinstance(node, ast.List):
            self.buildVlaue_List(node, gl_space, loc_space)
        elif isinstance(node, ast.Set):
            self.buildVlaue_Set(node, gl_space, loc_space)
        elif isinstance(node, ast.Dict):
            self.buildVlaue_Dict(node, gl_space, loc_space)

    def buildLine(self, node, gl_space, loc_space):
        # import from
        if isinstance(node, ast.Import):
            self.buildLine_Import(node, gl_space, loc_space)
        # as name
        elif isinstance(node, ast.Assign):
            self.buildLine_Assign(node, gl_space, loc_space)
        elif isinstance(node, ast.Call):
            self.buildLine_Call(node, gl_space, loc_space)
        elif isinstance(node, ast.Return):
            self.buildLine_Return(node, gl_space, loc_space)

    def buildToken(self, node, gl_space, loc_space):
        if isinstance(node, ast.Attribute):
            self.buildToken_Attribute(node, gl_space, loc_space)
        elif isinstance(node, ast.Name):
            self.buildToken_Name(node, gl_space, loc_space)

    def buildBlock(self, node, gl_space, loc_space):
        if isinstance(node, ast.ClassDef):
            self.buildBlock_Class(node, gl_space, loc_space)
        elif isinstance(node, ast.FunctionDef):
            self.buildBlock_Function(node, gl_space, loc_space)

        # for i in nodes.body:
        #     print i
        #     # import from
        #     if isinstance(i, ast.Import):
        #         for t in i.names:
        #             self.Import(t.name)
        #             # self.Import(t.name)
        #             if not t.asname is None:
        #                 loc_space.data[t.asname] = self.modules.get(t.name)
        #             else:
        #                 n = t.name.split(".")[0]
        #                 loc_space.data[n] = self.modules.get(n)
        #             t.name = ".".join([self.hashName(n) for n in t.name.split(".")])
        #     # as name
        #     elif isinstance(i, ast.Assign):
        #         for t in i.targets:
        #             if isinstance(t, ast.Tuple):
        #                 for l in t.elts:
        #                     if py_value_re.match(l.id) is None:
        #                         n = Node("value")
        #                         n.value = l.id
        #                         loc_space.data[l.id] = n
        #                         l.id = self.hashName(l.id)
        #             else:
        #                 if py_value_re.match(t.id) is None:
        #                     n = Node("value")
        #                     n.value = t.id
        #                     loc_space.data[t.id] = n
        #                     t.id = self.hashName(t.id)
        #     elif isinstance(i, ast.FunctionDef):
        #         n = Node("func")
        #         n.name = i.name
        #         loc_space.data[i.name] = n
        #         i.name = self.hashName(i.name)
        #     elif isinstance(i, ast.ClassDef):
        #         n = Node("class")
        #         n.name = i.name
        #         loc_space.data[i.name] = n
        #         i.name = self.hashName(i.name)
        #     # set name
        #     elif isinstance(i, ast.Attribute):
        #         attrs = list()
        #         n = i
        #         while True:
        #             attrs.insert(0, n)
        #             if not isinstance(n, ast.Attribute):
        #                 break
        #             n = n.value
        #         space = loc_space
        #         for attr in attrs:
        #             if isinstance(attr, ast.Name):
        #                 if attr.id in space.data:
        #                     space = space.data[attr.id]
        #                     attr.id = self.hashName(attr.id)
        #             elif isinstance(attr, ast.Attribute):
        #                 if attr.attr in space.data:
        #                     space = space.data[attr.attr]
        #                     attr.attr = self.hashName(attr.attr)
        #             else:
        #                 break
        #     elif isinstance(i, ast.Name):
        #         if i.id in loc_space.data:
        #             i.id = self.hashName(i.id)

    def buildPy(self, path):
        module_node = Node("module")
        module_node.path = path

        code = readFile(self.current_file)
        nodes = ast.parse(code)
        for i in nodes.body:
            print i
            self.buildLine(i, module_node, module_node)
            self.buildBlock(i, module_node, module_node)
        # if isinstance(i, ast.Name):
        #     i.id = self.hashName(i.id)
        code = astunparse.unparse(nodes)
        writeFile(self.current_file, code)
        return module_node

    def buildAll(self, path):
        module_node = Node("module")
        module_node.path = path
        return module_node

    def _Import(self, module_name):
        path = searchModuleFile(self.current_src, module_name)
        if path is None:
            path = searchModuleFile(self.src, module_name)
            if path is None:
                return
        path = formattedPath(path)
        current_file = self.current_file
        current_src = self.current_src
        self.current_file = path
        self.current_src = u"/".join(self.current_file.split(u"/")[:-1])

        file_type = path.split(u".")[-1]
        if file_type == u"py":
            node = self.buildPy(path)
        else:
            node = self.buildAll(path)
        self.modules[module_name] = node

        self.current_file = current_file
        self.current_src = current_src
        return node

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
        return modules[0]

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
