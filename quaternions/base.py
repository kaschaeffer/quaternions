import math

class Quaternion(object):
    def __init__(self, n, n_i, n_j, n_k):
        self._n   = n
        self._n_i = n_i
        self._n_j = n_j
        self._n_k = n_k

    @property
    def n(self):
        return self._n

    @property
    def n_i(self):
        return self._n_i

    @property
    def n_j(self):
        return self._n_j

    @property
    def n_k(self):
        return self._n_k

    def __repr__(self):
        quaternion_repr = "{n_i}i + {n_j}j + {n_k}k + {n}".format(n=self.n, 
                                                                  n_i=self.n_i, 
                                                                  n_j=self.n_j, 
                                                                  n_k=self.n_k)
        return quaternion_repr
    def __add__(self, other):
        if other.__class__ == Quaternion:
            n   = self.n + other.n
            n_i = self.n_i + other.n_i
            n_j = self.n_j + other.n_j
            n_k = self.n_k + other.n_k
            added = Quaternion(n, n_i, n_j, n_k)
            return added

    def __mul__(self, other):
        if other.__class__ == Quaternion:
            n = ((self.n * other.n) - (self.n_i *other.n_i) -
                (self.n_j * other.n_j) - (self.n_k * other.n_k))
            n_i = ((self.n * other.n_i) + (self.n_i * other.n) + 
                  (self.n_j * other.n_k) - (self.n_k * other.n_j))
            n_j = ((self.n * other.n_j) + (self.n_j * other.n) + 
                  (self.n_k * other.n_i) - (self.n_i * other.n_k))
            n_k = ((self.n * other.n_k) + (self.n_k * other.n) + 
                  (self.n_i * other.n_j) - (self.n_j * other.n_i))
            multiplied = Quaternion(n, n_i, n_j, n_k)
            return multiplied
        # TODO add utility methods for adding real and
        # complex numbers

    def __key(self):
        return (self.n, self.n_i, self.n_j, self.n_k)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())

    def __abs__(self):
        self_abs = math.sqrt(self.n**2 + self.n_i**2 + self.n_j**2 + self.n_k**2)
        return self_abs
