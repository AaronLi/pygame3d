from pygame import *
from simulation.rendering import camera, shape, light_source
import numpy as np

screen = display.set_mode((800, 600))

c = camera.Camera(800, 600, 90)

clockity = time.Clock()

cyl = shape.cylinder.Cylinder(10, 5, faces=50, pos=np.array((20, -2.5, 0, 1)))

disc = shape.disc.Disc(10, 35, 20)

capped_cyl = shape.capped_cylinder.CappedCylinder(4, 15, 15, 3)

capped_cyl.translate_z(-20)
capped_cyl.rotate_z(np.radians(45))
capped_cyl.translate_x(30)

disc.rotate_z(np.radians(90))
disc.translate_z(30)
disc.translate_x(30)

sphere = shape.sphere.Sphere(2)

sphere.translate_z(-30)
#sphere.translate_y(2)
sphere.translate_x(1)


#cyl.rotate_x(np.radians(90))
#cyl.translate_x(20)

running = True

l = light_source.LightSource(np.array((5, 5, 5, 1)))

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    cyl.rotate_y(np.radians(10) * clockity.get_time()/1000)
    disc.rotate_x(np.radians(10) * clockity.get_time()/1000)
    capped_cyl.rotate_z(np.radians(10) * clockity.get_time()/1000)
    sphere.rotate_z(np.radians(10)*clockity.get_time()/1000)

    pols = c.render_shapes([capped_cyl], l)
    pols.sort(key=lambda x: sum(x.face[:, 0])/4)
    screen.fill((70, 80, 90))
    for pol in pols:

        draw.polygon(screen, pol.colour, pol.face[:, 1:3])

    display.flip()

    clockity.tick(144)

    display.set_caption(f'FPS: {clockity.get_fps():5.2f} Faces: {len(pols):03d}')

quit()