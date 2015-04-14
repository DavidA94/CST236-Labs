"""
Test for Round 1 Part 3
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
        with self.assertRaises(SystemExit) as cm:
            response = g.button_pressed('x')
        self.assertEqual(cm.exception.code, 1)

    def test_button_pressed_is_X(self):
        g = Game()
        with self.assertRaises(SystemExit) as cm:
            response = g.button_pressed('X')
            
        self.assertEqual(cm.exception.code, 1)
