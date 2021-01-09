# !/usr/bin/python
# -*-coding:utf-8 -*-
import sys


class TTT(object):
    pass


path = sys.path


class LLL(TTT):
    a = (1, 2)
    b = [1, 2]
    c = {1, 2}
    d = {"a": a, "b": b, "c": c}


def TF(t, s=1, *args, **kwargs):
    www = LLL()
    return (www, 1)
