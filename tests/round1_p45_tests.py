"""
Test for Round 1 Parts 4 and 5
"""
from unittest import TestCase
from source.orc import Orc
from source.defense import Shield

class TestRound1Test45(TestCase):

    def test_orc_distances(self):
        s = Shield(100)
        o1 = Orc(101)
        o2 = Orc(150)
        o3 = Orc(200)
        o4 = Orc(123)
        o5 = Orc(143)
        s.orcs.append(o1)
        s.orcs.append(o2)
        s.orcs.append(o3)
        s.orcs.append(o4)
        s.orcs.append(o5)

        self.assertEqual(s.orc_dists(), [1, 50, 100, 23, 43])

    def test_orc_speeds(self):
        s = Shield(100)
        o1 = Orc(101, 5)
        o2 = Orc(150, 10)
        o3 = Orc(200, 15)
        o4 = Orc(123, 7)
        o5 = Orc(143, 13)
        s.orcs.append(o1)
        s.orcs.append(o2)
        s.orcs.append(o3)
        s.orcs.append(o4)
        s.orcs.append(o5)

        self.assertEqual(s.orc_speeds(), [5, 10, 15, 7, 13])
