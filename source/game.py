class Game(object):
    def __init__(self, uType="imperial"):
        self.playing = True
        self.response = []
        self.__unitTypes = ["imperial", "metric", "parsec", "nautical"]
        self.__unitType = "imperial"
        self.setUnitType(uType)
        

    def button_pressed(self, button):
        if button == 'x' or button == 'X':
            self.playing = False
        elif button == '?':
            self.response.append(["A: Attack",
                                  "S: Surrender",
                                  "X: Stop this charade"]
                                 )

    def setUnitType(self, uType):
        if(uType in self.__unitTypes):
            self.__unitType = uType
        else:
            raise ValueError("Invalid Measurement")

    def getUnitType(self):
        return self.__unitType
