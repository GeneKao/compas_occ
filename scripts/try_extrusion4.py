from compas.geometry import Vector
from compas.geometry import Circle
from compas.geometry import Plane
from compas.geometry import NurbsCurve
from compas_occ.geometry import OCCNurbsSurface
from compas_view2.app import App

curve = NurbsCurve.from_circle(Circle(Plane.worldXY(), 3.0))

surface = OCCNurbsSurface.from_extrusion(curve, Vector(0, 0, 10))

viewer = App()
viewer.view.camera.position = [-5, -10, 7]
viewer.view.camera.target = [0, 0, 5]

viewer.add(curve.to_polyline(), linewidth=5, color=(1, 0, 0))
viewer.add(surface.to_mesh())
viewer.show()
