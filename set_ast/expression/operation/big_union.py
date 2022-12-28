from set_ast.node import Node
from set_ast.Environment import Environment
from set_math import SetMath


class BigUnion(Node):

    def __init__(self,  set_class, expr):
        self.expr = expr
        self.set_class = set_class

    def execute(self, env: Environment):
        env, expr_set = self.expr.execute(env)
        return env, SetMath.big_union(expr_set)
