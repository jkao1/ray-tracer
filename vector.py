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

    def normal(self):
        return self * (1.0 / abs(self))

    def cond_get(self, cond):
        return Vector(
            cond_get(cond, self.x),
            cond_get(cond, self.y),
            cond_get(cond, self.z),
        )
