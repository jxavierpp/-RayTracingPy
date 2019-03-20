from geom import T3D

class Light(object):

    def __init__(self, position, color, brightness):
        self.position = position
        self.color = color
        self.brightness = brightness

    def getPosition(self):
        return self.position

    def getColor(self):
        return self.color

    def getBrightness(self):
        return self.brightness
