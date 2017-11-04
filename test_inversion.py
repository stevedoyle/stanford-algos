from inversion import count_inv
import unittest


class TestInversion(unittest.TestCase):

    def test_count_inv_1(self):
        data = [1, 20, 6, 4, 5]
        self.assertEqual(5, count_inv(data))

    def test_count_inv_2(self):
        data = [1, 9, 6, 4, 5]
        self.assertEqual(5, count_inv(data))

    def test_count_inv_3(self):
        data = [1, 5, 3, 7, 4, 8, 9, 5, 4, 2, 6, 1]
        self.assertEqual(35, count_inv(data))
