"""
Test for source.source2
"""
from unittest import TestCase
#from source.source2 import get_poly_type

class TestGetTriangleType(TestCase):

    def test_orc_breach_alert(self):
        result = None
        self.assertEqual(result, "breach_detected")

    def test_isolate_outupt_from_particular_modeul(self):
        result = None
        self.assertEqual(result, [1, 3, 5])

    def test_x_pressed(self):
        result = None
        self.assertEqual(result, False)

    def test_distance(self):
        result = None
        self.assertEqual(result, 10)

    def test_velocity(self):
        result = None
        self.assertEqual(result, 5)





    from orc import orc
    from defense import shield


    def test_has_breached(self):
        s = shield(100)
        o = orc(50)
        s.orcs.append(o) # list of orcs
        self.assertEqual(s.is_safe(), False)

    def test_has_not_breached(self):
        s = shield(100)
        o = orc(150)
        s.orcs.append(o) # list of orcs
        self.assertEqual(s.is_safe(), True)

    def test_set_perim(self):
        None

    def test_orcs(self):
        None
    

    
