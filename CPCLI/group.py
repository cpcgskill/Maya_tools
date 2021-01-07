#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/5 20:39
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


n_id = uid()


def hashName(s):
    v = u"CP_" + hashString(n_id + s)
    return v


class ModuleNode(object):
    path = ""
    buffers = ""


# def group()
main_module = r"main"
src = r"D:\Development\tools\test\src"
buidl_dir = r"D:\Development\tools\test\build"

re_o = re.compile(r".*\.(py|pyd|pyo|pyw)$")
main_module = main_module.replace(u"\\", u"/")
src = src.replace(u"\\", u"/")
buidl_dir = buidl_dir.replace(u"\\", u"/")

mid = buidl_dir + u"/mid"
buidl_dir = buidl_dir + u"/build"

# if not os.path.isdir(mid):
#     os.mkdir(mid)
# if not os.path.isdir(buidl_dir):
#     os.mkdir(buidl_dir)

utils.copyDir(src, mid)

root_dir = mid
main_file = u"%s/%s.py" % (mid, main_module)
current_file = main_file

src_size = len(mid)
root_dir_size = len(root_dir)

files = [(_root + u"\\" + file).replace(u"\\", u"/")[src_size:][1:] for _root, dirs, files in os.walk(mid) for file in
         files]
files = [i for i in files if not re_o.match(i) is None]
print files


def searchModuleFile(root, module):
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


def fileModuleName(module_file):
    names = module_file[root_dir_size + 1:].split(u"/")
    if names[-1] == u"__init__.py":
        names.pop(-1)
    names[-1] = names[-1].split(u".")[0]
    return u".".join(names)


def absModuleName(module, level=0):
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


buidl_modules = dict()


def addBuildFiles(module_path):
    global current_file
    code = readFile(module_path)
    r_node = ast.parse(code)
    current_file = module_path
    for i in ast.walk(r_node):
        if isinstance(i, ast.ImportFrom):
            try:
                module_name, module_file = absModuleName(i.module, i.level)
                print module_name, module_file
                buidl_modules[module_name] = module_file
                addBuildFiles(module_file)
            except:
                continue

        if isinstance(i, ast.Import):
            pass
            for t in i.names:
                try:
                    module_name, module_file = absModuleName(t.name, 0)
                    print module_name, module_file
                    buidl_modules[module_name] = module_file
                    addBuildFiles(module_file)
                except:
                    continue
    # writeFile(module_path, code)
def buildModule(file):
    global current_file
    code = readFile(file)
    r_node = ast.parse(code)
    current_file = file
    for i in ast.walk(r_node):
        pass

addBuildFiles(current_file)
print buidl_modules
buildModule(main_file)