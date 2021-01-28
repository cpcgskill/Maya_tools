
import sys
import _44a6428a69494567aed2941f480fe31f
_44a6428a69494567aed2941f480fe31f.plugins = sys.modules.get(__name__)
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/12/30 21:18\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\n\n'
from _44a6428a69494567aed2941f480fe31f.config import *
if DEBUG:
    from . import mesh_mirror_inspection
    from . import controller_cleanup
    from . import loc_node
    from . import unloc_node
    from . import loc_scenes
    from . import clean_up_scenes_with_one_click
    from . import one_click_cleanup_of_selected_objects
    reload(mesh_mirror_inspection)
    reload(controller_cleanup)
    reload(loc_node)
    reload(unloc_node)
    reload(loc_scenes)
    reload(clean_up_scenes_with_one_click)
    reload(one_click_cleanup_of_selected_objects)
from . import mesh_mirror_inspection
from . import controller_cleanup
from . import loc_node
from . import unloc_node
from . import loc_scenes
from . import clean_up_scenes_with_one_click
from . import one_click_cleanup_of_selected_objects
plugins = [mesh_mirror_inspection, controller_cleanup, loc_node, unloc_node, loc_scenes, clean_up_scenes_with_one_click, one_click_cleanup_of_selected_objects]
