
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n'

class its(object, ):

    def __init__(self, *args):
        self.__its = tuple(((t for t in i) for i in args))
        self.__obj_size = len(args)

    def __iter__(self):
        return self

    def next(self):
        objs = tuple((i.next() for i in self.__its))
        if (len(objs) != self.__obj_size):
            raise StopIteration
        return objs

def MAyyayIt(obj):
    return (obj[i] for i in range(obj.length()))

class MItForIt(object, ):

    def __init__(self, obj):
        self.__CP_is_start = True
        self.__obj = obj
        self.__obj.reset()

    def next(self):
        if self.__CP_is_start:
            self.__CP_is_start = False
        else:
            self.__obj.next()
        if self.__obj.isDone():
            raise StopIteration
        else:
            return self.__obj
