from set_ast.node import Node
from set_ast.Environment import Environment


class Difference(Node):

    def __init__(self, set_class, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.set_class = set_class

    def execute(self, env: Environment):
        env, lhs_val = self.lhs.execute(env)
        env, rhs_val = self.rhs.execute(env)

        return env, lhs_val.differnece(rhs_val)
