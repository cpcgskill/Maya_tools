#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/13 18:14
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from CPCLI import *

scripts = r"D:\Development\tools\script"
src = r"D:\Development\tools\src"
build = r"D:\Development\tools\build"

group_name = utils.uidname()
main_script = r"entrance.py"

scripts = formattedPath(scripts)
src = formattedPath(src)
build = formattedPath(build)

group_src = u"{}/{}".format(build, group_name)
copyDir(src, group_src)
writeFile(u"{}/{}".format(build, main_script),
          readFile(u"{}/{}".format(scripts, main_script)))

group(group_src, u"{}/{}".format(build, main_script), group_name)
