"""
Test for source.source2
"""
from unittest import TestCase
from source.game import Game

class TestRound1Test3(TestCase):

    def test_button_pressed_not_x(self):
        g = Game()
        g.button_pressed('a')

        self.assertEqual(g.playing, True)

    def test_button_pressed_is_x(self):
        g = Game()
        g.button_pressed('x')

        self.assertEqual(g.playing, False)

    def test_button_pressed_is_X(self):
        g = Game()
        g.button_pressed('X')

        self.assertEqual(g.playing, False)
    
