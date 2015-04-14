"""
Orc object
"""
import logging

# Logging for this file
orcLog = logging.getLogger("orcLog")

class Orc(object):

    count = 0

    def __init__(self, distance=100, velocity=5, oType='A'):
        self.distance = distance
        self.velocity = velocity
        self.type = oType
        self.priority = 5

        Orc.count = Orc.count + 1
        self.id = Orc.count

        orcLog.info("Creating a new orc with id " + str(self.id))

