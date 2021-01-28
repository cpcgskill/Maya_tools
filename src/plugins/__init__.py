#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/12/30 21:18
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from config import *

if DEBUG:
    from . import mesh_mirror_inspection
    from . import controller_cleanup
    from . import loc_node
    from . import unloc_node
    from . import loc_scenes
    from . import clean_up_scenes_with_one_click
    from . import one_click_cleanup_of_selected_objects
    from . import select_nodes

    reload(mesh_mirror_inspection)
    reload(controller_cleanup)
    reload(loc_node)
    reload(unloc_node)
    reload(loc_scenes)
    reload(clean_up_scenes_with_one_click)
    reload(one_click_cleanup_of_selected_objects)
    reload(select_nodes)

from . import mesh_mirror_inspection
from . import controller_cleanup
from . import loc_node
from . import unloc_node
from . import loc_scenes
from . import clean_up_scenes_with_one_click
from . import one_click_cleanup_of_selected_objects
from . import select_nodes

plugins = [
    mesh_mirror_inspection,
    controller_cleanup,
    loc_node,
    unloc_node,
    loc_scenes,
    clean_up_scenes_with_one_click,
    one_click_cleanup_of_selected_objects,
    select_nodes
]
