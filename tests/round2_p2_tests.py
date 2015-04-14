"""
Test for Round 2 Part 2
"""
from unittest import TestCase
from source.orc import Orc

class TestRound2Test2(TestCase):

    def test_orc_types(self):
        o0 = Orc(oType='A')
        o1 = Orc(oType='B')
        o2 = Orc(oType='C')
        o3 = Orc(oType='D')
        o4 = Orc(oType='E')
        o5 = Orc(oType='F')
        o6 = Orc(oType='G')
        o7 = Orc(oType='H')
        o8 = Orc(oType='I')
        o9 = Orc(oType='J')
        o10 = Orc() #default = A 

        self.assertEqual(o0.type, 'A')
        self.assertEqual(o1.type, 'B')
        self.assertEqual(o2.type, 'C')
        self.assertEqual(o3.type, 'D')
        self.assertEqual(o4.type, 'E')
        self.assertEqual(o5.type, 'F')
        self.assertEqual(o6.type, 'G')
        self.assertEqual(o7.type, 'H')
        self.assertEqual(o8.type, 'I')
        self.assertEqual(o9.type, 'J')
        self.assertEqual(o10.type, 'A')
