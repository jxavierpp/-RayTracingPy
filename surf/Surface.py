class Surface:
    ambientColor = 0
    diffuseColor = 0
    specularColor = 0
    specularCoefficient  = 0
    reflectionCoefficient = 0
    transparencyCoefficient  = 0

    def __init__(self, ambientColor, diffuseColor, specularColor, specularCoefficient, reflectionCoefficient, transparencyCoefficient):
        self.ambientColor = ambientColor
        self.diffuseColor = diffuseColor
        self.specularColor = specularColor
        self.specularCoefficient = specularCoefficient
        self.reflectionCoefficient = reflectionCoefficient
        self.transparencyCoefficient = transparencyCoefficient
        

    def getAmbientColor(self):
        return self.ambientColor

    def getDiffuseColor(self):
        return self.diffuseColor
    
    def getSpecularColor(self):
        return self.specularColor
    
    def getSpecularCoefficient(self):
        return self.specularCoefficient   

    def getReflectionCoefficient(self):
        return self.reflectionCoefficient
    
    def getTransparencyCoefficient(self):
        return self.transparencyCoefficient
    
    def toString(self):
        return ("ambientColor: " + self.ambientColor +
               ", diffuseColor: " + self.diffuseColor +
               ", specularColor: " + self.specularColor +
               ", specularCoefficient: " + self.specularCoefficient +
               ", reflectionCoefficient: " + self.reflectionCoefficient +
               ", transparencyCoefficient: " + self.transparencyCoefficient)
    