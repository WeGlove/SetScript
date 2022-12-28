from set_math import SetMath
from sets.AbstractSet import AbstractSet


class NormalSet(AbstractSet):

    def __init__(self, elements=None):
        if elements is None:
            elements = []
        elements = [element.fset for element in elements]
        self.fset = frozenset(elements)

    def union(self, Y):
        return NormalSet.from_fset(self.fset.union(Y.fset))

    def difference(self, Y):
        return NormalSet.from_fset(self.fset.difference(Y.fset))

    def intersection(self, Y):
        return NormalSet.from_fset(self.fset.intersection(Y.fset))

    def is_in(self, Y):
        return Y in self.fset

    def big_union(self):
        return NormalSet(SetMath.big_union(self.fset))

    def big_intersection(self):
        return NormalSet(SetMath.big_intersection(self.fset))

    def is_equal(self, Y):
        return NormalSet.true() if self.fset == Y.fset else NormalSet.false()

    @staticmethod
    def number(num):
        res_set = NormalSet.empty()
        for i in range(num):
            res_set = NormalSet([res_set]).union(res_set)
        return res_set

    @staticmethod
    def from_fset(fest):
        s = NormalSet.empty()
        s.fset = fest
        return s

    @staticmethod
    def empty():
        return NormalSet()

    @staticmethod
    def true():
        return NormalSet.empty()

    @staticmethod
    def false():
        return NormalSet([NormalSet.empty()])

    def cardinality(self):
        return len(self.fset)

    def __str__(self):
        return "Normal Set of cardinality: " + str(self.cardinality())

    def __repr__(self):
        return self.__str__()


