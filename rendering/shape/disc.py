import numpy as np
from rendering.shape import generic

class Disc(generic.GenericShape):
    def __init__(self, radius, radial_resolution, lateral_resolution, colour=(255, 255, 255), transform=np.identity(4, dtype=float), pos=None):
        super().__init__(colour, transform, pos)

        self.scale_x(radius)
        self.scale_z(radius)

        self.faces = np.ndarray((radial_resolution * lateral_resolution, 4, 4), dtype=float)

        angle_per_slice = 2 * np.pi / radial_resolution

        for i in range(radial_resolution):
            for j in range(lateral_resolution):
                face = self.faces[i*lateral_resolution+j]
                face[0] = ((j / lateral_resolution) * np.sin(i * angle_per_slice), 0, (j / lateral_resolution) * np.cos(i * angle_per_slice), 1)
                face[1] = (((j + 1) / lateral_resolution) * np.sin(i * angle_per_slice), 0, ((j + 1) / lateral_resolution) * np.cos(i * angle_per_slice), 1)
                face[2] = (((j+1) / lateral_resolution) * np.sin((i+1) * angle_per_slice), 0, ((j+1) / lateral_resolution) * np.cos((i+1) * angle_per_slice), 1)
                face[3] = ((j / lateral_resolution) * np.sin((i + 1) * angle_per_slice), 0, (j / lateral_resolution) * np.cos((i + 1) * angle_per_slice), 1)