import unittest
from func import func


class MyTestCase(unittest.TestCase):
    def test_01_equal(self):
        x = 0
        eps = 1
        value = func(x, eps)
        expected = 1
        self.assertEqual(value, expected)

    def test_02_equal(self):
        x = 0.1
        eps = 1
        value = func(x, eps)
        expected = 1
        self.assertEqual(value, expected)

    def test_03_equal(self):
        x = 0.5
        exp = 0.1
        value = func(x, exp)
        expected = 0.3203125
        self.assertEqual(value, expected)

    def test_04_equal(self):
        x = 0.5
        exp = 0.0001
        value = func(x, exp)
        expected = 0.29631948471069336
        self.assertEqual(value, expected)

    def test_05_is_not_none(self):
        x = 0
        eps = 1
        value = func(x, eps)
        self.assertIsNotNone(value)

    def test_06_true(self):
        x = 0.1
        exp = 0.01
        expected = 1/pow((1 + x), 3)
        value = func(x, exp)
        self.assertTrue(expected < value)

    def test_07_equal(self):
        x = -0.5
        exp = 0.1
        value = func(x, exp)
        expected = 7.91015625
        self.assertEqual(value, expected)


if __name__ == '__main__':
    unittest.main()
