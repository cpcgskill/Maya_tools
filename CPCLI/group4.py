#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/11 21:05
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


_test_script_ = """\
import main
import main as t
from main import *
"""


class BuildPython(object):
    def __init__(self, script=_test_script_, src=r"D:\Development\tools\test\build\mid"):
        self.src = formattedPath(src)
        self.current_src = self.src
        self.current_file = None
        self.n_id = u"_" + uid()
        self.files = list()
        self.group_name = "mid"
        for root, dirs, files in os.walk(self.src):
            for file in files:
                self.files.append(formattedPath(u"%s/%s" % (root, file)))
        nodes = ast.parse(script)
        for i in ast.walk(nodes):
            if isinstance(i, ast.Import):
                for ID in range(len(i.names)):
                    t = i.names[ID]
                    file = self.searchModuleFile(self.src, t.name)
                    if not file is None:
                        module_name = self.fileModuleName(self.src, file)
                        module_name = u"%s.%s" % (self.group_name, module_name)
                        module_names = module_name.split(u".")
                        head = ast.alias()
                        head.name = u".".join(module_names[:2])
                        if t.asname is None:
                            head.asname = module_names[1]
                        else:
                            head.asname = u"_"
                        if t.asname is None:
                            t.asname = u"_"
                        i.names[ID] = [head, t]
                        t.name = module_name
                        self.buildPyFile(file)
                    else:
                        i.names[ID] = [t]
                i.names = [l for t in i.names for l in t]
            elif isinstance(i, ast.ImportFrom):
                if i.level < 1:
                    file = self.searchModuleFile(self.src, i.module)
                    if not file is None:
                        module_name = self.fileModuleName(self.src, file)
                        module_name = u"%s.%s" % (self.group_name, module_name)
                        i.module = module_name
                        self.buildPyFile(file)
        code = astunparse.unparse(nodes)
        print code

    def buildPyFile(self, file):
        _up_file = self.current_file
        self.current_file = formattedPath(file)
        self.current_src = u"/".join(self.current_file.split(u"/")[:-1])
        try:
            code = readFile(self.current_file)
            nodes = ast.parse(code)
            for i in ast.walk(nodes):
                if isinstance(i, ast.Import):
                    for ID in range(len(i.names)):
                        t = i.names[ID]
                        file = self.searchModuleFile(self.current_src, t.name)
                        if file is None:
                            file = self.searchModuleFile(self.src, t.name)
                        if not file is None:
                            module_name = self.fileModuleName(self.src, file)
                            module_name = u"%s.%s" % (self.group_name, module_name)
                            module_names = module_name.split(u".")
                            op_module_names = t.name.split(u".")

                            # 头部
                            head = ast.alias()
                            head.name = u".".join(module_names[:len(module_names) - (len(op_module_names) - 1)])
                            if t.asname is None:
                                head.asname = module_names[len(module_names) - len(op_module_names)]
                            else:
                                head.asname = u"_"
                            # 身体 （原来的导入）
                            if t.asname is None:
                                t.asname = u"_"
                            i.names[ID] = [head, t]
                            t.name = module_name
                            # 对应的python文件
                            self.buildPyFile(file)
                        else:
                            i.names[ID] = [t]
                    i.names = [l for t in i.names for l in t]
                elif isinstance(i, ast.ImportFrom):
                    if i.level < 1:
                        file = self.searchModuleFile(self.current_file, i.module)
                        if file is None:
                            file = self.searchModuleFile(self.src, i.module)
                        if not file is None:
                            module_name = self.fileModuleName(self.src, file)
                            module_name = u"%s.%s" % (self.group_name, module_name)
                            i.module = module_name
                            self.buildPyFile(file)
            code = astunparse.unparse(nodes)
            print ">> ", file, " :\n", code
            writeFile(self.current_file, code)
        finally:
            self.current_file = _up_file
            if not _up_file is None:
                self.current_src = u"/".join(self.current_file.split(u"/")[:-1])

    def Import(self, name):
        pass

    def ImportFrom(self, name, levex=0):
        pass

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


BuildPython()
