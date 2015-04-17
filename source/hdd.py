class HDD(object):
    def __init__(self, size, gps):
        """
        :param size: The size of the HDD
        :param gps: The G/s of the HDD

        Creates a new HDD object
        """
        self.size = size
        self.gps = gps