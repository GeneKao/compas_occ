from compas.geometry import Point
from compas.geometry import Polyline
from compas_occ.geometry import OCCNurbsCurve
from compas_view2.app import App


points0 = [Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)]
curve0 = OCCNurbsCurve.from_points(points0)

points1 = [Point(6, -3, 0), Point(3, 1, 0), Point(6, 6, 3), Point(3, 12, 0)]
curve1 = OCCNurbsCurve.from_points(points1)

parameters, distance = curve0.closest_parameters_curve(curve1, return_distance=True)

points = curve0.closest_points_curve(curve1, return_distance=False)

# ==============================================================================
# Visualisation
# ==============================================================================

view = App()

view.add(Polyline(curve0.locus()), linewidth=3)
view.add(Polyline(curve1.locus()), linewidth=3)

view.add(points[0], pointcolor=(1, 0, 0))
view.add(points[1], pointcolor=(1, 0, 0))

view.run()
