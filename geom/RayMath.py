from math import sqrt
from .T3D import T3D

class RayMath:
    def normalize(self, r: T3D):
        d = sqrt(r.x * r.x + r.y * r.y + r.z * r.z)
        r.x /= d
        r.y /= d
        r.z /= d
        return d

    def dotp(self, r, s):
        return (r.x * s.x) + (r.y * s.y) + (r.z * s.z)

    def crossp(self, t, r, s):
        t.x = (r.y * s.z) - (r.z * s.y)
        t.y = (r.z * s.x) - (r.x * s.z)
        t.z = (r.x * s.y) - (r.y * s.x)
        d = sqrt((t.x * t.x) + (t.y * t.y) + (t.z * t.z))
        t.x /= d
        t.y /= d
        t.z /= d
        return d