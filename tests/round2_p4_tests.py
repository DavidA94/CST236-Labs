"""
Test for Round 2 Part 4
"""
from unittest import TestCase
from source.game import Game

class TestRound2Test4(TestCase):

    def test_game_unit_auto(self):
        g = Game()
        self.assertEqual(g.getUnitType(), "imperial")

    def test_game_unit_imperial(self):
        g = Game(uType="imperial")
        self.assertEqual(g.getUnitType(), "imperial")

    def test_game_unit_metric(self):
        g = Game(uType="metric")
        self.assertEqual(g.getUnitType(), "metric")

    def test_game_unit_parsec(self):
        g = Game(uType="parsec")
        self.assertEqual(g.getUnitType(), "parsec")

    def test_game_unit_nautical(self):
        g = Game(uType="nautical")
        self.assertEqual(g.getUnitType(), "nautical")

    def test_game_unit_change(self):
        # default
        g = Game()              # default / imperial
        self.assertEqual(g.getUnitType(), "imperial")
        g.setUnitType("metric") # metric
        self.assertEqual(g.getUnitType(), "metric")
        g.setUnitType("parsec") # parsec
        self.assertEqual(g.getUnitType(), "parsec")
        g.setUnitType("nautical") # nautical
        self.assertEqual(g.getUnitType(), "nautical")

        # Bad unit passed in
        try:
            g.setUnitType("feet")
        except ValueError as e:
            self.assertEqual(e.message, "Invalid Measurement")
            # Should not have changed.
            self.assertEqual(g.getUnitType(), "nautical")
        
        
