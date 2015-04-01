"""
Test for source.source1
"""
from unittest import TestCase
from source.source1 import get_triangle_type

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    ## Added by David Antonucci
    def test_get_triangle_isosceles_all_int(self):
        result = get_triangle_type(1, 1, 3)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_invalid_param(self):
        result = get_triangle_type(1, 'a', 3)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_invalid_small(self):
        result = get_triangle_type(1, -1, 3)
        self.assertEqual(result, 'invalid')

    #float
    def test_get_triangle_equilateral_all_float(self):
        result = get_triangle_type(1.0, 1.0, 1.0)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_float(self):
        result = get_triangle_type(1.0, 2.0, 3.0)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_all_float(self):
        result = get_triangle_type(1.0, 1.0, 3.0)
        self.assertEqual(result, 'isosceles')


    #list 
    def test_get_triangle_equilateral_list(self):
        result = get_triangle_type([1,1,1])
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_list(self):
        result = get_triangle_type([1,2,3])
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_list(self):
        result = get_triangle_type([1, 1, 3])
        self.assertEqual(result, 'isosceles')

    #tuple
    def test_get_triangle_equilateral_tuple(self):
        result = get_triangle_type((1,1,1))
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_tuple(self):
        result = get_triangle_type((1,2,3))
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_tuple(self):
        result = get_triangle_type((1, 1, 3))
        self.assertEqual(result, 'isosceles')
        

    #dict
    def test_get_triangle_equilateral_dict(self):
        result = get_triangle_type({'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_dict(self):
        result = get_triangle_type({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(result, 'scalene')

    def test_get_triangle_isosceles_dict(self):
        result = get_triangle_type({'a': 1, 'b': 1, 'c': 3})
        self.assertEqual(result, 'isosceles')
