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


class PlainExpFactory(ExpressionFactory):

    def Power(self, X):
        return Power(X)

    def FunctionCall(self, name, expressions):
        return FunctionCall(name, expressions)

    def Qualified(self, names):
        return Qualified(names)

    def Variable(self, name):
        return Variable(name)

    def Number(self, num):
        return Number(num)

    def Set(self, elements):
        return Set(elements)

    def Tuple(self, elements):
        return Tuple(elements)

    def BigUnion(self, X):
        return BigUnion(X)

    def BigIntersection(self, X):
        return BigIntersection

    def Difference(self, X, Y):
        return  Difference

    def Equality(self, X, Y):
        return Equality

    def In(self, x, X):
        return In

    def InEquality(self, X, Y):
        return InEquality

    def Intersection(self, X, Y):
        return Intersection

    def Union(self, X, Y):
        return Union
