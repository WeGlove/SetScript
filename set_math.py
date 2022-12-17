class SetMath:

    @staticmethod
    def big_union(X):
        elements = []
        for x in X:
            for y in x:
                elements.append(y)
        return frozenset(elements)

    @staticmethod
    def build_number(X):
        num = 0
        while X != frozenset():
            X = SetMath.big_union(X)
            X = SetMath.big_union(X)
            num += 1
        return num
