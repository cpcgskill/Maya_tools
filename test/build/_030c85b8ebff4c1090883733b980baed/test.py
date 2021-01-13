
import sys
import _030c85b8ebff4c1090883733b980baed
_030c85b8ebff4c1090883733b980baed.test = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2021/1/3 20:19\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
import os
import zipfile

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
zip_src = 'D:\\Development\\tools\\testzip\\tools.zip'
dst_dir = 'D:\\\\Development\\\\tools\\\\testzip'

def unzipFile(zip_src, dst_dir):
    if zipfile.is_zipfile(zip_src):
        with zipfile.ZipFile(zip_src, 'r') as fz:
            for file in fz.namelist():
                v = fz.extract(file, dst_dir)
    else:
        raise 
