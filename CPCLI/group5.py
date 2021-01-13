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
import uuid
import hashlib
import ast
import astunparse

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
from main import *
win = MainWindow()
win.show()
"""


class BuildPython(object):
    head = u"""\
import sys
import <<group>>

<<group>>.<<module>> = sys.modules.get(__name__)
"""

    def __init__(self,
                 src=r"D:\Development\tools\test\src",
                 build=r"D:\Development\tools\test\build",
                 group_name="test"):
        src = formattedPath(src)
        build = formattedPath(build)
        build = u"%s/%s" % (build, group_name)

        copyDir(src, build)

        self.src = build
        self.current_src = self.src
        self.current_file = None
        self.n_id = u"_" + uid()
        self.files = list()
        self.build_end_files = list()
        self.group_name = group_name

        # 获得所有文件

        for root, dirs, files in os.walk(self.src):
            for file in files:
                self.files.append(formattedPath(u"%s/%s" % (root, file)))

    def run(self, script=_test_script_):
        # 确定要编译的文件
        build_files = [i for i in self.files if i.split(u".")[-1] == u"py"]

        # 对文件进行编译
        for i in build_files:
            self.buildPyFile(i)

        # 添加运行时头
        for i in build_files:
            module_name = self.fileModuleName(self.src, i)
            if len(module_name.split(u".")) == 1:
                code = readFile(i)
                nodes = ast.parse(code)
                for t in reversed(self.buildTemplate(module_name.split(u".")[0])):
                    nodes.body.insert(0, t)
                writeFile(i, astunparse.unparse(nodes))

        # 编译脚本程序
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
                        if t.asname is None:
                            head = ast.alias()
                            head.name = u".".join(module_names[:2])
                            head.asname = module_names[1]

                            t.asname = u"_"
                            i.names[ID] = [head, t]
                        else:
                            i.names[ID] = [t]
                        t.name = module_name
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
        code = astunparse.unparse(nodes)
        return code

    def buildTemplate(self, module_name):
        head = self.head
        head = head.replace(u"<<group>>", self.group_name)
        head = head.replace(u"<<module>>", module_name)
        return ast.parse(head).body

    def buildPyFile(self, file):
        if file in self.build_end_files:
            return
        _up_file = self.current_file
        self.current_file = formattedPath(file)
        self.current_src = u"/".join(self.current_file.split(u"/")[:-1])
        try:
            code = readFile(self.current_file)
            # 添加到完成编译的文件里
            self.build_end_files.append(self.current_file)
            nodes = ast.parse(code)
            for i in ast.walk(nodes):
                if isinstance(i, ast.Import):
                    for ID in range(len(i.names)):
                        t = i.names[ID]
                        file = self.searchModuleFile(self.src, t.name)
                        if not file is None:
                            module_name = self.fileModuleName(self.src, file)
                            module_name = u"%s.%s" % (self.group_name, module_name)
                            module_names = module_name.split(u".")
                            op_module_names = t.name.split(u".")

                            if t.asname is None:
                                head = ast.alias()
                                head.name = u".".join(module_names[:len(module_names) - (len(op_module_names) - 1)])
                                head.asname = module_names[len(module_names) - len(op_module_names)]
                                t.asname = u"_"
                                i.names[ID] = [head, t]
                            else:
                                i.names[ID] = [t]
                            t.name = module_name
                            # 对应的python文件
                            # self.buildPyFile(file)
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
                            # self.buildPyFile(file)
            code = astunparse.unparse(nodes)
            writeFile(self.current_file, code)
        except Exception as ex:
            if self.current_file in self.build_end_files:
                self.build_end_files.remove(self.current_file)
        finally:
            self.current_file = _up_file
            if not _up_file is None:
                self.current_src = u"/".join(self.current_file.split(u"/")[:-1])

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
        if len(names) <= 1:
            names[-1] = names[-1].split(u".")[0]
            return u".".join(names)
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


o = BuildPython(group_name=uid())
print o.run()
