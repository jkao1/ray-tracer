from sphere import Vector, Sphere, Chess
from PIL import Image
import numpy as np

WIDTH = 500
HEIGHT = 500
light = Vector(100, 100, -100)

def cond_get(cond, x):
    if isinstance(x, int):
        return x
    else:
        return np.extract(cond, x)


eye = Vector(0, 0, -1)

def trace(objects, origin, normal, reflect_index=0):
    color = Vector(0, 0, 0)
    object_distances = [ o.touches(origin, normal) for o in objects ]
    closest_object = reduce( np.minimum, object_distances )

    frumpy = []
    for i in range( len(objects) ):
        frumpy.append(
            (i, objects[i], object_distances[i])
        )
    for (i, o, d) in frumpy:
        intersected = closest_object == d
        if np.any(intersected):
            individual_color = o.color(
                objects,
                origin.cond_get(intersected),
                normal.cond_get(intersected),
                cond_get(intersected, d),
                i,
                reflect_index
            )
            color += individual_color.project(intersected)
    return color



all_objects = [
    Sphere(Vector(.75, 1., 1.), .6, Vector(0, 0, 1)),
    Sphere(Vector(-.5, .1, .5), .2, Vector(1, 0, 0)),
    Sphere(Vector(.5, .1, 1.5), .4, Vector(1, 0, 0)),
    Sphere(Vector(0, .1, 5), .4, Vector(1, 1, 0)),
    Chess(Vector(0,-20.5, 0), 20, Vector(0, 0, 1))
]

# Mad quick code stolen from https://www.geeksforgeeks.org/numpy-tile-python/
all_x = np.tile( np.linspace( -1.0, 1.0, WIDTH), HEIGHT )

all_y = np.repeat(
    np.linspace(
        1.0 * HEIGHT / WIDTH,
        -1.0 * HEIGHT / WIDTH,
        HEIGHT,
    ), WIDTH )

tracer = Vector(all_x, all_y, 0.0)
normalized = (tracer - eye).normal()

total_color = trace(
    all_objects,
    eye,
    normalized,
)


# This may be my 10th "Thanks stackoverflow"
screen = [
    Image.fromarray(
        (255 * np.clip( x, 0, 1 ).reshape(( HEIGHT, WIDTH))).astype(np.uint8),
        'L',
    ) for x in [total_color.x, total_color.y, total_color.z]
]


Image.merge('RGB', screen).save('pleasework.png')

