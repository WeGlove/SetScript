class SetMath:

    @staticmethod
    def big_union(X):
        elements = []
        for x in X:
            for y in x:
                elements.append(y)
        return frozenset(elements)
