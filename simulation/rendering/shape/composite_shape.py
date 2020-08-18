from simulation.rendering.shape import generic
import numpy as np

class CompositeShape(generic.GenericShape):
    def __init__(self, shapes, colour=(255, 255, 255), transform=np.identity(4, dtype=float), pos=None):
        super().__init__(colour, transform, pos)

        self.faces = np.vstack([shape.get_world_faces() for shape in shapes])