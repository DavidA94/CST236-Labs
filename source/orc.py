class Orc(object):
    def __init__(self, distance=100, velocity=5, oType='A'):
        self.distance = distance
        self.velocity = velocity
        self.type = oType
        self.priority = 5

        try:
            Orc.count = Orc.count + 1
            self.id = Orc.count
        except AttributeError:
            self.id = Orc.count = 0
    
