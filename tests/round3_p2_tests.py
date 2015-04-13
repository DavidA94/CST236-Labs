"""
Test for source.source2
"""
from unittest import TestCase
from source.game import Game

class TestRound3Test2(TestCase):

    def test_game_demo(self):
        g = Game()
        g.start_demo_mode()

        # No calls should work now
        try:
            g.button_pressed("")
        except AttributeError as e:
            self.assertEqual(e.message, "Cannot call methods while in demo mode")

        try:
            g.setUnitType("")
        except AttributeError as e:
            self.assertEqual(e.message, "Cannot call methods while in demo mode")

        try:
            g.getUnitType()
        except AttributeError as e:
            self.assertEqual(e.message, "Cannot call methods while in demo mode")

        # Stop demo mode
        g.stop_demo_mode()

        # Should be able to get the unit type now (assume other calls will also work)
        self.assertEqual(g.getUnitType(), "imperial")
        
    
