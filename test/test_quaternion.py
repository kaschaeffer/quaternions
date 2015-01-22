import math
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

    def test_sub(self):
        a_minus_b = Quaternion(1, -2, -18, 18)
        self.assertEquals(self.a - self.b, a_minus_b)

    def test_mult(self):
        a_times_b = Quaternion(17, -266, 89, 48)
        self.assertEquals(self.a * self.b, a_times_b)

    def test_div(self):
        # TODO
        pass

    def test_abs(self):
        abs_a = math.sqrt(430)
        abs_b = math.sqrt(189)
        self.assertAlmostEquals(abs(self.a), abs_a)
        self.assertAlmostEquals(abs(self.b), abs_b)

    def test_equals(self):
        a_copy = Quaternion(1, 2, -5, 20)
        self.assertEquals(self.a, a_copy)

    def test_not_equals(self):
        a_copy = Quaternion(1, 2, -5, 20)
        c = Quaternion(9, -100, 754, 1)
        self.assertFalse(self.a != a_copy)
        self.assertTrue(self.a != c)

    # TODO decide what behavior we expect for >, <, >=, <=
    # look into functools, @total_ordering...

    def test_pos(self):
        self.assertEquals(self.a, +self.a)

    def test_neg(self):
        a_neg = Quaternion(-1, -2, 5, -20)
        self.assertEquals(a_neg, -self.a)

    # __invert__?

    def test_round(self):
        pass

    def test_pow(self):
        # TODO
        pass

    # think __floor__, __ceiling__, __trunc__ don't make sense...
    # similarly with __floordiv__, __truediv__
    # NOTE: what's the difference between __truediv__ and __div__

    # skip __mod__, __divmod__

    # might want to define __radd__, __rsub__, etc... for doing
    # arithmetic with reals, complex #s

    def test_conjugate(self):
        a_conjugate = Quaternion(1, -2, 5, -20)
        self.assertEquals(self.a.conjugate(), a_conjugate)

    def test_to_matrix(self):
        a_matrix = [
            [1 + 2j, -5 + 20j],
            [+5 - 20j, 1 - 2j],
        ]
        self.assertEquals(self.a.to_matrix(), a_matrix)

    # __format__ ?

    def test_nonzero(self):
        pass
        # test __nonzero__ ...
