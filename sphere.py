import numpy as np

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

    def __mul__(self, s):
        return Vector(
            self.x * s,
            self.y * s,
            self.z * s,
        )

    def __abs__(self):
        return self.dot(self)

    def dot(self, u):
        return self.x * u.x + self.y * u.y + self.z * u.z

    def double(self):
        return Vector(self.x*2, self.y*2, self.z*2)

    def normal(self):
        return self * (1.0 / abs(self))

    def cond_get(self, cond):
        return Vector(
            cond_get(cond, self.x),
            cond_get(cond, self.y),
            cond_get(cond, self.z),
        )


class Sphere():
    def __init__(self, center, radius, diffuse_reflection):
        self.c = center
        self.r = radius
        self.d = diffuse_reflection

    def touches(self, origin, norm):
        Rm = norm.dot(origin - self.c) * 2.0
        rsquared = self.r ** 2
        reduced = abs(self.c)
        dotted = self.c.dot(origin) * 2.0
        origin = abs(origin)
        hyp = reduced + origin - dotted - rsquared

        circle_probably = Rm ** 2 - 4 * hyp
        selected = np.sqrt( np.maximum(0, circle_probably) )

        # THANK YOU NICK CHEN
        alpha = (-Rm - selected) / 2
        beta = (-Rm + selected) / 2

        # THANK YOU STACK OVERFLOW
        head = np.where( (alpha > 0) & (alpha < beta), alpha, beta)
        h = (circle_probably > 0) & (head > 0)

        return np.where(h, head, 1e10)

    def color(self, objects, origin, norm, distance, i,  light, eye):
        intersection = origin + norm * distance
        translated = (intersection - self.c)
        inverse = translated * (1.0 / self.r)

        reflected = (light - intersection).normal()
        backwards_trace = (eye - intersection).normal()

        all_distances = [
            obj.touches(translated, reflected) for obj in objects
        ]
        closest_distances = reduce( np.minimum, all_distances )
        visible_ones = all_distances[i] == closest_distances

        ambient = Vector(50.0 / 255, 50.0 / 255, 50.0 / 255)
        lambert = np.maximum( translated.dot(reflected), 0.0 )
        diffused = self.d * lambert * visible_ones

        # phong reflection model
        fi = translated.double()
        reflection = (norm - fi * norm.dot(translated)).normal()
        # phong shading model
        shading = translated.dot( (reflected + backwards_trace).normal() )
        specular = Vector(1.0, 1.0, 1.0)
        specular *= np.power( np.clip(shading, 0.0, 1.0), 50.0)
        specular *= visible_ones

        return ambient + diffused + reflection + specular

