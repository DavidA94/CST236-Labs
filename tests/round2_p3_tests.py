"""
Test for source.source2
"""
from unittest import TestCase
from source.orc import Orc

class TestRound2Test3(TestCase):

    def test_orc_ids(self):
        # nose 2 doesn't make this start from zero, so get the starting nubmer
        startNum = Orc.count + 1
        o0 = Orc()
        o1 = Orc()
        o2 = Orc()
        o3 = Orc()
        o4 = Orc()

        

        self.assertEqual(o0.id, startNum)
        self.assertEqual(o1.id, startNum + 1)
        self.assertEqual(o2.id, startNum + 2)
        self.assertEqual(o3.id, startNum + 3)
        self.assertEqual(o4.id, startNum + 4)
        
        
