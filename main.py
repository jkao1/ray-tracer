from vector import Vector
from sphere import Sphere
import numpy as np

WIDTH = 500
HEIGHT = 500

def cond_get(cond, x):
    if isinstance(x, int):
        return x
    else:
        return np.extract(cond, x)


light = Vector(100, 100, -100)
eye = Vector(0, 0, -1)

def trace(objects, origin, normal):
    color = [ 0, 0, 0 ]
    object_distances = [ o.touches(origin, normal) for o in objects ]
    closest_object = reduce( np.minimum, distances )

    frumpy = []
    for i in range( len(objects) ):
        frumpy.append(
            (i, objects[i], object_distances[i])
        )
    for (i, o, d) in frumpy:
        intersected = closest_object == d
        if np.any(intersected):
            color += s.color(
                objects,
                origin.cond_get(intersected),
                normal.cond_get(intersected),
                cond_get(intersected, d),
                i,
            )
    return color


all_objects = [
    Sphere( Vector(0, 0, 0), 1, Vector(1, 0, 0) ),
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
print normalized, type(normalized)

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
    ) for x in colors
]

Image.merge(rgb).save('pleasework.png')

