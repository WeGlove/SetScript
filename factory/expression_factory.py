from abc import abstractmethod


class ExpressionFactory:

    @abstractmethod
    def Power(self, element):
        pass

    @staticmethod
    def FunctionCall(name, expr):
        pass

    @staticmethod
    def Qualified(names):
        pass

    @staticmethod
    def Variable(name):
        pass

    @staticmethod
    def Number(number):
        pass

    @staticmethod
    def Set(elements):
        pass

    @staticmethod
    def Tuple(elements):
        pass

    @staticmethod
    def BigUnion(element):
        pass

    @staticmethod
    def BigIntersection(element):
        pass

    @staticmethod
    def Difference(X, Y):
        pass

    @staticmethod
    def Equality(X, Y):
        pass

    @staticmethod
    def In(x, X):
        pass

    @staticmethod
    def InEquality(X, Y):
        pass

    @staticmethod
    def Intersection(X, Y):
        pass

    @staticmethod
    def Union(X, Y):
        pass