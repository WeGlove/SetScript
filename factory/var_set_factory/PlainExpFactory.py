from factory.expression_factory import ExpressionFactory
from set_ast.expression.power import Power
from set_ast.expression.function_call import FunctionCall
from set_ast.expression.qualified import Qualified
from set_ast.expression.set import Set
from set_ast.expression.tuple import Tuple
from set_ast.expression.number import Number
from set_ast.expression.operation.big_union import BigUnion
from set_ast.expression.operation.big_intersection import BigIntersection
from set_ast.expression.operation.binary.union import Union
from set_ast.expression.operation.binary.intersection import Intersection
from set_ast.expression.operation.binary.In import In
from set_ast.expression.operation.binary.difference import Difference
from set_ast.expression.operation.binary.equality import Equality
from set_ast.expression.operation.binary.inequality import InEquality
from set_ast.expression.Variable import Variable


class VarSetExpFactory(ExpressionFactory):

    def __init__(self, set_class):
        self.set_class = set_class

    def Power(self, X):
        return Power(self.set_class, X)

    def FunctionCall(self, name, expressions):
        return FunctionCall(self.set_class, name, expressions)

    def Qualified(self, names):
        return Qualified(self.set_class, names)

    def Variable(self, name):
        return Variable(self.set_class, name)

    def Number(self, num):
        return Number(self.set_class, num)

    def Set(self, elements):
        return Set(self.set_class, elements)

    def Tuple(self, elements):
        return Tuple(self.set_class, elements)

    def BigUnion(self, X):
        return BigUnion(self.set_class, X)

    def BigIntersection(self, X):
        return BigIntersection(self.set_class, X)

    def Difference(self, X, Y):
        return  Difference(self.set_class, X,Y)

    def Equality(self, X, Y):
        return Equality(self.set_class, X,Y)

    def In(self, x, X):
        return In(self.set_class, x,X)

    def InEquality(self, X, Y):
        return InEquality(self.set_class, X,Y)

    def Intersection(self, X, Y):
        return Intersection(self.set_class, X,Y)

    def Union(self, X, Y):
        return Union(self.set_class, X, Y)
