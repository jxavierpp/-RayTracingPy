from geom.T3D import *
from surf import Surface
from math import sqrt
from obj import Primitive

class Sphere(Primitive):
    center: T3D

    def __init__(self,id, center: T3D, radius, surface):
        super()
        self.id = id
        self.surface = surface
        self.center = center
        self.radius = radius

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def intersect(self, pos: T3D, ray):
        # translate ray origin to object's space
        xadj = pos.x - self.center[0]
        yadj = pos.y - self.center[1]
        zadj = pos.z - self.center[2]

        # solve quadratic equation
        b = xadj * ray.x + yadj * ray.y + zadj * ray.z
        t = b * b - xadj * xadj - yadj * yadj - zadj * zadj + self.radius * self.radius
        if (t < 0): 
            return 0

        s = -b - sqrt(t)  # try smaller solution
        if (s > 0):
            return s
        

        s = -b + sqrt(t)  # try larger solution
        if (s > 0):
            return s

        return 0  # both solutions <= 0

    def normal(self, pos: T3D):
        nrm = T3D()
        nrm.x = (pos.x - self.center[0]) / self.radius
        nrm.y = (pos.y - self.center[1]) / self.radius
        nrm.z = (pos.z - self.center[2]) / self.radius
        return nrm
    
    def toString(self):
        return "center: " + self.center + ", radius: " + self.radius
    

