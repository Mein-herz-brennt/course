import unittest
from func import function
from math import log2


class MyTestCase(unittest.TestCase):
    def test_01_equal(self):
        x = 0
        eps = 1
        value = function(x, eps)
        expected = 0
        self.assertEqual(value, expected)

    def test_02_equal(self):
        x = 0.1
        eps = 1
        value = function(x, eps)
        expected = 0
        self.assertEqual(value, expected)

    def test_03_equal(self):
        x = 0.5
        exp = 0.1
        value = function(x, exp)
        expected = 1.0833333333333333
        self.assertEqual(value, expected)

    def test_04_equal(self):
        x = 0.5
        exp = 0.0001
        value = function(x, exp)
        expected = 1.0985882823773445
        self.assertEqual(value, expected)

    def test_05_is_not_none(self):
        x = 0
        eps = 1
        value = function(x, eps)
        self.assertIsNotNone(value)

    def test_06_true(self):
        x = 0.1
        exp = 0.01
        expected = log2((1 - x)/(1 + 2))
        value = function(x, exp)
        self.assertTrue(expected < value)

    def test_07_equal(self):
        x = -0.3
        exp = 0.1
        value = function(x, exp)
        expected = 0
        self.assertEqual(value, expected)


if __name__ == '__main__':
    unittest.main()
