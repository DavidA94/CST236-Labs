import logging

city_log = logging.getLogger("city_log")


class City(object):
    def __init__(self, city_name, location, connection_speed):
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
        return (self.name + " -- Location: " + str(self.location) +
                "; C_Speed: " + str(self.connection_speed))

    def __eq__(self, rhs):
        return (self.name == rhs.name and
                self.location == rhs.location and
                self.connection_speed == rhs.connection_speed)

    def check_hdd(self, hdd_size, hdd_speed):
        # There should be fancy math here, but meh.

        if self.connection_speed >= 100:
            return "The net is faster"
        else:
            return "The HDD is faster"

    def time_diff(self, hdd_size, hdd_speed):
        # There should be fancy math here, but meh

        return 10
