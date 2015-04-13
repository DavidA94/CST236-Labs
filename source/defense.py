from orc import Orc

class Shield(object):
    def __init__(self, perimeter=100):
        self.orcs = []
        self._perimeter = perimeter
        

    def is_safe(self):
        for orc in self.orcs:
            if orc.distance < self._perimeter:
                return False

        return True

    def perim(self):
        return self._perimeter

    def orc_speeds(self):
        speeds = []
        for orc in self.orcs:
            speeds.append(orc.velocity)

        return speeds

    def orc_dists(self):
        dists = []
        for orc in self.orcs:
            dists.append(orc.distance - self._perimeter)

        return dists
