from set_ast.node import Node
from set_ast.Environment import Environment


class In(Node):

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def execute(self, env: Environment):
        env, lhs_val = self.lhs.execute(env)
        env, rhs_val = self.rhs.execute(env)

        return env, frozenset() if lhs_val in rhs_val else frozenset([frozenset()])