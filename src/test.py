#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/1/3 20:19
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
import zipfile


def decode(s=''):
    u"""
    字符串解码函数

    :param s:
    :return:
    """
    if not isinstance(s, basestring):
        try:
            s = str(s)
        except:
            s = unicode(s)
    if type(s) == str:
        try:
            return s.decode("UTF-8")
        except UnicodeDecodeError:
            try:
                return s.decode("GB18030")
            except UnicodeDecodeError:
                try:
                    return s.decode("Shift-JIS")
                except UnicodeDecodeError:
                    try:
                        return s.decode("EUC-KR")
                    except UnicodeDecodeError:
                        return unicode(s)
    return s.encode("UTF-8").decode("UTF-8")


zip_src = r"D:\Development\tools\testzip\tools.zip"
dst_dir = r"D:\\Development\\tools\\testzip"
def unzipFile(zip_src, dst_dir):
    if zipfile.is_zipfile(zip_src):
        with zipfile.ZipFile(zip_src, 'r') as fz:
            for file in fz.namelist():
                v = fz.extract(file, dst_dir)
    else:
        raise