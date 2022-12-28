from set_math import SetMath


class NormalSet:

    def __init__(self, elements):
        self.elements = elements

    def union(self, Y):
        return NormalSet(self.elements.union(Y.elements))

    def difference(self, Y):
        return NormalSet(self.elements.difference(Y.elements))

    def intersection(self, Y):
        return NormalSet(self.elements.intersection(Y.elements))

    def is_in(self, Y):
        return Y in self.elements

    def big_union(self):
        return NormalSet(SetMath.big_union(self.elements))

    def big_intersection(self):
        return NormalSet(SetMath.big_intersection(self.elements))
