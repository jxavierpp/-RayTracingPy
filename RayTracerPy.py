import numpy as np
import png
from PIL import Image 
from geom import RayMath
from geom import T3D
from geom import Scene
from maths import DoubleMath
from obj  import Primitive
from surf import Surface
from math import tan,radians, pow, log, exp

class RayTracerPy(object):
    sizeX = 0
    sizeY = 0
    level = 0
    maxlevel = 0
    scene = 0
    image = 0
    lightDist = 0
    npImage = 0
    LUT=np.zeros(256,dtype=np.uint8)

    def __init__(self):
        pass

    def execute(self):
        self.setup()
        self.raytracer()
        self.writeImage()

    def setup(self):
        self.level = 0
        self.sizeX = 512
        self.sizeY = 512
        self.image = Image.new('RGB', (self.sizeX, self.sizeY), color = 'red')
        self.npImage = np.array(self.image)
        self.scene = Scene()

    def raytracer(self):
        screenX = T3D()
        screenY = T3D()
        firstRay = T3D()
        ray = T3D(0,0,0)
        self.viewing(screenX, screenY, firstRay)

        for lineY in range(0, self.sizeY):
            for pixelX in range(0, self.sizeX):
                ray.x = firstRay.x + pixelX * screenX.x - lineY * screenY.x
                ray.y = firstRay.y + pixelX * screenX.y - lineY * screenY.y
                ray.z = firstRay.z + pixelX * screenX.z - lineY * screenY.z
                RayMath().normalize(ray)
                color = self.intersect(-1, self.scene.camera.lookFrom, ray)
                self.npImage[pixelX, lineY] = color
        
    def viewing(self, screenX, screenY, firstRay):
        gaze = T3D()

        gaze.x = self.scene.camera.lookTo.x - self.scene.camera.lookFrom.x
        gaze.y = self.scene.camera.lookTo.y - self.scene.camera.lookFrom.y
        gaze.z = self.scene.camera.lookTo.z - self.scene.camera.lookFrom.z
        dist = RayMath().normalize(gaze)

        # screenX = gaze cross up
        RayMath().crossp(screenX, gaze, self.scene.camera.up)
        RayMath().normalize(screenX)

        # screenY = screenX cross gaze
        RayMath().crossp(screenY, screenX, gaze)

        dist *= 2.0
        magnitude = dist * tan(radians(self.scene.camera.hFOV)) / self.sizeX
        screenX.x *= magnitude
        screenX.y *= magnitude
        screenX.z *= magnitude

        magnitude = dist * tan(radians(self.scene.camera.vFOV)) / self.sizeY
        screenY.x *= magnitude
        screenY.y *= magnitude
        screenY.z *= magnitude

        firstRay.x = self.scene.camera.lookTo.x - self.scene.camera.lookFrom.x
        firstRay.y = self.scene.camera.lookTo.y - self.scene.camera.lookFrom.y
        firstRay.z = self.scene.camera.lookTo.z - self.scene.camera.lookFrom.z

        firstRay.x += self.sizeY / 2.0 * screenY.x - self.sizeX / 2.0 * screenX.x
        firstRay.y += self.sizeY / 2.0 * screenY.y - self.sizeX / 2.0 * screenX.y
        firstRay.z += self.sizeY / 2.0 * screenY.z - self.sizeX / 2.0 * screenX.z
    
    def intersect(self, source, pos, ray):
        objHit = -1
        s = 99.99e20
        ss = 99.99e20

        for objTry in range(0, self.scene.getObjectsCount()):
            if (objTry != source)    :
                s = self.scene.getObject(objTry).intersect(pos, ray)
                if (s > 0.0 and s < ss):
                    objHit = objTry
                    ss = s
            
        if (objHit < 0):
            return self.scene.bgColor
        
        hit = T3D()
        hit.x = pos.x + ss * ray.x
        hit.y = pos.y + ss * ray.y
        hit.z = pos.z + ss * ray.z

        normal = self.scene.getObject(objHit).normal(hit)

        r,g,b = self.shade(hit, ray, normal, self.scene.getObject(objHit))
        # print(r,g,b)

        return r,g,b
    
    def shade(self, position, ray, normal, objectType):
        # ambient light contribution
        surface = objectType.getSurface()
        red = surface.ambientColor[0]
        green = surface.ambientColor[1]
        blue = surface.ambientColor[2]

        # calculate reflected ray
        reflectedRay = T3D()
        k = -2.0 * RayMath().dotp(ray, normal)
        reflectedRay.x = k * normal.x + ray.x
        reflectedRay.y = k * normal.y + ray.y
        reflectedRay.z = k * normal.z + ray.z

        for lightNum in range(0, self.scene.getLightsCount()):
            # get ray to light
            lightray = self.lightRay(lightNum, position)
            diffuse = RayMath().dotp(normal, lightray)
            if (diffuse > 0):
                # object faces light, add diffuse
                bright = self.brightness(objectType.getId(), lightNum, position, lightray)
                diffuse *= bright
                red += np.multiply(surface.diffuseColor[0], diffuse)
                green += np.multiply(surface.diffuseColor[1], diffuse)
                blue += np.multiply(surface.diffuseColor[2], diffuse)

                spec = RayMath().dotp(reflectedRay, lightray)
                if (spec > 0):
                    # highlight is here, add specular
                    spec = bright * pow(spec, surface.getSpecularCoefficient())
                    red += np.multiply(surface.specularColor[0], spec)
                    green += np.multiply(surface.specularColor[1], spec)
                    blue += np.multiply(surface.specularColor[2], spec)
                
        red = self.clamp(red, 0, 255)
        green = self.clamp(green, 0, 255)
        blue = self.clamp(blue, 0, 255)
        shadeColor = ((int) (red + 0.5), (int) (green + 0.5), (int) (blue + 0.5))
        return shadeColor

    def lightRay(self, lightNum, objPos):
        lightRay = T3D()
        lightRay.x = self.scene.lights[lightNum].position[0] - objPos.x
        lightRay.y = self.scene.lights[lightNum].position[1] - objPos.y
        lightRay.z = self.scene.lights[lightNum].position[2] - objPos.z
        self.lightDist = RayMath().normalize(lightRay)

        return lightRay

    def brightness(self, source, lightNum, pos, ray):
        for objTry in range(0, self.scene.getObjectsCount()):
            if (objTry != source):                              # don't try source
                s = self.scene.getObject(objTry).intersect(pos, ray)
                if (s > 0 and DoubleMath().leq(s, self.lightDist)):
                    return 0                                    # object in shadow
        # object not in shadow
        return self.scene.getLight(lightNum).brightness

    def clamp(self, x, min, max):
        if (x < min):
            x = min
        if (x > max):
            x = max
        return x

    def gammaCorrect(self, intensity):
        GAMMA = 2.2

        # scale to 0-1 range
        dval = self.clamp(intensity / 255.0, 0, 1)

        # do gamma correction
        dval = exp(log(dval) / GAMMA)

        # convert to integer, range 0-255
        dval *= 255.0
        ival = (int) (dval + 0.5)

        return ival

    def writeImage(self):
        # pixels = self.LUT[self.npImage]

        # self.image.save('output.png')
        result = Image.fromarray(self.npImage)
        result.save('output.png')
       

        