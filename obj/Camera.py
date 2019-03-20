from geom import T3D

class Camera(object):    
    
    def __init__(self, eyePoint, lookPoint, up, hFOV, vFOV):
        self.lookFrom = eyePoint
        self.lookTo = lookPoint
        self.up = up
        self.hFOV = hFOV
        self.vFOV = vFOV

    def getLookFrom(self):
        return self.lookFrom

    def getLookTo(self):
        return self.lookTo

    def getUp(self):
        return self.up
    
    def gethFOV(self):
        return self.hFOV

    def getvFOV(self):
        return self.vFOV

    def toString(self):
        return("look from: " + self.lookFrom +
                ", look to: " + self.lookTo + ", up: " + self.up +
                ", FOV: <" + self.hFOV + ", " + self.vFOV + ">")
    

