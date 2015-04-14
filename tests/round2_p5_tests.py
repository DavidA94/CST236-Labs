"""
Test for Round 2 Part 5
"""
from unittest import TestCase
from source.orc import Orc

class TestRound2Test5(TestCase):

    def test_orc_priority_auto(self):
        o = Orc()
        self.assertEqual(o.priority, 5)

    def test_orc_priority_changing_number(self):
        o = Orc()
        self.assertEqual(o.priority, 5)
        o.priority = 10
        self.assertEqual(o.priority, 10)
        o.priority = 1
        self.assertEqual(o.priority, 1)

    def test_orc_priority_changing_value(self):
        o = Orc()
        o.priority = "med"
        self.assertEqual(o.priority, "med")
        o.priority = "high"
        self.assertEqual(o.priority, "high")
        o.priority = "low"
        self.assertEqual(o.priority, "low")

        
    
        
