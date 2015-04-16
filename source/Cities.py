import logging
from City import City
from ast import literal_eval

cities_log = logging.getLogger("cities_log")


class Cities(object):
    def __init__(self):
        self.cities = []
        cities_log.info("Creating new cities object")
        self.hdd_space = 100

    def add_city(self, city):
        if type(city) is not City:
            cities_log.error("Attribute city must be of type City")

        elif city not in self.cities:
            self.cities.append(city)
            cities_log.info("Adding city: " + str(city))

    def rem_city(self, city):
        if type(city) is not City:
            cities_log.error("Attribute city must be of type City")
        elif city in self.cities:
            self.cities.remove(city)

    def read_from_file(self, f):
        for line in f:
            if len(line) > 0:
                line = line.split(", ")
                line[1] = literal_eval(line[1])
                line[2] = int(line[2])
                self.add_city(City(*tuple(line)))

    def estimate_speed(self, city1, city2, speed):
        # Technically this should find the two cities, and do some fancy math
        # but this isn't a full implementation, so > 200 = driving is faster
        if speed > 200:
            cities_log.info("Going between " + str(city1) + " and " +
                            str(city2) + ": driving is faster")
            return "Driving is faster"
        else:
            cities_log.info("Going between " + str(city1) + " and " +
                            str(city2) + ": network is faster")
            return "Network is faster"

    def add_hdd_space(self, space_to_add):
        self.hdd_space += space_to_add
