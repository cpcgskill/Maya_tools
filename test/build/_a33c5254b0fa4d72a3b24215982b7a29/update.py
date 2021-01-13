
import sys
import _a33c5254b0fa4d72a3b24215982b7a29
_a33c5254b0fa4d72a3b24215982b7a29.update = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/12/31 21:39\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
import requests
import time
import json
import urllib2
import zipfile
from _a33c5254b0fa4d72a3b24215982b7a29.config import *
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.api.OpenMaya import MGlobal
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.cmds import refresh, CPMelError
from _a33c5254b0fa4d72a3b24215982b7a29.CPMel.tool import decode

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
                if ((time.time() - time1) > 2):
                    p = ((count / length) * 100)
                    speed = ((((count - count_tmp) / 1024) / 1024) / 2)
                    count_tmp = count
                    MGlobal.displayInfo(((((((name + u': ') + u'{:.2f}'.format(p)) + u'%') + u' Speed: ') + u'{:.2f}'.format(speed)) + u'M/S'))
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
        raise CPMelError(u'\u627e\u4e0d\u5230\u53ef\u89e3\u538b\u6587\u4ef6')

def update():
    MGlobal.displayInfo(u'\u83b7\u53d6\u66f4\u65b0\u4fe1\u606f')
    refresh()
    data = json.loads(updateinfo())
    for (k, v) in data.items():
        MGlobal.displayInfo(((str(k) + u': ') + str(v)))
        refresh()
    if (int((Version * 10)) < int((data.get(u'version', (-1)) * 10))):
        url = data[u'url']
        MGlobal.displayInfo(u'\u4e0b\u8f7d\u4e2d')
        refresh()
        downloadFile((PATH + u'/update.zip'), url)
        MGlobal.displayInfo(u'\u89e3\u538b\u4e2d')
        refresh()
        unzipFile((PATH + u'/update.zip'), PATH)
        MGlobal.displayInfo(u'\u66f4\u65b0\u5b8c\u6210')
        refresh()
        return
    MGlobal.displayInfo(u'\u5df2\u7ecf\u662f\u6700\u65b0\u7684\u7248\u672c\u4e86\uff01')
    refresh()
    return

def updateinfo():
    url = u'http://tools.cpcgskill.com/updateinfo'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response.read()
