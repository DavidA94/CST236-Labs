import logging

city_log = logging.getLogger("city_log")


class City(object):
    def __init__(self, city_name, location, connection_speed):
        """
        :param city_name: The name of the city
        :param location: The coordinates of the city
        :param connection_speed: The speed of the internet in the city

        Creates a new City object
        """
        if(type(city_name) is not str or
           type(location) is not tuple or
           type(connection_speed) is not int):
                city_log.error("Bad attribute type passed in.")
                self.name = self.location = self.connection_speed = None

        else:
            self.name = city_name
            self.location = location
            self.connection_speed = connection_speed
            city_log.info("New City Created")

    def __str__(self):
        """
        :return: A stringified version of the class
        """
        return (self.name + " -- Location: " + str(self.location) +
                "; C_Speed: " + str(self.connection_speed))

    def __eq__(self, rhs):
        """
        :param rhs: The right hand side of the == test
        :return: If self and rhs are equal

        Tests if self is == to rhs
        """
        return (self.name == rhs.name and
                self.location == rhs.location and
                self.connection_speed == rhs.connection_speed)

    def check_hdd(self, HDD):
        """
        :param HDD: The HDD to be checked
        :return: Whether the net or an HDD is faster

        Checks if the net or the HDD is faster
        """
        # There should be fancy math here, but meh.

        if self.connection_speed >= 100:
            return "The net is faster"
        else:
            return "The HDD is faster"

    def time_diff(self, hdd):
        """
        :param hdd: The HDD to be checked against
        :return: The time difference

        Calculates the time difference between the net and the HDD
        """
        # There should be fancy math here, but meh

        return 10

    def write(self):
        """
        :return: A string that can be written to a file to be read later
        """
        return (self.name + ", " + str(self.location).replace(" ", "") +
                ", " + str(self.connection_speed))