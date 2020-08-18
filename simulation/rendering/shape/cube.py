from simulation.rendering.shape import plane, composite_shape
import numpy as np

class Cube(composite_shape.CompositeShape):
    def __init__(self, length, width, height, lengthwise_resolution, widthwise_resolution, height_resolution, colour=(255, 255, 255), transform=np.identity(4, dtype=float), pos=None):

        bottom = plane.Plane(1, 1, lengthwise_resolution, widthwise_resolution)

        bottom.rotate_z(np.radians(180))

        bottom.translate_x(1)

        top = plane.Plane(1, 1, lengthwise_resolution, widthwise_resolution)

        top.translate_y(1)

        
        super().__init__(shapes, colour, transform, pos)