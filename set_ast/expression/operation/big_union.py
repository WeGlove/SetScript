from set_ast.node import Node
from set_ast.Environment import Environment


class BigUnion(Node):

    def __init__(self, expr):
        self.expr = expr

    def execute(self, env: Environment):
        env, expr_set = self.expr.execute(env)
        elements = []
        for x in expr_set:
            for y in x:
                elements.append(y)
        return env, frozenset(elements)