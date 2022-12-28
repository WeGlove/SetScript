from set_ast.node import Node
from set_ast.Environment import Environment


class BigIntersection(Node):

    def __init__(self, expr):
        self.expr = expr

    def execute(self, env: Environment):
        env, expr_set = self.expr.execute(env)
        union = []
        for x in expr_set:
            for y in x:
                union.append(y)

        for x in expr_set:
            elements = []
            for y in x:
                elements.append(y)
            union = [el for el in union if el in elements]
        return env, frozenset(union)
