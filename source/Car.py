class Car(object):
    def __init__(self, speed=None, make=None):
        if speed is None and make is not None:
            self.make = make

            if make == "Porsche":
                self.speed = 100
            elif make == "Bus":
                self.speed = 65
            elif make == "Cement Truck":
                self.speed = 55
            elif make == "laden swallow":
                self.speed = 70
            else:
                self.speed = 55

        else:
            self.make = make
            self.speed = speed
