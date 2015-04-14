"""
Shield Defense object
"""
import logging

# Logging for this file
defenseLog = logging.getLogger("defenseLog")


class Shield(object):
    def __init__(self, perimeter=100):
        defenseLog.info("Creating new Shield")
        self.orcs = []
        self._perimeter = perimeter
        

    def is_safe(self):
        defenseLog.info("Checking if any orcs are too close")
        for orc in self.orcs:
            if orc.distance < self._perimeter:
                defenseLog.warning("Orc " + str(orc.id) + " has breached the perimeter")
                return False

        defenseLog.info("All orcs are far enough away")
        return True

    def perim(self):
        return self._perimeter

    def orc_speeds(self):
        defenseLog.info("Getting orc speeds")
        speeds = []
        for orc in self.orcs:
            speeds.append(orc.velocity)

        return speeds

    def orc_dists(self):
        defenseLog.info("Getting orc distances")
        dists = []
        for orc in self.orcs:
            dists.append(orc.distance - self._perimeter)

        return dists
