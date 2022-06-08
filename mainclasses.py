import math

def closer2(value1, value2, parameter):
    if math.fabs(parameter - value1) < math.fabs(parameter - value2): return value1
    else: return value2
def closer3(value1, value2, value3, parameter):
    m = min(math.fabs(parameter - value1), min(math.fabs(parameter - value2), math.fabs(parameter - value3)))
    if m == math.fabs(parameter - value1): return value1
    elif m == math.fabs(parameter - value2) : return value2
    else: return value3
def closerList(values, parameter):
    m = 1000
    id = -1
    for i in range(len(values)):
        if math.fabs(parameter - values[i]) < m:
            m = math.fabs(parameter - values[i])
            id = i
    return values[id]
def interpolation(amount1, amount2, value1, value2, parameter):
    points = amount2 - amount1
    difference = value2 - value1
    point = difference / points
    return value1 + point * (parameter - value1)

class Building(object):
    def __init__(self, walls):
        self.walls = walls

class Wall(object):
    def __init__(self, width, square, type):
        self.width = width
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



class Layer(object):
    def __init__(self, width, conductivity):
        self.width = width
        self.conductivity = conductivity
        self.thermalResistance = self.width / self.conductivity


class Assembly0(object):
    def __init__(self, value, amount):
        self.name = 'Гибкие связи'
        self.type = 0

        self.value = value
        self.amount = amount

class Assembly1(object):
    def __init__(self, length, amount):
        self.name = 'Тарельчатый анкер'
        self.type = 0

        self.length = length
        self.amount = amount

    def HeatLoss(self):
        if self.length <= 2: x = 0.006
        elif self.length <= 5: x = 0.005
        elif self.length <= 11: x = 0.004
        elif self.length <= 16: x = 0.003
        elif self.length <= 24: x = 0.0025
        elif self.length <= 40: x = 0.002
        elif self.length <= 70: x = 0.0015
        else: x = 0.001

class Assembly2(object):
    def __init__(self, value, amount):
        self.name = 'Кронштейн'
        self.type = 0
        
        self.value = value
        self.amount = amount

class Assembly3(object):
    
    def __init__(self, wall_type, insulation_resistance, plate_width, base_conductivity, perforated_or_NTE, parameter, value):
        self.name = 'Сопряжение с перекрытиями и балконами'
        self.type = 1
        self.conducts = [0.2, 0.6, 1.8]
        self.resists = [1.22, 2.44, 6.1]

        self.wall = wall_type
        self.resist = insulation_resistance
        self.width = plate_width
        self.cond = base_conductivity
        self.paramtype = perforated_or_NTE
        self.parameter = parameter
        self.value = value

    # def HeatLoss(self):
    #     if self.paramtype == 0:
    #         if self.cond in self.conducts:

