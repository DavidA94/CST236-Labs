"""
Test for Round 2 Part 1
"""
from unittest import TestCase
from source.game import Game

class TestRound2Test1(TestCase):

    def test_button_pressed_qMark(self):
        g = Game()
        g.button_pressed("?")
        cmds = g.response.pop()
        expectedCmds = ["A: Attack", "S: Surrender", "X: Stop this charade"]
        self.assertEqual(cmds, expectedCmds)
    
        
