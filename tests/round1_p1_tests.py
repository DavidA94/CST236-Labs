"""
Test for source.source2
"""
from unittest import TestCase
from source.orc import Orc
from source.defense import Shield

class TestRound1Test1(TestCase):

    def test_has_breached_very_close(self):
        s = Shield(100)
        o = Orc(50)
        s.orcs.append(o) # list of orcs
        self.assertEqual(s.is_safe(), False)

    def test_has_breached_edge(self):
        s = Shield(100)
        o = Orc(99)
        s.orcs.append(o) # list of orcs
        self.assertEqual(s.is_safe(), False)

    def test_has_not_breached_edge(self):
        s = Shield(100)
        o = Orc(101)
        s.orcs.append(o) # list of orcs
        self.assertEqual(s.is_safe(), True)

    def test_has_not_breached_very_far(self):
        s = Shield(100)
        o = Orc(150)
        s.orcs.append(o) # list of orcs
        self.assertEqual(s.is_safe(), True)

    def test_set_perim(self):
        s = Shield(100)
        self.assertEqual(s.perim(), 100)

    def test_has_breached_multiple(self):
        s = Shield(102)
        o1 = Orc(150)
        o2 = Orc(101)
        o3 = Orc(99)
        o4 = Orc(50)
        s.orcs.append(o1)
        s.orcs.append(o2)
        s.orcs.append(o3)
        s.orcs.append(o4)

        self.assertEqual(s.is_safe(), False)
