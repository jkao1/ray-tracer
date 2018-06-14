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

class Sphere():
    def __init__(self, center, radius, diffuse_reflection):
        self.c = center
        self.r = radius
        self.d = diffuse

    def touches(self, origin, norm):
        Rm = 2 * norm.dot(origin - self.c)
        rsquared = self.r ** 2
        reduced = abs(self.c)
        dotted = self.c.dot(origin)
        origin = abs(origin)
        hyp = reduced + origin - 2 * dotted - rsquared

        circle_probably = Rm ** 2 - 4 * hyp
        selected = np.sqrt( np.maximum(o, circle_probably) )

        # THANK YOU NICK CHEN
        alpha = (-Rm - selected) / 2
        beta = (-Rm + selected) / 2

        # THANK YOU STACK OVERFLOW
        head = np.where( (alpha > 0) & (alpha < beta), alpha, beta)
        h = (circle_probably > 0) & (head > 0)

        return np.where(h, head, 10000000000000000000000000000000000000)

    def color(self, objects, origin, norm, distance, i):
        intersection = origin + normal * distance
        translated = (intersection - sefl.c)
        inverse = translated * 1.0 / self.r

        reflected = (light - intersection).normal()
        backwards_trace = (eye - intersection).normal()

        all_distances = [
            obj.touches(translation, reflected) for obj in objects
        ]
        closest_distances = reduce( np.minimum, all_distances )
        visible_ones = all_distances[i] == closest_distances

        ambient = [50.0 / 255, 50.0 / 255, 50.0 / 255]
        lambert = np.maximum( translated.dot(reflected), 0.0 )

        # phong reflection model
        reflection = (norm - 2 * translated * norm.dot(translated)).norm()
        # phong shading model
        shading = translated.dot( (reflected + backwards_trace).norm() )

        return ambient + diffuse*visible_light*lambert + reflection + shading


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
        intersected = closest_object === d
        if np.any(intersected):
            color += s.color(
                objects,
                origin.cond_get(intersected),
                normal.cond_get(intersected),
                cond_get(intersected, d),
                i,
            )
    return color


