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
    return id
def interpolation(amount1, amount2, value1, value2, parameter):
    if parameter == amount1:
        return value1
    if parameter == amount2:
        return value2
    points = amount2 - amount1
    difference = value2 - value1
    point = difference / points
    return round(value1 + point * (parameter - amount1), 3)

class Building(object):
    def __init__(self, walls):
        self.walls = walls

class Wall(object):
    def __init__(self, square, type):
        self.fullSquare = square
        self.actualSquare = square
        self.type = type
        self.assemblies = []
        self.layers = []
        self.assembliessquare = 0
    
    def AddAssemblies(self, assemblies, assembliessquare):
        self.assemblies = assemblies
        self.assembliessquare = assembliessquare
        self.actualSquare = self.actualSquare - self.assembliessquare
    
    def A(self): return self.actualSquare / self.fullSquare
    
    def AddLayers(self, newlayers): self.layers += newlayers
    def AddLayer(self, newlayer): self.layers.append(newlayer)
    def ClearLayers(self): self.layers = []
    def LayersResistSum(self):
        sum = 0
        for elem in self.layers:
            sum += elem.thermalResistance
        return sum
    def SuppositiveConductivity(self, insideratio, outsideratio): return 1 / insideratio + self.LayersResistSum() + 1 / outsideratio

class Layer(object):
    def __init__(self, name, width, conductivity):
        self.name = name
        self.width = width
        self.conductivity = conductivity
        self.thermalResistance = self.width / self.conductivity

class Assembly(object):
    def __init__(self, amount):
        self.name = 'Unidentified'
        self.type = -1
        
        self.amount = amount
    
    def HeatLoss(self, walltype):
        return -1

class Assembly0(object):
    def __init__(self, value, amount):
        self.name = 'Гибкие связи'
        self.type = 0

        self.value = value
        self.geom_value = amount

        def HeatLoss(self, walltype):
            self.wall = walltype
            return self.amount

class Assembly1(object):
    def __init__(self, length, amount):
        self.name = 'Тарельчатый анкер'
        self.type = 0

        self.length = length
        self.geom_value = amount

    def HeatLoss(self, walltype):
        self.wall = walltype
        if self.length <= 2: x = 0.006
        elif self.length <= 5: x = 0.005
        elif self.length <= 11: x = 0.004
        elif self.length <= 16: x = 0.003
        elif self.length <= 24: x = 0.0025
        elif self.length <= 40: x = 0.002
        elif self.length <= 70: x = 0.0015
        else: x = 0.001
        return x

class Assembly2(object):
    def __init__(self, value, amount):
        self.name = 'Кронштейн'
        self.type = 0
        
        self.value = value
        self.geom_value = amount

        def HeatLoss(self, walltype):
            self.wall = walltype
            return self.amount

class Assembly3(Assembly):
    def __init__(self, insulation_resistance, plate_width, base_conductivity, assembly_type, parameter, geometrical_value):
        self.name = 'Сопряжение с перекрытиями и балконами'
        self.type = 1

        self.resist = insulation_resistance
        self.width = plate_width
        self.cond = base_conductivity
        self.paramtype = assembly_type
        self.parameter = parameter
        self.geom_value = geometrical_value

    def HeatLoss(self, walltype):
        match walltype:
            case 0:
                conducts = [0.2, 0.6, 1.8]
                resists = [1.22, 2.44, 6.1]
                condid = closerList(conducts, self.cond)
                resistid = closerList(resists, self.resist)
                match self.paramtype:
                    case 0:
                        temp160 = [[0.488, 0.500, 0.577], [0.477, 0.515, 0.592], [0.408, 0.444, 0.494]]
                        temp210 = [[0.606, 0.617, 0.698], [0.594, 0.633, 0.719], [0.592, 0.522, 0.610]]
                        return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                    case 1:
                        match self.parameter:
                            case 1:
                                temp160 = [[0.300, 0.298, 0.346], [0.304, 0.315, 0.352], [0.283, 0.298, 0.323]]
                                temp210 = [[0.379, 0.373, 0.421], [0.385, 0.396, 0.435], [0.360, 0.377, 0.406]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 3:
                                temp160 = [[0.188, 0.179, 0.208], [0.196, 0.196, 0.215], [0.198, 0.202, 0.215]]
                                temp210 = [[0.238, 0.225, 0.252], [0.252, 0.250, 0.269], [0.252, 0.259, 0.273]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 5:
                                temp160 = [[0.142, 0.131, 0.152], [0.152, 0.148, 0.160], [0.160, 0.161, 0.169]]
                                temp210 = [[0.179, 0.163, 0.181], [0.194, 0.188, 0.202], [0.204, 0.206, 0.215]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                    case 2:
                        match self.parameter:
                            case 1:
                                temp160 = [[0.126, 0.081, 0.063], [0.115, 0.098, 0.094], [0.131, 0.133, 0.137]]
                                temp210 = [[0.126, 0.072, 0.047], [0.120, 0.098, 0.093], [0.144, 0.144, 0.147]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 3:
                                temp160 = [[0.086, 0.038, 0.016], [0.076, 0.055, 0.049], [0.095, 0.092, 0.097]]
                                temp210 = [[0.086, 0.028, 0.001], [0.076, 0.055, 0.050], [0.106, 0.098, 0.103]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
            case 1:
                conducts = [0.2, 0.6, 1.8]
                resists = [1.5, 3.0, 6.0]
                condid = closerList(conducts, self.cond)
                resistid = closerList(resists, self.resist)
                match self.paramtype:
                    case 0:
                        temp160 = [[0.583, 0.660, 0.838], [0.550, 0.638, 0.781], [0.472, 0.536, 0.626]]
                        temp210 = [[0.704, 0.777, 0.958], [0.669, 0.758, 0.915], [0.580, 0.650, 0.751]]
                        return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                    case 1:
                        match self.parameter:
                            case 1:
                                temp160 = [[0.400, 0.413, 0.477], [0.346, 0.371, 0.419], [0.311, 0.338, 0.374]]
                                temp210 = [[0.483, 0.492, 0.556], [0.429, 0.456, 0.510], [0.393, 0.421, 0.466]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 3:
                                temp160 = [[0.279, 0.265, 0.285], [0.225, 0.227, 0.244], [0.209, 0.219, 0.237]]
                                temp210 = [[0.335, 0.315, 0.333], [0.281, 0.283, 0.302], [0.268, 0.279, 0.297]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 5:
                                temp160 = [[0.227, 0.202, 0.210], [0.173, 0.171, 0.179], [0.168, 0.171, 0.183]]
                                temp210 = [[0.269, 0.240, 0.244], [0.219, 0.213, 0.223], [0.213, 0.219, 0.230]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                    case 2:
                        temp160 = [[0.191, 0.156, 0.151], [0.158, 0.149, 0.155], [0.168, 0.173, 0.182]]
                        temp210 = [[0.192, 0.147, 0.134], [0.166, 0.152, 0.156], [0.182, 0.184, 0.193]]
                        return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
            case 2:
                conducts = [0.2, 0.6, 1.8]
                resists = [1.5, 3.0, 6.0]
                condid = closerList(conducts, self.cond)
                resistid = closerList(resists, self.resist)
                match self.paramtype:
                    case 0:
                        temp160 = [[0.583, 0.660, 0.838], [0.550, 0.638, 0.781], [0.472, 0.536, 0.626]]
                        temp210 = [[0.704, 0.777, 0.958], [0.669, 0.758, 0.915], [0.580, 0.650, 0.751]]
                        return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                    case 1:
                        match self.parameter:
                            case 1:
                                temp160 = [[0.400, 0.413, 0.477], [0.346, 0.371, 0.419], [0.311, 0.338, 0.374]]
                                temp210 = [[0.483, 0.492, 0.556], [0.429, 0.456, 0.510], [0.393, 0.421, 0.466]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 3:
                                temp160 = [[0.279, 0.265, 0.285], [0.225, 0.227, 0.244], [0.209, 0.219, 0.237]]
                                temp210 = [[0.335, 0.315, 0.333], [0.281, 0.283, 0.302], [0.268, 0.279, 0.297]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                            case 5:
                                temp160 = [[0.227, 0.202, 0.210], [0.173, 0.171, 0.179], [0.168, 0.171, 0.183]]
                                temp210 = [[0.269, 0.240, 0.244], [0.219, 0.213, 0.223], [0.213, 0.219, 0.230]]
                                return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)
                    case 2:
                        temp160 = [[0.191, 0.156, 0.151], [0.158, 0.149, 0.155], [0.168, 0.173, 0.182]]
                        temp210 = [[0.192, 0.147, 0.134], [0.166, 0.152, 0.156], [0.182, 0.184, 0.193]]
                        return interpolation(160, 210, temp160[resistid][condid], temp210[resistid][condid], self.width)

class Assembly4(Assembly):
    def __init__(self, insulation_resistance, plate_width, base_conductivity, assembly_type, geometrical_value):
        self.name = 'Стыки с оконными блоками'
        self.type = 1

        self.resist = insulation_resistance
        self.width = plate_width
        self.cond = base_conductivity
        self.paramtype = assembly_type
        self.geom_value = geometrical_value

    def HeatLoss(self, walltype):
        match walltype:
            case 0:
                match self.paramtype:
                    case 0:
                        widths = [60, 80, 120]
                        resists = [1.5, 3.0, 6.0]
                        widthid = closerList(widths, self.width)
                        resistid = closerList(resists, self.resist)
                        temp = [[0.121, 0.104, 0.083], [0.121, 0.104, 0.079], [0.132, 0.114, 0.092]]
                        return temp[resistid][widthid] * self.geom_value
                    case 1:
                        conducts = [0.2, 0.6, 1.8]
                        resists = [1.5, 3.0, 6.0]
                        condid = closerList(conducts, self.cond)
                        resistid = closerList(resists, self.resist)
                        temp00 = [[0.054, 0.098, 0.133], [0.050, 0.092, 0.127], [0.055, 0.097, 0.129]]
                        temp20 = [[0.042, 0.067, 0.083], [0.033, 0.054, 0.069], [0.034, 0.056, 0.068]]
                        temp60 = [[0.013, 0.031, 0.042], [0.000, 0.010, 0.019], [0.000, 0.006, 0.012]]
                        if self.width == 20:
                            return temp20[resistid][condid] * self.geom_value
                        match closer2(0, 60, self.width):
                            case 0:
                                return interpolation(0, 20, temp00[resistid][condid], temp20[resistid][condid], self.width)
                            case 60:
                                return interpolation(20, 60, temp20[resistid][condid], temp60[resistid][condid], self.width)
            case 1:
                conducts = [0.2, 0.6, 1.8]
                resists = [1.5, 3.0, 6.0]
                condid = closerList(conducts, self.cond)
                resistid = closerList(resists, self.resist)
                match self.paramtype:
                    case 0:
                        temp00 = [[0.054, 0.098, 0.133], [0.050, 0.092, 0.127], [0.055, 0.097, 0.129]]
                        temp20 = [[0.042, 0.067, 0.083], [0.033, 0.054, 0.069], [0.034, 0.056, 0.068]]
                        temp60 = [[0.013, 0.031, 0.042], [0.000, 0.010, 0.019], [0.000, 0.006, 0.012]]
                        if self.width == 20:
                            return temp20[resistid][condid] * self.geom_value
                        match closer2(0, 60, self.width):
                            case 0:
                                return interpolation(0, 20, temp00[resistid][condid], temp20[resistid][condid], self.width)
                            case 60:
                                return interpolation(20, 60, temp20[resistid][condid], temp60[resistid][condid], self.width)
                    case 1:
                        temp00 = [[0.156, 0.157, 0.183], [0.119, 0.119, 0.123], [0.109, 0.112, 0.114]]
                        temp20 = [[0.000, 0.000, 0.000], [0.092, 0.092, 0.094], [0.072, 0.072, 0.072]]
                        temp60 = [[0.000, 0.000, 0.000], [0.054, 0.052, 0.054], [0.012, 0.012, 0.012]]
                        if self.width == 20:
                            return temp20[resistid][condid] * self.geom_value
                        match closer2(0, 60, self.width):
                            case 0:
                                return interpolation(0, 20, temp00[resistid][condid], temp20[resistid][condid], self.width)
                            case 60:
                                return interpolation(20, 60, temp20[resistid][condid], temp60[resistid][condid], self.width)
                    case 2:
                        temp00 = [[0.106, 0.319, 0.696], [0.121, 0.346, 0.738], [0.134, 0.366, 0.764]]
                        temp20 = [[0.063, 0.135, 0.196], [0.069, 0.140, 0.196], [0.078, 0.147, 0.202]]
                        temp60 = [[0.017, 0.054, 0.081], [0.015, 0.046, 0.067], [0.018, 0.047, 0.064]]
                        if self.width == 20:
                            return temp20[resistid][condid] * self.geom_value
                        match closer2(0, 60, self.width):
                            case 0:
                                return interpolation(0, 20, temp00[resistid][condid], temp20[resistid][condid], self.width)
                            case 60:
                                return interpolation(20, 60, temp20[resistid][condid], temp60[resistid][condid], self.width)
            case 2:
                return self.value * self.geom_value

class Assembly5(Assembly):
    def __init__(self, insulation_resistance, insulation_width, base_conductivity, geometrical_value):
        self.name = 'Примыкание к цокольному ограждению'
        self.type = 1

        self.resist = insulation_resistance
        self.width = insulation_width
        self.cond = base_conductivity
        self.geom_value = geometrical_value

    def HeatLoss(self):
        conducts = [0.2, 0.6, 1.8]
        resists = [1.5, 3.0, 6.0]
        widths = [1.88, 3.13, 5.0, 7.81]
        condid = closerList(conducts, self.cond)
        resistid = closerList(resists, self.resist)
        widthid = closerList(widths, self.width)
        temp188 = [[0.156, 0.364, 0.553], [0.175, 0.400, 0.710], [0.194, 0.424, 0.735]]
        temp313 = [[0.135, 0.333, 0.635], [0.152, 0.363, 0.679], [0.168, 0.385, 0.703]]
        temp500 = [[0.115, 0.293, 0.593], [0.128, 0.319, 0.629], [0.141, 0.337, 0.650]]
        temp781 = [[0.099, 0.251, 0.538], [0.107, 0.271, 0.566], [0.116, 0.284, 0.581]]

        match widthid:
            case 0:
                return interpolation(1.88, 3.13, temp188[resistid][condid], temp313[resistid][condid], self.width)
            case 1:
                if closer2(1.88, 5.0, self.width) == 1.88:
                    return interpolation(1.88, 3.13, temp188[resistid][condid], temp313[resistid][condid], self.width)
                else:
                    return interpolation(3.13, 5.00, temp313[resistid][condid], temp500[resistid][condid], self.width)
            case 2:
                if closer2(3.13, 7.81, self.width) == 3.13:
                    return interpolation(3.13, 5.0, temp313[resistid][condid], temp500[resistid][condid], self.width)
                else:
                    return interpolation(5.0, 7.81, temp500[resistid][condid], temp781[resistid][condid], self.width)
            case 3:
                return interpolation(5.0, 7.81, temp500[resistid][condid], temp781[resistid][condid], self.width)

        

