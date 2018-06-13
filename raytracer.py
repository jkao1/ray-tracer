import numpy as np

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
        m = np.sqrt( self.dot(self) )
        return self * 1.0 / m


