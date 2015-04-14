"""
Test for Round 1 Part 2
"""
from unittest import TestCase
import logging
from testfixtures import LogCapture
from source.defense import Shield
from source.orc import Orc
from source.game import Game

class TestRound1Test2(TestCase):

    def test_orc_logging_info(self):
        numOrcs = 0
        with LogCapture() as l:
            o = Orc()
            numOrcs = Orc.count

        l.check(('orcLog', 'INFO', 'Creating a new orc with id ' + str(numOrcs)))

    def test_defense_logging_info_safe(self):

        with LogCapture(names="defenseLog", level=logging.INFO) as l:
            s = Shield()
            s.orcs.append(Orc(distance=150))
            s.orcs.append(Orc(distance=125))

            s.is_safe()
            s.orc_speeds()
            s.orc_dists()

        l.check(("defenseLog", "INFO", "Creating new Shield"),
                ("defenseLog", "INFO", "Checking if any orcs are too close"),
                ("defenseLog", "INFO", "All orcs are far enough away"),
                ("defenseLog", "INFO", "Getting orc speeds"),
                ("defenseLog", "INFO", "Getting orc distances"),
                )

    def test_defense_logging_info_not_safe(self):

        with LogCapture(names="defenseLog", level=logging.INFO) as l:
            s = Shield()
            s.orcs.append(Orc(distance=100))
            s.orcs.append(Orc(distance=50))

            s.is_safe()
            s.orc_speeds()
            s.orc_dists()

        l.check(("defenseLog", "INFO", "Creating new Shield"),
                ("defenseLog", "INFO", "Checking if any orcs are too close"),
                ("defenseLog", "WARNING", "Orc " + str(Orc.count) + " has breached the perimeter"),
                ("defenseLog", "INFO", "Getting orc speeds"),
                ("defenseLog", "INFO", "Getting orc distances"),
                )

    def test_defense_logging_warning_safe(self):

        with LogCapture(names="defenseLog", level=logging.WARNING) as l:
            s = Shield()
            s.orcs.append(Orc(distance=150))
            s.orcs.append(Orc(distance=125))

            s.is_safe()
            s.orc_speeds()
            s.orc_dists()

        l.check()

    def test_defense_logging_warning_not_safe(self):
        orcs = []

        with LogCapture(names="defenseLog", level=logging.WARNING) as l:
            s = Shield()
            s.orcs.append(Orc(distance=50))
            orcs.append(Orc.count)
            s.orcs.append(Orc(distance=75))
            orcs.append(Orc.count)

            s.is_safe()
            s.orc_speeds()
            s.orc_dists()

        l.check(("defenseLog", "WARNING", "Orc " + str(orcs[0]) + " has breached the perimeter"))

    def test_game_logging_no_fatal(self):

        with LogCapture(names="gameLog", level=logging.INFO) as l:
            g = Game()
            g.start_demo_mode()
            try:
                g.button_pressed('x')
            except AttributeError:
                pass

            try:
                g.get_orcs()
            except AttributeError:
                pass

            try:
                g.getUnitType()
            except AttributeError:
                pass

            try:
                g.setUnitType("imperial")
            except AttributeError:
                pass

            g.stop_demo_mode()

            g.button_pressed("s")
            g.button_pressed("E")
            g.button_pressed("N")
            g.button_pressed("T")
            g.button_pressed("e")
            g.button_pressed("r")
            g.button_pressed(" ")
            g.button_pressed("t")
            g.button_pressed("h")
            g.button_pressed("e")
            g.button_pressed(" ")
            g.button_pressed("T")
            g.button_pressed("r")
            g.button_pressed("e")
            g.button_pressed("e")
            g.button_pressed("s")

        l.check(("gameLog", "INFO", "Creating new Game"),
                ("gameLog", "INFO", "Setting the current measurement to: imperial"),
                ("gameLog", "INFO", "Adding 10 Orcs"),
                ("gameLog", "INFO", "x was pressed"),
                ("gameLog", "ERROR", "App is in demo mode. Cannot send key presses."),
                ("gameLog", "ERROR", "App is in demo mode. Cannot send key presses."),
                ("gameLog", "ERROR", "App is in demo mode. Cannot send key presses."),
                ("gameLog", "ERROR", "App is in demo mode. Cannot send key presses."),
                ("gameLog", "INFO", "s was pressed"),
                ("gameLog", "INFO", "E was pressed"),
                ("gameLog", "INFO", "N was pressed"),
                ("gameLog", "INFO", "T was pressed"),
                ("gameLog", "INFO", "e was pressed"),
                ("gameLog", "INFO", "r was pressed"),
                ("gameLog", "INFO", "  was pressed"),
                ("gameLog", "INFO", "t was pressed"),
                ("gameLog", "INFO", "h was pressed"),
                ("gameLog", "INFO", "e was pressed"),
                ("gameLog", "INFO", "  was pressed"),
                ("gameLog", "INFO", "T was pressed"),
                ("gameLog", "INFO", "r was pressed"),
                ("gameLog", "INFO", "e was pressed"),
                ("gameLog", "INFO", "e was pressed"),
                ("gameLog", "INFO", "s was pressed"),
                ("gameLog", "INFO", "Making all Orcs run away")
                )

    def test_game_logging_fatal(self):
        with LogCapture(names="gameLog", level=logging.FATAL) as l:
            g = Game()
            with self.assertRaises(SystemExit) as cm:
                g.button_pressed("X")

        l.check(("gameLog", "CRITICAL", "X pressed. Killing app"))

