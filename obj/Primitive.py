from geom import T3D
from surf import Surface

class Primitive(object):

    def __init__(self, id, surface):
        self.id = id
        self.surface = surface

    def getId(self):
        return self.id

    def getSurface(self):
        return self.surface

    # def intersect(self, pos, ray):

    # def normal(self, pos):

