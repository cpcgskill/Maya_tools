#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/31 21:39
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import requests
import time
import json
import urllib2
import zipfile

from config import *
from CPMel.api.OpenMaya import MGlobal
from CPMel.cmds import refresh, CPMelError
from CPMel.tool import decode


def downloadFile(name, url):
    headers = {u'Proxy-Connection': u'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers[u'content-length'])
    with open(name, 'wb') as f:
        count = 0
        count_tmp = 0
        time1 = time.time()
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
                count += len(chunk)
                if time.time() - time1 > 2:
                    p = count / length * 100
                    speed = (count - count_tmp) / 1024 / 1024 / 2
                    count_tmp = count
                    MGlobal.displayInfo(
                        name + u': ' + u'{:.2f}'.format(p) + u'%' + u' Speed: ' + u'{:.2f}'.format(speed) + u'M/S')
                    refresh()
                    time1 = time.time()


def unzipFile(zip_src, dst_dir):
    if zipfile.is_zipfile(zip_src):
        with zipfile.ZipFile(zip_src, 'r') as fz:
            for file in fz.namelist():
                try:
                    MGlobal.displayInfo(file)
                    refresh()
                    fz.extract(file, dst_dir)
                except Exception as ex:
                    MGlobal.displayWarning(decode(str(ex)))
                    refresh()
    else:
        raise CPMelError(u"找不到可解压文件")


def update():
    MGlobal.displayInfo(u"获取更新信息")
    refresh()
    data = json.loads(updateinfo())
    for k, v in data.items():
        MGlobal.displayInfo(str(k) + u": " + str(v))
        refresh()

    if int(Version * 10) < int(data.get(u"version", -1) * 10):
        url = data[u"url"]
        MGlobal.displayInfo(u"下载中")
        refresh()
        downloadFile(PATH + u"/update.zip", url)
        MGlobal.displayInfo(u"解压中")
        refresh()
        unzipFile(PATH + u"/update.zip", PATH)
        MGlobal.displayInfo(u"更新完成")
        refresh()
        return
    MGlobal.displayInfo(u"已经是最新的版本了！")
    refresh()
    return


def updateinfo():
    url = u"http://tools.cpcgskill.com/updateinfo"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()
