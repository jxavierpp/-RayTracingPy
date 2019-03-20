from obj import Light,Camera,Sphere
from geom.T3D import T3D
from surf import Surface

class Scene(object):
    def __init__(self, option):
        self.camera: Camera
        self.lights = []
        self.objects = []
        self.bgColor = (0, 0, 0)
        self.filename = ''
        self.maxLevel = 0
        
        if(option == 1):
            self.example1()
        if(option == 2):
            self.example2()
        if(option == 3):
            self.example3()

    def example1(self):
        self.filename = "output1.png"
        self.bgColor = (100, 200, 250)
        self.lights.append(Light((100, 300, 0),     #position
                (255, 255, 255),                    #color
                1))                                 #brightness

        self.camera = Camera(T3D(100, 0, 0),        #look from
                T3D(),                              #look at
                T3D(0, 1, 0),                       #up
                50, 50)                             #fov

        self.objects.append(Sphere(0, T3D(5, 30, 40), 40,
                Surface((30, 0, 0),            #ambient color
                        (90, 0, 0),            #diffuse color
                        (190, 120, 120),       #specular color
                        15,0,0)))

        self.objects.append(Sphere(1, T3D(-10, -10, -40), 30,
                Surface((0, 50, 0),            #ambient color
                        (0, 100, 0),           #diffuse color
                        (30, 40, 30),          #specular color
                        2,0,0)))

    def example2(self):
        self.filename = "output2.png"
        self.bgColor = (100, 200, 250)
        self.lights.append(Light((100, 300, 0),      # position
                (255, 255, 255),                     # color
                1))                                  # brightness

        self.camera = Camera(T3D(100, 0, 0),         # look from
                T3D(0,0,0),                          # look at
                T3D(0, 1, 0),                        # up
                50, 50)                              # fov

        self.objects.append(Sphere(0, T3D(5, 30, 40), 40,
                Surface((30, 0, 0),               # ambient color
                        (90, 0, 0),               # diffuse color
                        (190, 120, 120),          # specular color
                        5, 0.2, 0)))

        self.objects.append(Sphere(1, T3D(-10, -10, -40), 30,
                Surface((0, 50, 0),               # ambient color
                        (0, 100, 0),              # diffuse color
                        (30, 40, 30),             # specular color
                        2, 0.5, 0)))

        self.maxLevel = 4
    
    def example3(self):
        self.filename = "output3.png"
        self.bgColor = (100, 200, 250)
        self.lights.append(Light((100, 300, 0),      # position
                (255, 255, 255),                     # color
                1))                                  # brightness

        self.camera = Camera(T3D(100, 0, 0),         # look from
                T3D(0,0,0),                          # look at
                T3D(0, 1, 0),                        # up
                50, 50)                              # fov

        self.objects.append(Sphere(0, T3D(5, 30, 40), 40,
                Surface((30, 0, 0),               # ambient color
                        (90, 0, 0),               # diffuse color
                        (190, 120, 120),          # specular color
                        5, 0.2, 0.2)))

        self.objects.append(Sphere(1, T3D(-10, -10, -40), 30,
                Surface((0, 50, 0),               # ambient color
                        (0, 100, 0),              # diffuse color
                        (30, 40, 30),             # specular color
                        2, 0.5, 0)))

        self.objects.append(Sphere(2, T3D(-150, 40, 20), 60,
                Surface((60, 60, 0),         # ambient color
                        (90, 90, 0),         # diffuse color
                        (190, 190, 90),      # specular color
                        5, 0.2, 0)))

        self.maxLevel = 4

    def getLight(self, i):
        return self.lights[i]

    def getLightsCount(self):
        return len(self.lights)

    def getObject(self,i):
        return self.objects[i]

    def getObjectsCount(self):
        return len(self.objects)