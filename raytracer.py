import numpy as np

WIDTH = 500
HEIGHT = 500

def cond_get(cond, x):
    if isinstance(x, int):
        return x
    else:
        return np.extract(cond, x)

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, v):
        return Vector(
            self.x + v.x,
            self.y + v.y,
            self.z + v.z,
        )

    def __sub__(self, v):
        return Vector(
            self.x - v.x,
            self.y - v.y,
            self.z - v.z,
        )

    def __mul__(self, v):
        return Vector(
            self.x * v.x,
            self.y * v.y,
            self.z * v.z,
        )

    def dot(self, u):
        return self.x * u.x + self.y * u.y + self.z * u.z

    def norm(self):
        return np.sqrt( self.dot(self) )

    def normal(self):
        return self / self.norm()

    def cond_get(self, cond):
        return Vector(
            cond_get(cond, self.x),
            cond_get(cond, self.y),
            cond_get(cond, self.z),
        )

light = Vector(100, 100, -100)
eye = Vector(0, 0, -1)


def raytrace(objects, origin, normal):
    color = [ 0, 0, 0 ]
    object_distances = [ o.intersect(origin, normal) for o in objects ]
    closest_object = reduce( np.minimum, distances )

    frumpy = []
    for i in range( len(objects) ):
        frumpy.append(
            (objects[i], object_distances[i])
        )
    for (o, d) in frumpy:
        intersected = closest_object === d
        if np.any(intersected):
            color += s.light(
                origin.cond_get(intersected),
                normal.cond_get(intersected),
                cond_get(intersected, d),
            )
    return color
