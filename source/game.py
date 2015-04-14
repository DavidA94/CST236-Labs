"""
Main Game Object
"""
import logging
import random
import sys
from defense import Shield
from orc import Orc

# Logging for this file
gameLog = logging.getLogger("gameLog")

class Game(object):
    def __init__(self, uType="imperial"):
        gameLog.info("Creating new Game")
        self.playing = True
        self.response = []
        self.__unitTypes = ["imperial", "metric", "parsec", "nautical"]
        self.__unitType = "imperial"
        self.__demoMode = False
        self.__cheatCodes = ""
        self.__defense = Shield()
        
        self.setUnitType(uType)

        gameLog.info("Adding 10 Orcs")
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        self.__defense.orcs.append(Orc())
        

    def button_pressed(self, button):
        gameLog.info(str(button) + " was pressed")
        if self.__demoMode:
            gameLog.error("App is in demo mode. Cannot send key presses.")
            raise AttributeError("Cannot call methods while in demo mode")

        if button == 'x' or button == 'X':
            gameLog.fatal("X pressed. Killing app")
            sys.exit(1)
        elif button == '?':
            gameLog.info("Giving commands")
            self.response.append(["A: Attack",
                                  "S: Surrender",
                                  "X: Stop this charade"]
                                 )
        elif button == 's':
            # All cheat codes end with S. If other buttons have been pressed,
            # then the code will have to be entered twice. This is by design.
            self.__cheatCodes += button
            if(self.__cheatCodes == "ENTer the Trees"):
                gameLog.info("Making all Orcs run away")
                for orc in self.get_orcs():
                    orc.distance = 500 + (random.random() * 100)

            self.__cheatCodes = ""

        else:
            self.__cheatCodes += button

    def setUnitType(self, uType):
        if self.__demoMode:
            gameLog.error("App is in demo mode. Cannot send key presses.")
            raise AttributeError("Cannot call methods while in demo mode")
        
        if uType in self.__unitTypes:
            gameLog.info("Setting the current measurement to: " + uType)
            self.__unitType = uType
        else:
            gameLog.error(uType + " is not a valid measurement")
            raise ValueError("Invalid Measurement")

    def getUnitType(self):
        if self.__demoMode:
            gameLog.error("App is in demo mode. Cannot send key presses.")
            raise AttributeError("Cannot call methods while in demo mode")
        return self.__unitType

    def get_orcs(self):
        if self.__demoMode:
            gameLog.error("App is in demo mode. Cannot send key presses.")
            raise AttributeError("Cannot call methods while in demo mode")
        return self.__defense.orcs

    def start_demo_mode(self):
        self.__demoMode = True;
        # Start Random stuff...

    def stop_demo_mode(self):
        self.__demoMode = False;

    
