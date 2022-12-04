from set_ast.node import Node
from set_ast.Environment import Environment


class BigUnion(Node):

    def __init__(self, expr):
        self.expr = expr

    def execute(self, env: Environment):
        res = frozenset()
        env, expr_set = self.expr.execute(env)
        for x in expr_set:
            res = res | expr_set
        return env, res