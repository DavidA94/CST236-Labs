import logging
from ast import literal_eval
from Car import Car
from City import City
from hdd import HDD


cities_log = logging.getLogger("cities_log")


class Cities(object):

    def __init__(self, filename="cities.txt", start_city=None):
        """
        Create a new Cities object
        :param filename: The filename to remember so that an active file is kept
        :param start_city: The starting desination
        """

        self.cities = []
        self.filename = filename
        cities_log.info("Creating new cities object")
        self.hdd = HDD(100, 1)

        # The start point should probably be required, but leaving as None
        # for backward compatibility with older tests.
        self.start_point = start_city

        if start_city is not None:
            self.add_city(start_city)

    def add_city(self, city):
        """
        :param city: The City to be added
        """


        if type(city) is not City:
            cities_log.error("Attribute city must be of type City")

        elif city not in self.cities:
            self.cities.append(city)
            cities_log.info("Adding city: " + str(city))
            self.write_file()

    def rem_city(self, city):
        """
        :param city: The city to be removed

        Removes a city
        """

        if type(city) is not City:
            cities_log.error("Attribute city must be of type City")
        elif city in self.cities:
            self.cities.remove(city)
            self.write_file()

    def read_from_file(self, f=None):
        """
        :param f: The file object to be read through

        Reads a file and adds cities
        """
        for line in f:
            if len(line) > 0:
                line = line.split(", ")
                line[1] = literal_eval(line[1])
                line[2] = int(line[2])
                self.add_city(City(*tuple(line)))

    def estimate_speed(self, city1, city2, car):
        """
        :param city1: The first city to be used in teh estimate
        :param city2: The second city to be used in the estimate
        :param car: The car that is being driven
        :return: Whether the notwork or the car is faster
        """

        # Technically this should find the two cities, and do some fancy math
        # but this isn't a full implementation, so > 200 = driving is faster
        if (type(car) is Car and car.speed > 200) or car > 200:
            cities_log.info("Going between " + str(city1) + " and " +
                            str(city2) + ": driving is faster")
            return "Driving is faster"
        else:
            cities_log.info("Going between " + str(city1) + " and " +
                            str(city2) + ": network is faster")
            return "Network is faster"

    def add_hdd_space(self, space_to_add):
        """
        :param space_to_add: The new amount of storage

        Increases the storage space
        """
        self.hdd.size += space_to_add

    def change_hdd_gps(self, new_speed):
        """
        :param new_speed: The new G/s for the HDD

        Changes the speeds of the HDD's G/s
        """

        self.hdd.gps = new_speed

    def write_file(self):
        """
        Writes a file with all the cities
        """
        f = open(self.filename, 'w')
        for city in self.cities:
            f.write(city.write() + "\n")

        f.close()

    def calc_route(self, *args):
        """
        :param args: The cities to be used in the calcualtion
        :return: A more accurate picture of the route

        Calculates a route between up to 10 cities
        """
        if len(args) < 1:
            return "Please pass cities"
        elif len(args) > 10:
            return "Error: Too many cities"
        else:
            # Find cities by names
            # Generate some fancy stuff that give a more accurate picture
            return "More accurate picture"

    def latency_calc(self, city1, city2):
        """
        :param city1: The first city
        :param city2: The second city
        :return: Network latency accounted for

        Accounts for latency in a network between two cities
        """
        # There should be some fancy math, and looking up the cities passed in,
        # but meh.

        return "Network latency accounted for"