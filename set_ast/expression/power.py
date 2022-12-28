from set_ast.node import Node
from set_ast.Environment import Environment
from set_math import SetMath


class Power(Node):

    def __init__(self,  set_class, expr):
        self.expr = expr
        self.set_class = set_class

    def execute(self, env: Environment):
        env, val = self.expr.execute(env)

        out = SetMath.power_set(val)

        return env, out

    def __str__(self):
        return "P(...)"
