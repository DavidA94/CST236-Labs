"""
Test for Round 3 Part 3
"""
from unittest import TestCase
from source.game import Game

class TestRound3Test3(TestCase):

    def test_easy_win(self):
        g = Game()

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

        orcs = g.get_orcs()

        for orc in orcs:
            self.assertGreater(orc.distance, 500)
        
        
