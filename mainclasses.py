class Building(object):
    def __init__(self, walls):
        self.walls = walls

class Wall(object):
    def __init__(self, diametr, square, type):
        self.diametr = diametr
        self.fullSquare = square
        self.actualSquare = square
        self.typeid = type
        self.assemblies = []
        self.layers = []
        self.assemblieswidth = 0
    
    def AddAssemblies(self, assemblies):
        self.assemblies = assemblies
        self.assemblieswidth = sum(assemblies)
        self.actualSquare = self.actualSquare - self.assemblieswidth
    
    def A(self, length): return length / self.actualSquare
    
    def AddLayers(self, newlayers): self.layers += newlayers
    def AddLayer(self, newlayer): self.layers.append(newlayer)
    def ClearLayers(self): self.layers = []
    def LayersResistSum(self):
        sum = 0
        for elem in self.layers:
            sum += elem.thermalResistance
        return sum
    def SuppositiveConductivity(self, insideratio, outsideratio): return 1 / insideratio + self.LayersResistSum + 1 / outsideratio



class Assembly(object):
    def __init__(self, assemblytype):
        self.type = assemblytype

class Layer(object):
    def __init__(self, width, conductivity):
        self.width = width
        self.conductivity = conductivity
        self.thermalResistance = self.width / self.conductivity
    