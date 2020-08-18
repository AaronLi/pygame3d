from simulation.rendering.shape import generic
import numpy as np


class Plane(generic.GenericShape):
    def __init__(self, length, width, lengthwise_resolution, widthwise_resolution, colour=(255, 255, 255),
                 transform=np.identity(4, dtype=float), pos=None):
        super().__init__(colour, transform, pos)

        self.scale_x(length)
        self.scale_z(width)

        self.faces = np.ndarray((widthwise_resolution * lengthwise_resolution, 4, 4), dtype=float)

        for x in range(lengthwise_resolution):
            for z in range(widthwise_resolution):
                face = self.faces[x * lengthwise_resolution + z]
                face[0] = (x / lengthwise_resolution, 0, z / widthwise_resolution),
                face[1] = ((x + 1) / lengthwise_resolution, 0, z / widthwise_resolution),
                face[2] = ((x + 1) / lengthwise_resolution, 0, (z + 1) / widthwise_resolution),
                face[3] = (x / lengthwise_resolution, 0, (z + 1) / widthwise_resolution)
