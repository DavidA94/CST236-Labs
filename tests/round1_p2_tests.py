"""
Test for source.source2
"""
from unittest import TestCase
from source.dg import diagnose

class TestRound1Test2(TestCase):

    def test_diagnose_alert_all(self):
        d = diagnose()
        d.add_error("A", "Error 1, module A")
        d.add_error("B", "Error 2, module B")
        d.add_error("B", "Error 3, module B")
        d.add_error("C", "Error 4, module C")
        result = d.get_errors()

        expected_result = {'A': ["Error 1, module A"],
                           'B': ["Error 2, module B",
                                 "Error 3, module B"],
                           'C': ["Error 4, module C"]}

        self.assertEqual(result, expected_result)

    def test_diagnose_alert_A(self):
        d = diagnose()
        d.add_error("A", "Error 1, module A")
        d.add_error("B", "Error 2, module B")
        d.add_error("B", "Error 3, module B")
        d.add_error("C", "Error 4, module C")
        result = d.get_errors('A')

        expected_result = {'A': ["Error 1, module A"]}

        self.assertEqual(result, expected_result)

    def test_diagnose_alert_B(self):
        d = diagnose()
        d.add_error("A", "Error 1, module A")
        d.add_error("B", "Error 2, module B")
        d.add_error("B", "Error 3, module B")
        d.add_error("C", "Error 4, module C")
        result = d.get_errors('B')

        expected_result = {'B': ["Error 2, module B",
                                 "Error 3, module B"]}

        self.assertEqual(result, expected_result)

    def test_diagnose_alert_C(self):
        d = diagnose()
        d.add_error("A", "Error 1, module A")
        d.add_error("B", "Error 2, module B")
        d.add_error("B", "Error 3, module B")
        d.add_error("C", "Error 4, module C")
        result = d.get_errors('C')

        expected_result = {'C': ["Error 4, module C"]}

        self.assertEqual(result, expected_result)

    def test_diagnose_alert_no_error(self):
        d = diagnose()
        result = d.get_errors()

        self.assertEqual(result, None)

    
