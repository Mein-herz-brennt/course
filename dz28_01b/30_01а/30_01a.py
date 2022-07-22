import unittest
from func import func


class MyTestCase(unittest.TestCase):
    def test_01_equal(self):
        x = 0
        eps = 1
        value = func(x, eps)
        expected = 1
        print(f"1 -> {value} ==> {expected}")
        self.assertEqual(value, expected)

    def test_02_equal(self):
        x = 0.1
        eps = 1
        value = func(x, eps)
        expected = 0.9
        print(f"2 -> {value} ==> {expected}")
        self.assertEqual(value, expected)

    def test_03_equal(self):
        x = 0.5
        exp = 0.1
        value = func(x, exp)
        expected = 0.6875
        print(f"3 -> {value} ==> {expected}")
        self.assertEqual(value, expected)

    def test_04_equal(self):
        x = 0.5
        exp = 0.0001
        value = func(x, exp)
        expected = 0.66668701171875
        print(f"4 -> {value} ==> {expected}")
        self.assertEqual(value, expected)

    def test_05_is_not_none(self):
        x = 0
        eps = 1
        value = func(x, eps)
        print(f"5 -> {value}")
        self.assertIsNotNone(value)

    def test_06_true(self):
        x = 0.1
        exp = 0.01
        expected = 1/(1 + x)
        value = func(x, exp)
        print(f"6 -> {value} ==> {expected}")
        self.assertTrue(expected > value)

    def test_07_equal(self):
        x = -0.5
        exp = 0.1
        value = func(x, exp)
        expected = 1.9375
        print(f"7 -> {value} ==> {expected}")
        self.assertEqual(value, expected)


if __name__ == '__main__':
    unittest.main()
