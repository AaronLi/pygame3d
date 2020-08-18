from simulation.rendering.shape import composite_shape, disc, cylinder
import numpy as np

class CappedCylinder(composite_shape.CompositeShape):
    def __init__(self, radius, height, radial_resolution, lateral_resolution, colour=(255, 255, 255), transform=np.identity(4, dtype=float), pos=None, bottom_cap = True, top_cap = True):

        cyl = cylinder.Cylinder(radius, height, colour, faces=radial_resolution)

        shapes = [cyl]

        if bottom_cap:
            cap_1 = disc.Disc(radius, radial_resolution, lateral_resolution, colour)

            cap_1.rotate_z(np.radians(180))

            shapes.append(cap_1)

        if top_cap:

            cap_2 = disc.Disc(radius, radial_resolution, lateral_resolution, colour)

            cap_2.translate_y(height)

            shapes.append(cap_2)

        super().__init__(shapes, colour, transform, pos)
