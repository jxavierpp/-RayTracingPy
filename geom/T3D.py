from math import sqrt

class T3D(object):
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self, p):
        tx = self.x - p.x
        ty = self.y - p.y
        tz = self.z - p.z
        return sqrt(tx * tx + ty * ty + tz * tz)
    
    def toString(self):
        return "x: " + self.x + ", y: " + self.y + ", z: " + self.z
    
    def getRGB(self):
        return tuple([self.x,self.y,self.z])

