import unittest

from quaternions.base import Quaternion


class QuaternionTest(unittest.TestCase):
    def setUp(self):
        self.a = Quaternion(1, 2, -5, 20)
        self.b = Quaternion(0, 4, 13, 2)

    def test_read_only(self):
        with self.assertRaises(AttributeError):
            self.a.n = 0

        with self.assertRaises(AttributeError):
            self.a.n_i = 0
        
        with self.assertRaises(AttributeError):
            self.a.n_j = 0
        
        with self.assertRaises(AttributeError):
            self.a.n_k = 0

    def test_add(self):
        a_plus_b = Quaternion(1, 6, 8, 22)
        self.assertEquals(self.a + self.b, a_plus_b)

    def test_mult(self):
        a_times_b = Quaternion(17, -266, 89, 48)
        self.assertEquals(self.a * self.b, a_times_b)

    def test_abs(self):
        abs_a = 430
        abs_b = 189
        self.assertEquals(abs(self.a), abs_a)
        self.assertEquals(abs(self.b), abs_b)

    def test_equals(self):
        a_copy = Quaternion(1, 2, -5, 20)
        self.assertEquals(self.a, a_copy)
