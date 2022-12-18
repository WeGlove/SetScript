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

    @staticmethod
    def list_to_n_tuple(elements):
        res_set = elements[0]

        for element in elements[1:]:
            res_set = frozenset([frozenset([res_set]), frozenset([res_set, element])])

        return res_set

    @staticmethod
    def nat_num_to_set(X):
        res_set = frozenset()
        for i in range(X):
            res_set = frozenset([res_set]).union(res_set)
        return res_set

    @staticmethod
    def string_to_set(s):
        elements = []
        for char in s:
            print(char, ord(char))
            elements.append(SetMath.nat_num_to_set(ord(char)))
            print("Yo")

        print("Yee")
        res_tuple = SetMath.list_to_n_tuple(elements)
        return res_tuple

    @staticmethod
    def tuple_to_list(tup):
        while tup != frozenset():
            tup = SetMath.big_union(tup)