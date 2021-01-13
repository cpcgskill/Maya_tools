
u'\n:\u521b\u5efa\u65f6\u95f4: 2020/5/18 23:57\n:\u4f5c\u8005: \u82cd\u4e4b\u5e7b\u7075\n:\u6211\u7684\u4e3b\u9875: https://cpcgskill.com\n:QQ: 2921251087\n:\u7231\u53d1\u7535: https://afdian.net/@Phantom_of_the_Cang\n:aboutcg: https://www.aboutcg.org/teacher/54335\n:bilibili: https://space.bilibili.com/351598127\nCPMel.cmds\u6a21\u5757\u8282\u70b9\u7c7b\u578b\u5b9a\u4e49\n'
import array
import maya.cmds as cmds
import maya.mel as mel
from . import basedata
from ...api import apiwrap
from ... import core as cmcore
from .nodedata import *
from .basedata import *
from ...api.OpenMaya import *
from ...api.OpenMayaAnim import *
__all__ = ['Transform', 'MeshVtx', 'MeshEdge', 'MeshFace', 'Mesh', 'CurveCv', 'Curve', 'SurfaceCv', 'Surface', 'SkinCluster']
ScriptUtil = MScriptUtil()

class Transform(DagNode, ):
    __metaclass__ = ObjectMetadef(MFn.kTransform)

    def __init__(self, obj=MObject, uuid=MUuid, uuid_s=u''):
        super(Transform, self).__init__(obj, uuid, uuid_s)

    def __getattribute__(self, item):
        u'\n        .\u8bbf\u95ee\u64cd\u4f5c\n\n        :param item:\n        :return:\n        '
        try:
            return object.__getattribute__(self, item)
        except AttributeError:
            try:
                return self.attr(item)
            except cmcore.CPMelErrorBase:
                try:
                    return getattr(self.getShape(), item)
                except cmcore.CPMelErrorBase:
                    raise cmcore.CPMelError(u'\u627e\u4e0d\u5230\u5c5e\u6027')

    def getShape(self, index=0):
        path = self.fn.dagPath()
        int_p = ScriptUtil.asUintPtr()
        path.numberOfShapesDirectlyBelow(int_p)
        shape_size = ScriptUtil.getUint(int_p)
        if (shape_size > 0):
            path.extendToShapeDirectlyBelow(index)
            return Global.objToNode(path.node())
        else:
            raise cmcore.CPMelError(u'\u6ca1\u6709\u5f62\u72b6\u8282\u70b9')

    def getShapes(self):
        path = self.fn.dagPath()
        int_p = ScriptUtil.asUintPtr()
        path.numberOfShapesDirectlyBelow(int_p)
        shape_size = ScriptUtil.getUint(int_p)
        if (shape_size > 0):
            objs = list()
            for i in range(shape_size):
                path = self.fn.dagPath()
                path.extendToShapeDirectlyBelow(i)
                obj = self.Globalfunction.objToNode(path.node())
                objs.append(obj)
            return objs
        else:
            return []

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n        :return: MFn\n        :rtype: MFnDependencyNode\n        '
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnTransform(path)

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param path: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        '
        return path.hasFn(MFn.kTransform)

class MeshVtx(Components1Base, ):
    components_type_str = 'vtx'
    __metaclass__ = componentsTypesMetadef

    def cp__init_componenrs(self):
        (dag, obj) = self.Globalfunction.nameToMDagPath(self.compile())
        self.it = MItMeshVertex(dag, obj)

    @Components1Base.IsSingleComponent
    def verticesToFace(self):
        return self.node.verticesToFace(self.index)

    @Components1Base.IsSingleComponent
    def verticesToEdge(self):
        return self.node.verticesToEdge(self.index)

    @Components1Base.IsSingleComponent
    def verticesToVertices(self):
        return self.node.verticesToVertices(self.index)

    @Components1Base.IsSingleComponent
    def setPoint(self, point, space=basedata.Space.object):
        return self.node.setPoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getPoint(self.index, space)

class MeshEdge(Components1Base, ):
    components_type_str = 'e'
    __metaclass__ = componentsTypesMetadef

    def cp__init_componenrs(self):
        (dag, obj) = self.Globalfunction.nameToMDagPath(self.compile())
        self.it = MItMeshEdge(dag, obj)

    @Components1Base.IsSingleComponent
    def edgeToFace(self):
        return self.node.edgeToFace(self.index)

    @Components1Base.IsSingleComponent
    def edgeToEdge(self):
        return self.node.edgeToEdge(self.index)

    @Components1Base.IsSingleComponent
    def edgeToVertices(self):
        return self.node.edgeToVertices(self.index)

    @Components1Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setEdgePoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.setEdgePoint(self.index, space)

class MeshFace(Components1Base, ):
    components_type_str = 'f'
    __metaclass__ = componentsTypesMetadef

    @Components1Base.IsSingleComponent
    def faceToFace(self):
        return self.node.faceToFace(self.index)

    @Components1Base.IsSingleComponent
    def faceToEdge(self):
        return self.node.faceToEdge(self.index)

    @Components1Base.IsSingleComponent
    def faceToVertices(self):
        return self.node.faceToVertices(self.index)

    @Components1Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setFacePoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getFacePoint(space)

class Mesh(DagNode, ):
    __metaclass__ = ObjectMetadef(MFn.kMesh)

    def __init__(self, *args):
        super(Mesh, self).__init__(*args)
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        self.it_vtx = MItMeshVertex(path)
        self.it_e = MItMeshEdge(path)
        self.it_f = MItMeshPolygon(path)
        self.vtx = MeshVtx(self)
        self.vtx.cp__init_componenrs()
        self.e = MeshEdge(self)
        self.e.cp__init_componenrs()
        self.f = MeshFace(self)
        self.f.cp__init_componenrs()

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n        :return: MFn\n        '
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnMesh(path)

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param path: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        '
        return path.hasFn(MFn.kMesh)

    @property
    def MeshVertex(self):
        return apiwrap.MeshVertex(('%s.vtx[*]' % self.name()))

    def vertexToFace(self, index=0):
        u'\n        \u83b7\u5f97\u8fde\u63a5\u5230\u8f93\u5165\u9876\u70b9\u7684\u9762\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_vtx.getConnectedFaces(ids)
        return basedata.IntArray(ids)

    def vertexToEdge(self, index=0):
        u'\n        \u83b7\u5f97\u8fde\u63a5\u5230\u8f93\u5165\u9876\u70b9\u7684\u8fb9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_vtx.getConnectedEdges(ids)
        return basedata.IntArray(ids)

    def vertexTovertex(self, index=0):
        u'\n        \u83b7\u5f97\u56f4\u7ed5\u8f93\u5165\u9876\u70b9\u7684\u9876\u70b9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_vtx.getConnectedVertices(ids)
        ids.append(index)
        return basedata.IntArray(ids)

    def edgeToFace(self, index=0):
        u'\n        \u83b7\u5f97\u8fde\u63a5\u7684\u8f93\u5165\u8fb9\u7684\u9762\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_e.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_e.getConnectedFaces(ids)
        return basedata.IntArray(ids)

    def edgeToEdge(self, index=0):
        u'\n        \u83b7\u5f97\u56f4\u7ed5\u8f93\u5165\u8fb9\u7684\u8fb9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_e.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_e.getConnectedEdges(ids)
        ids.append(index)
        return basedata.IntArray(ids)

    def edgeTovertex(self, index=0):
        u'\n        \u83b7\u5f97\u8fde\u63a5\u7684\u8f93\u5165\u8fb9\u7684\u9876\u70b9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        int_2_ptr = ScriptUtil.asInt2Ptr()
        self.fn.getEdgeVertices(index, int_2_ptr)
        ids = (ScriptUtil.getInt2ArrayItem(int_2_ptr, 0, 0), ScriptUtil.getInt2ArrayItem(int_2_ptr, 0, 1))
        return ids

    def faceToFace(self, index=0):
        u'\n        \u83b7\u5f97\u56f4\u7ed5\u8f93\u5165\u9762\u7684\u9762\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        ids = MIntArray()
        self.it_f.getConnectedFaces(ids)
        ids.append(index)
        return basedata.IntArray(ids)

    def faceToEdge(self, index=0):
        u'\n        \u83b7\u5f97\u8fde\u63a5\u7684\u8f93\u5165\u9762\u7684\u8fb9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        idsa = MIntArray()
        self.it_f.getEdges(idsa)
        return basedata.IntArray(idsa)

    def faceToVertex(self, index=0):
        u'\n        \u83b7\u5f97\u8fde\u63a5\u7684\u8f93\u5165\u9762\u7684\u9876\u70b9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        return basedata.IntArray([t for i in self.faceToEdge(index) for t in self.edgeTovertex(i)])

    def VerticesIsBoundary(self, index):
        u'\n        \u68c0\u67e5\u8f93\u5165\u7684\u9876\u70b9\u662f\u5426\u4e3a\u8fb9\u754c\u70b9\n\n        :param index:\n        :return:\n        :rtype: list\n        '
        self.it_vtx.setIndex(index, ScriptUtil.asIntPtr())
        return self.it_vtx.onBoundary()

    def setPoint(self, index, point, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6e\u9876\u70b9\u4f4d\u7f6e\n\n        :param index: \u9876\u70b9ID\n        :param point: \u4f4d\u7f6e\u53c2\u6570\n        :param space: \u53d8\u6362\u7a7a\u95f4\n        :return:\n        '
        if (not isinstance(point, MPoint)):
            point = MPoint(point[0], point[1], point[2])
        unpoint = MPoint()
        self.fn.getPoint(index, unpoint, space)

        def doIt():
            self.functionSet().setPoint(index, point, space)

        def undoIt():
            self.functionSet().setPoint(index, unpoint, space)
        return cmcore.addCommand(doIt, undoIt)

    def getPoint(self, index, space=basedata.Space.object):
        u'\n        \u83b7\u5f97\u9876\u70b9\u4f4d\u7f6e\n\n        :param index: \u9876\u70b9ID\n        :param space: \u53d8\u6362\u7a7a\u95f4\n        :return:\n        :rtype:basedata.Double3\n        '
        point = MPoint()
        self.fn.getPoint(index, point, space)
        return basedata.Double3(point)

    def setPoints(self, points, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6e\u6240\u6709\u9876\u70b9\u4f4d\u7f6e\n\n        :param points: \u70b9\u4f4d\u7f6e\u5217\u8868\n        :param space: \u53d8\u6362\u7a7a\u95f4\n        :return:\n        '
        point_size = len(points)
        if (len(points) != self.fn.numVertices()):
            raise cmcore.CPMelError(u'\u8f93\u5165\u7684\u70b9\u6570\u91cf\u4e0e\u6a21\u578b\u9876\u70b9\u6570\u4e0d\u4e00\u81f4')
        if (not isinstance(points, MPointArray)):
            m_points = MPointArray(point_size)
            [m_points.set(ID, i[0], i[1], i[2]) for (ID, i) in enumerate(points)]
            points = m_points
        unpoints = MPointArray()
        self.fn.getPoints(unpoints, space)

        def doIt():
            self.functionSet().setPoints(points, space)

        def undoIt():
            self.functionSet().setPoints(unpoints, space)
        return cmcore.addCommand(doIt, undoIt)

    def getPoints(self, space=basedata.Space.object):
        u'\n        \u83b7\u5f97\u6240\u6709\u9876\u70b9\u4f4d\u7f6e\n\n        :param space: \u53d8\u6362\u7a7a\u95f4\n        :return: MPointArray\n        '
        points = MPointArray()
        self.fn.getPoints(points, space)
        return basedata.NewDouble3s(points)

    def setEdgePoint(self, index=0, point=basedata.Double3, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6e\u8fb9\u4f4d\u7f6e\n        :param index:\n        :param point:\n        :param space:\n        :return:\n        '
        if (not isinstance(point, MPoint)):
            point = MPoint(point[0], point[1], point[2])
        (strat_id, end_id) = self.edgeToVertices(index)
        strat_point = MPoint()
        self.fn.getPoint(strat_id, strat_point, space)
        end_point = MPoint()
        self.fn.getPoint(end_id, end_point, space)
        mid_point = ((strat_point + end_point) * 0.5)
        do_strat_point = (point + (strat_point - mid_point))
        do_end_point = (point + (end_point - mid_point))

        def doIt():
            fn = self.functionSet()
            fn.setPoint(strat_id, do_strat_point, space)
            fn.setPoint(end_id, do_end_point, space)

        def undoIt():
            fn = self.functionSet()
            fn.setPoint(strat_id, strat_point, space)
            fn.setPoint(end_id, end_point, space)
        return cmcore.addCommand(doIt, undoIt)

    def getEdgePoint(self, index=0, space=basedata.Space.object):
        u'\n        \u83b7\u5f97\u8fb9\u4f4d\u7f6e\n\n        :param index:\n        :param space:\n        :return:\n        '
        (strat_id, end_id) = self.edgeToVertices(index)
        strat_point = self.getPoint(strat_id, space)
        end_point = self.getPoint(end_id, space)
        mid_point = ((strat_point + end_point) * 0.5)
        return basedata.Double3(mid_point)

    def setFacePoint(self, index=0, point=basedata.Double3, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6e\u9762\u4f4d\u7f6e\n\n        :param index:\n        :param point:\n        :param space:\n        :return:\n        '
        if (not isinstance(point, MVector)):
            point = MVector(point[0], point[1], point[2])
        ids = self.faceToVertex(index)
        strat_points = list()
        for i in ids:
            strat_point = MPoint()
            self.fn.getPoint(i, strat_point, space)
            strat_points.append(strat_point)
        m_point = MPoint()
        for i in strat_points:
            m_point = (i + m_point)
        m_point = (m_point / len(ids))
        end_points = list()
        for i in xrange(len(ids)):
            end_points.append(MPoint(((strat_points[i] - m_point) + point)))

        def doIt():
            fn = self.functionSet()
            for i in xrange(len(ids)):
                fn.setPoint(ids[i], end_points[i], space)

        def undoIt():
            fn = self.functionSet()
            for i in xrange(len(ids)):
                fn.setPoint(ids[i], strat_points[i], space)
        return cmcore.addCommand(doIt, undoIt)

    def getFacePoint(self, index=0, space=basedata.Space.object):
        u'\n        \u83b7\u5f97\u9762\u4f4d\u7f6e\n\n        :param index:\n        :param space:\n        :return:\n        '
        self.it_f.setIndex(index, ScriptUtil.asIntPtr())
        point = self.it_f.center(space)
        return basedata.Double3(point)

    def getClosestPointAndFace(self, point=basedata.Double3, space=basedata.Space.object):
        u'\n        \u83b7\u5f97\u6700\u8fd1\u70b9\u4e0e\u6700\u8fd1\u9762ID\n\n        :param point: \u8f93\u5165\u7684Double3\n        :param space: \u5728\u4ec0\u4e48\u7a7a\u95f4\u4e0b\u8fd0\u884c\n        :return: Double3\uff0c\u9762ID\n        '
        if (not isinstance(point, MPoint)):
            point = MPoint(point[0], point[1], point[2])
        out_point = MPoint()
        closest_face_id = ScriptUtil.asIntPtr()
        self.fn.getClosestPoint(point, out_point, space, closest_face_id)
        return (basedata.Double3(out_point), ScriptUtil.getInt(closest_face_id))

    def getClosestPoitnAndVertices(self, point=basedata.Double3, space=basedata.Space.object):
        u'\n        \u8fd4\u56de\u6700\u8fd1\u70b9\u4e0e\u6700\u8fd1\u9876\u70b9ID\n\n        :param point: \u8f93\u5165\u7684Double3\n        :param space: \u5728\u4ec0\u4e48\u7a7a\u95f4\u4e0b\u8fd0\u884c\n        :return: Double3\uff0c\u70b9ID\n        '
        if (not isinstance(point, MPoint)):
            point = MPoint(point[0], point[1], point[2])
        c_point = MPoint()
        closest_face_id = ScriptUtil.asIntPtr()
        self.fn.getClosestPoint(point, c_point, space, closest_face_id)
        faceid = ScriptUtil.getInt(closest_face_id)
        ids = MIntArray()
        self.fn.getPolygonVertices(faceid, ids)

        def _(i):
            pt = MPoint()
            self.fn.getPoint(i, pt, space)
            return point.distanceTo(pt)
        return (basedata.Double3(c_point), min(((i, _(i)) for i in ids), key=(lambda i: i[1]))[0])

class CurveCv(Components1Base, ):
    components_type_str = 'cv'
    __metaclass__ = componentsTypesMetadef

    @Components1Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setPoint(self.index, point, space)

    @Components1Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getPoint(self.index, space)

class Curve(DagNode, ):
    __metaclass__ = ObjectMetadef(MFn.kCurve)

    def __init__(self, *args):
        super(Curve, self).__init__(*args)
        self.cv = CurveCv(self)
        self.cv.cp__init_componenrs()

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param path: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        '
        return path.hasFn(MFn.kCurve)

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n        :return: MFn\n        '
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnNurbsCurve(path)

    def setPoint(self, index=0, point=basedata.Double3, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6e\u6307\u5b9aCV\u70b9\u7684\u4f4d\u7f6e\n\n        :param index:\n        :param point:\n        :param space:\n        :return:\n        '
        if (not isinstance(point, MPoint)):
            point = MPoint(point[0], point[1], point[2])
        unpoint = MPoint()
        self.fn.getCV(index, unpoint)
        self.fn.setCV(index, point, space)

        def doIt():
            fn = self.functionSet()
            fn.setCV(index, point, space)
            fn.updateCurve()

        def undoIt():
            fn = self.functionSet()
            fn.setCV(index, unpoint, space)
            fn.updateCurve()
        return cmcore.addCommand(doIt, undoIt)

    def getPoint(self, index=0, space=basedata.Space.object):
        u'\n        \u83b7\u5f97CV\u70b9\u7684\u4f4d\u7f6e\n\n        :param index:\n        :param space:\n        :return:\n        '
        point = MPoint()
        self.fn.getCV(index, point, space)
        return basedata.Double3(point)

    def setPoints(self, points, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6e\u6240\u6709CV\u70b9\u7684\u4f4d\u7f6e\n\n        :param points:\n        :param space:\n        :return:\n        '
        point_size = len(points)
        num_cvsize = self.numCvs()
        if (len(points) != num_cvsize):
            raise cmcore.CPMelError(u'\u8f93\u5165\u7684\u70b9\u6570\u91cf\u4e0e\u66f2\u7ebf\u70b9\u6570\u4e0d\u4e00\u81f4')
        if (not isinstance(points, MPointArray)):
            m_points = MPointArray(point_size)
            [m_points.set(ID, i[0], i[1], i[2]) for (ID, i) in enumerate(points)]
            points = m_points
        un_points = MPointArray()
        self.fn.getCVs(un_points, space)

        def doIt():
            fn = self.functionSet()
            fn.setCVs(points, space)
            fn.updateCurve()

        def undoIt():
            fn = self.functionSet()
            fn.setCVs(un_points, space)
            fn.updateCurve()
        cmcore.addCommand(doIt, undoIt)

    def getPoints(self, space=basedata.Space.object):
        u'\n        \u83b7\u5f97\u6240\u6709CV\u70b9\u7684\u4f4d\u7f6e\n\n        :param space:\n        :return:\n        '
        points = MPointArray()
        self.fn.getCVs(points, space)
        return NewDouble3s(points)

    def numCvs(self):
        u'\n        \u8fd4\u56de\u6b64\u66f2\u7ebf\u7684CV\u6570\n\n        :return:\n        '
        return self.fn.numCVs()

    def numSpans(self):
        u'\n        \u8fd4\u56de\u6b64\u66f2\u7ebf\u7684\u8de8\u5ea6\u6570\n\n        :return:\n        '
        return self.fn.numSpans()

    def numKnots(self):
        u'\n        \u8fd4\u56de\u6b64\u66f2\u7ebf\u7684\u7ed3\u6570\n\n        :return:\n        '
        return self.fn.numKnots()

    def degree(self):
        u'\n        \u8fd4\u56de\u6b64\u66f2\u7ebf\u7684\u5ea6\u6570\n\n        :return:\n        '
        return self.fn.degree()

    def getPointAtParam(self, u, space=basedata.Space.object):
        u'\n        \u8fd4\u56de\u66f2\u7ebf\u4e0a\u7ed9\u5b9a\u53c2\u6570\u503c\u5904\u7684\u7a7a\u95f4\u70b9\n\n        :param u:\n        :param space:\n        :return:\n        '
        point = MPoint()
        self.fn.getPointAtParam(u, point, space)
        return basedata.Double3(point)

    def findLengthFromParam(self, u):
        u'\n        \u8fd4\u56de\u4e0e\u66f2\u7ebf\u4e0a\u7ed9\u5b9a\u53c2\u6570\u503c\u76f8\u5bf9\u5e94\u7684\u6cbf\u66f2\u7ebf\u7684\u957f\u5ea6\n\n        :param u:\n        :return:\n        '
        return self.fn.findLengthFromParam(u)

    def findParamFromLength(self, u):
        u'\n        \u8fd4\u56de\u4e0e\u66f2\u7ebf\u4e0a\u7ed9\u5b9a\u6cbf\u66f2\u7ebf\u7684\u957f\u5ea6\u76f8\u5bf9\u5e94\u7684\u53c2\u6570\u503c\n\n        :param u:\n        :return:\n        '
        return self.fn.findParamFromLength(u)

    def closestPoint(self, point=basedata.Double3, space=basedata.Space.object, tolerance=1e-05):
        u'\n        \u6b64\u65b9\u6cd5\u786e\u5b9a\u66f2\u7ebf\u4e0a\u6700\u63a5\u8fd1\u7ed9\u5b9a\u70b9\u7684\u70b9\u3002\n\n        :param point: \u6d4b\u8bd5\u70b9\n        :param space: \u6307\u5b9a\u6b64\u64cd\u4f5c\u7684\u5750\u6807\u7cfb\n        :param tolerance: \u8ba1\u7b97\u4e2d\u5141\u8bb8\u7684\u8bef\u5dee\u91cf\uff08\u03b5\u503c\uff09\n        :return:\n        '
        if isinstance(point, MPoint):
            point = MPoint(point[0], point[1], point[2])
        u = ScriptUtil.asIntPtr()
        point = self.fn.closestPoint(point, u, tolerance, space)
        return (basedata.Double3(point), ScriptUtil.getInt(u))

class SurfaceCv(Components2Base, ):
    components_type_str = 'cv'
    __metaclass__ = componentsTypesMetadef

    @Components2Base.IsSingleComponent
    def setPoint(self, point=basedata.Double3, space=basedata.Space.object):
        return self.node.setPoint(self.indexu, self.indexv, point, space)

    @Components2Base.IsSingleComponent
    def getPoint(self, space=basedata.Space.object):
        return self.node.getPoint(self.indexu, self.indexv, space)

class Surface(DagNode, ):
    __metaclass__ = ObjectMetadef(MFn.kNurbsSurface)

    def __init__(self, *args):
        super(Surface, self).__init__(*args)
        self.cv = SurfaceCv(self)
        self.cv.cp__init_componenrs()

    @staticmethod
    def isCurrentNodeType(path=MDagPath):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param path: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        '
        return path.hasFn(MFn.kNurbsSurface)

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n        :return: MFn\n        '
        path = MDagPath()
        MDagPath.getAPathTo(self.obj, path)
        return MFnNurbsSurface(path)

    def setPoint(self, indexU=0, indexV=0, point=basedata.Double3, space=basedata.Space.object):
        u'\n        \u8bbe\u7f6eCV\u70b9\u4f4d\u7f6e\n\n        :param indexU:\n        :param indexV:\n        :param point:\n        :param space:\n        :return:\n        '
        if (not isinstance(point, MPoint)):
            point = MPoint(point[0], point[1], point[2])
        unpoint = MPoint()
        self.fn.getCV(indexU, indexV, unpoint, space)

        def doIt():
            fn = self.functionSet()
            fn.setCV(indexU, indexV, point, space)
            fn.updateSurface()

        def undoIt():
            fn = self.functionSet()
            fn.setCV(indexU, indexV, unpoint, space)
            fn.updateSurface()
        return cmcore.addCommand(doIt, undoIt)

    def getPoint(self, indexU=0, indexV=0, space=basedata.Space.object):
        u'\n        \u83b7\u5f97CV\u70b9\u4f4d\u7f6e\n\n        :param indexU:\n        :param indexV:\n        :param space:\n        :return:\n        '
        point = MPoint()
        self.fn.getCV(indexU, indexV, point, space)
        return basedata.Double3(point)

    def numSpansInU(self):
        u'\n        \u8fd4\u56deu\u65b9\u5411\u4e0a\u7684\u8de8\u5ea6\u6570\n\n        :return:\n        '
        return self.fn.numSpansInU()

    def numSpansInV(self):
        u'\n        \u8fd4\u56dev\u65b9\u5411\u4e0a\u7684\u8de8\u5ea6\u6570\n\n        :return:\n        '
        return self.fn.numSpansInV()

    def numCVsInU(self):
        u'\n        \u8fd4\u56deU\u65b9\u5411\u4e0a\u7684CV\u6570\u91cf\uff08\u5ea6+\u8de8\u5ea6\uff09\n\n        :return:\n        '
        return self.fn.numCVsInU()

    def numCVsInV(self):
        u'\n        \u8fd4\u56deV\u65b9\u5411\u4e0a\u7684CV\u6570\u91cf\uff08\u5ea6+\u8de8\u5ea6\uff09\n\n        :return:\n        '
        return self.fn.numCVsInV()

class WeightGeometryFilter(DgNode, ):
    __metaclass__ = ObjectMetadef(MFn.kWeightGeometryFilt)

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n        :return: MFn\n        '
        return MFnWeightGeometryFilter(self.obj)

    def getWeights(self, geo):
        u'\n        \u83b7\u5f97\u53d8\u5f62\u5668\u6743\u91cd\n\n        :param geo: \u7ec4\u4ef6 \u4f8b:xxx.vtx\n        :return:\n        '
        geo = str(geo)
        if (geo.find('.') < 0):
            raise cmcore.CPMelError(u'\u9700\u8981\u7ec4\u4ef6')
        sel_list = MSelectionList()
        try:
            sel_list.add(str(geo))
        except RuntimeError:
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        if (int(sel_list.length()) > 1):
            raise cmcore.CPMelError(u'\u4e0d\u5728\u4e00\u4e2amesh\u6216\u8005\u5176\u4ed6\u5bf9\u8c61\u4e0a')
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        weights = MFloatArray()
        self.fn.getWeights(path, comp, weights)
        return FloatArray(weights)

    def setWeights(self, geo, weights):
        u'\n        \u8bbe\u7f6e\u53d8\u5f62\u5668\u6743\u91cd\n\n        :param geo: \u7ec4\u4ef6 \u4f8b:xxx.vtx\n        :param weights: \u6743\u91cd\u5217\u8868\n        :return:\n        '
        geo = str(geo)
        if (geo.find('.') < 0):
            raise cmcore.CPMelError(u'\u9700\u8981\u7ec4\u4ef6')
        sel_list = MSelectionList()
        try:
            sel_list.add(str(geo))
        except RuntimeError:
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        if (int(sel_list.length()) > 1):
            raise cmcore.CPMelError(u'\u4e0d\u5728\u4e00\u4e2amesh\u6216\u8005\u5176\u4ed6\u5bf9\u8c61\u4e0a')
        try:
            weights = FloatArray(weights)
        except TypeError:
            raise cmcore.CPMelError(u'weight \u4e0d\u662f\u6d6e\u70b9\u6570\u7ec4')
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        m_weights = MFloatArray()
        un_weights = MFloatArray()
        tuple((m_weights.append(i) for i in weights))
        self.fn.getWeights(path, comp, un_weights)

        def doIt():
            self.functionSet().setWeight(path, comp, m_weights)

        def undoIt():
            self.functionSet().setWeight(path, comp, un_weights)
        cmcore.addCommand(doIt, undoIt)

class SkinCluster(WeightGeometryFilter, ):
    __metaclass__ = ObjectMetadef(MFn.kSkinClusterFilter)

    def cp__getFnClass(self):
        u'\n        \u83b7\u5f97\u5f53\u524d\u51fd\u6570\u96c6\n        :return: MFn\n        '
        return MFnSkinCluster(self.obj)

    @staticmethod
    def isCurrentNodeType(obj=MObject):
        u'\n        \u8fd4\u56de\u8282\u70b9\u8fd9\u4e2a\u7c7b\u662f\u5426\u652f\u6301\u8fd9\u4e2a\u8282\u70b9\n\n        :param obj: api1.0 MObject \u6307\u5411\u4e00\u4e2a\u8282\u70b9\u7684MObject\n        :return: bool\n        '
        return obj.hasFn(MFn.kSkinClusterFilter)

    def getPaint(self):
        u'\n        \u7ed8\u5236\u6743\u91cd\n\n        :param weights:\n        :return:\n        '
        return cmds.getAttr((str(self) + '.paintWeights'))

    def setPaint(self, weights):
        u'\n        \u7ed8\u5236\u6743\u91cd\n\n        :param weights:\n        :return:\n        '
        return cmds.setAttr((str(self) + '.paintWeights'), weights, type='doubleArray')
    paint = property(getPaint, setPaint)

    def rePaint(self):
        u'\n        \u91cd\u7ed8\u5236\u6743\u91cd\n\n        :return:\n        '
        ctx = cmds.currentCtx()
        if (ctx == 'artAttrSkinContext'):
            mel.eval((u'setSmoothSkinInfluence("%s")' % cmds.artAttrSkinPaintCtx(ctx, q=True, inf=True)))

    def getWeights(self, geo, inf):
        u'\n        \u83b7\u5f97\u9aa8\u9abc\u8499\u76ae\u6743\u91cd\n\n        :param geo: \u7ec4\u4ef6 \u4f8b:xxx.vtx\n        :param inf: \u5173\u8282\u7d22\u5f15\n        :return:\n        :rtype:list\n        '
        geo = str(geo)
        if (geo.find('.') < 0):
            raise cmcore.CPMelError(u'\u9700\u8981\u7ec4\u4ef6')
        try:
            inf = basedata.IntArray(inf)
        except TypeError:
            raise cmcore.CPMelError(u'inf \u4e0d\u662f\u6574\u5f62\u6570\u7ec4')
        sel_list = MSelectionList()
        try:
            sel_list.add(str(geo))
        except RuntimeError:
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        if (int(sel_list.length()) > 1):
            raise cmcore.CPMelError(u'\u4e0d\u5728\u4e00\u4e2amesh\u6216\u8005\u5176\u4ed6\u5bf9\u8c61\u4e0a')
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        m_inf = MIntArray()
        ScriptUtil.createIntArrayFromList(inf, m_inf)
        m_weigth = MDoubleArray()
        self.fn.getWeights(path, comp, m_inf, m_weigth)
        return FloatArray(m_weigth)

    def setWeights(self, geo, inf, weigths):
        u'\n        \u83b7\u5f97\u9aa8\u9abc\u8499\u76ae\u6743\u91cd\n\n        :param geo: \u7ec4\u4ef6 \u4f8b:xxx.vtx\n        :param inf: \u5173\u8282\u7d22\u5f15\n        :param weigths: \u6743\u91cd\u6570\u7ec4\n        :return:\n        '
        geo = str(geo)
        if (geo.find('.') < 0):
            raise cmcore.CPMelError(u'\u9700\u8981\u7ec4\u4ef6')
        try:
            inf = FloatArray(inf)
        except TypeError:
            raise cmcore.CPMelError(u'inf \u4e0d\u662f\u6574\u5f62\u6570\u7ec4')
        try:
            weigths = FloatArray(weigths)
        except TypeError:
            raise cmcore.CPMelError(u'weight \u4e0d\u662f\u6d6e\u70b9\u6570\u7ec4')
        sel_list = MSelectionList()
        try:
            sel_list.add(geo)
        except RuntimeError:
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        if (int(sel_list.length()) > 1):
            raise cmcore.CPMelError(u'\u4e0d\u5728\u4e00\u4e2amesh\u6216\u8005\u5176\u4ed6\u5bf9\u8c61\u4e0a')
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        m_inf = MIntArray()
        ScriptUtil.createIntArrayFromList(inf, m_inf)
        m_weigth = MDoubleArray()
        tuple((m_weigth.append(i) for i in weigths))
        un_weights = MDoubleArray()
        un_inf = MIntArray()
        test_dag_array = MDagPathArray()
        self.fn.influenceObjects(test_dag_array)
        tuple((un_inf.append(i) for i in xrange(len(test_dag_array))))
        self.fn.setWeights(path, comp, m_inf, m_weigth, True, un_weights)

        def doIt():
            self.functionSet().setWeights(path, comp, m_inf, m_weigth)

        def undoIt():
            self.functionSet().setWeights(path, comp, un_inf, un_weights)
        cmcore.defAddCommandList(doIt, undoIt)
        return

    def getBlendWeights(self, geo):
        u'\n        \u83b7\u5f97\u6743\u91cd\u5df2\u6df7\u5408\u6743\u91cd\n\n        :param geo: \u7ec4\u4ef6\n        :return:\n        :rtype:list\n        '
        geo = str(geo)
        if (geo.find('.') < 0):
            raise cmcore.CPMelError(u'\u9700\u8981\u7ec4\u4ef6')
        sel_list = MSelectionList()
        try:
            sel_list.add(geo)
        except RuntimeError:
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        if (int(sel_list.length()) > 1):
            raise cmcore.CPMelError(u'\u4e0d\u5728\u4e00\u4e2amesh\u6216\u8005\u5176\u4ed6\u5bf9\u8c61\u4e0a')
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        un_weight = MDoubleArray()
        self.fn.getBlendWeights(path, comp, un_weight)
        return FloatArray(un_weight)

    def setBlendWeights(self, geo, weigth):
        u'\n        \u8bbe\u7f6e\u6743\u91cd\u5df2\u6df7\u5408\u6743\u91cd\n\n        :param geo: \u7ec4\u4ef6\n        :param weigth: \u6743\u91cd\u6570\u7ec4\n        :return:\n        '
        geo = str(geo)
        if (geo.find('.') < 0):
            raise cmcore.CPMelError(u'\u9700\u8981\u7ec4\u4ef6')
        try:
            weigth = array.array('f', weigth)
        except TypeError:
            raise cmcore.CPMelError(u'weight \u4e0d\u662f\u6d6e\u70b9\u6570\u7ec4')
        sel_list = MSelectionList()
        try:
            sel_list.add(geo)
        except RuntimeError:
            raise cmcore.CPMelError(u'\u5bf9\u8c61\u4e0d\u5b58\u5728')
        if (int(sel_list.length()) > 1):
            raise cmcore.CPMelError(u'\u4e0d\u5728\u4e00\u4e2amesh\u6216\u8005\u5176\u4ed6\u5bf9\u8c61\u4e0a')
        path = MDagPath()
        comp = MObject()
        sel_list.getDagPath(0, path, comp)
        m_weigth = MDoubleArray()
        tuple((m_weigth.append(i) for i in weigth))
        un_weight = MDoubleArray()
        self.fn.getBlendWeights(path, comp, un_weight)
        self.fn.setBlendWeights(path, comp, m_weigth)

        def doIt():
            self.functionSet().setBlendWeights(path, comp, m_weigth)

        def undoIt():
            self.functionSet().setBlendWeights(path, comp, un_weight)
        cmcore.defAddCommandList(doIt, undoIt)
        return
