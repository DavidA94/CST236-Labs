"""
Test for source.source2
"""
from unittest import TestCase
from source.source2 import get_poly_type

class TestGetTriangleType(TestCase):

    # Int Sides
    def test_get_poly_square_sides_all_int(self):
        result = get_poly_type(2, 2, 2, 2)
        self.assertEqual(result, 'square')

    def test_get_poly_rect_sides_all_int(self):
        result = get_poly_type(2, 3, 2, 3)
        self.assertEqual(result, 'rectangle')

    # Float sides
    def test_get_poly_square_sides_all_float(self):
        result = get_poly_type(2.2, 2.2, 2.2, 2.2)
        self.assertEqual(result, 'square')

    def test_get_poly_rect_sides_all_float(self):
        result = get_poly_type(2.2, 3.2, 2.2, 3.2)
        self.assertEqual(result, 'rectangle')

    # Invalid Sides
    def test_get_poly_sides_invalid(self):
        result = get_poly_type(1, 2, 3, 5)
        self.assertEqual(result, 'invalid')

    def test_get_poly_sides_invalid_neg(self):
        result = get_poly_type(1, -2, 3, 4)
        self.assertEqual(result, 'invalid')

    def test_get_poly_sides_invalid_char(self):
        result = get_poly_type(2, 'a', 2, 3)
        self.assertEqual(result, 'invalid')

    # List Sides
    def test_get_poly_square_sides_list(self):
        result = get_poly_type([2, 2, 2, 2])
        self.assertEqual(result, 'square')

    def test_get_poly_rect_sides_list(self):
        result = get_poly_type([2, 3, 2, 3])
        self.assertEqual(result, 'rectangle')

    # Tuple Sides
    def test_get_poly_square_sides_tuple(self):
        result = get_poly_type((2, 2, 2, 2))
        self.assertEqual(result, 'square')

    def test_get_poly_rect_sides_tuple(self):
        result = get_poly_type((2, 3, 2, 3))
        self.assertEqual(result, 'rectangle')

    # Dict Sides
    def test_get_poly_square_sides_dict(self):
        result = get_poly_type({'a': 2, 'b': 2, 'c': 2, 'd': 2})
        self.assertEqual(result, 'square')

    def test_get_poly_rect_sides_dict(self):
        result = get_poly_type({'a': 2, 'b': 3, 'c': 2, 'd': 3})
        self.assertEqual(result, 'rectangle')


    # Int Angles
    def test_get_poly_square_angles_all_int(self):
        result = get_poly_type(90, 90, 90, 90, True)
        self.assertEqual(result, 'square')

    def test_get_poly_rhombus_angles_all_int(self):
        result = get_poly_type(135, 45, 135, 45, True)
        self.assertEqual(result, 'rhombus')

    def test_get_poly_disconnect_large_angles_all_int(self):
        result = get_poly_type(91, 91, 91, 91, True)
        self.assertEqual(result, 'disconnected')

    def test_get_poly_disconnect_bad_angles_all_int(self):
        result = get_poly_type(80, 100, 90, 90, True)
        self.assertEqual(result, 'disconnected')
