import numpy as np

class Sphere():
    def __init__(self, center, radius, diffuse_reflection):
        self.c = center
        self.r = radius
        self.d = diffuse_reflection

    def touches(self, origin, norm):
        Rm = 2.0 * norm.dot(origin - self.c)
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

        return np.where(h, head, 1e10)

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
