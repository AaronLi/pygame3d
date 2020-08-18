from simulation.rendering.shape.generic import GenericShape
import numpy as np


class Sphere(GenericShape):
    def __init__(self, radius, colour=(255, 255, 255), vertical_faces=5, horizontal_faces=10, transform=np.identity(4, dtype=float), pos = None):
        super().__init__(colour=colour, transform = transform, pos= pos)

        self.scale_x(radius)
        self.scale_y(radius)
        self.scale_z(radius)

        horizontal_radians_per_face = 2 * np.pi / horizontal_faces
        vertical_radians_per_face = np.pi / vertical_faces

        self.faces = np.ndarray((horizontal_faces * vertical_faces, 4, 4), dtype=float)

        for i in range(horizontal_faces):
            for j in range(vertical_faces):
                face = self.faces[i*vertical_faces+j]
                # create a 4 point polygon for each face of the cylinder (no end caps)
                face[0] = (np.cos(j * vertical_radians_per_face) * np.sin(i * horizontal_radians_per_face),
                           np.sin(j * vertical_radians_per_face) * np.sin(i * horizontal_radians_per_face),
                           np.cos(i * horizontal_radians_per_face),
                           1)
                face[1] = (np.cos(j * vertical_radians_per_face) * np.sin((i+1) * horizontal_radians_per_face),
                           np.sin(j * vertical_radians_per_face) * np.sin((i+1) * horizontal_radians_per_face),
                           np.cos((i+1) * horizontal_radians_per_face),
                           1)
                face[2] = (np.cos((j+1) * vertical_radians_per_face) * np.sin((i+1) * horizontal_radians_per_face),
                           np.sin((j+1) * vertical_radians_per_face) * np.sin((i+1) * horizontal_radians_per_face),
                           np.cos((i+1) * horizontal_radians_per_face),
                           1)
                face[3] = (np.cos((j+1) * vertical_radians_per_face) * np.sin(i * horizontal_radians_per_face),
                           np.sin((j+1) * vertical_radians_per_face) * np.sin(i * horizontal_radians_per_face),
                           np.cos(i * horizontal_radians_per_face),
                           1)
        print(self.faces)