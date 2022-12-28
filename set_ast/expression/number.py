from set_ast.node import Node
from set_ast.Environment import Environment


class Number(Node):

    def __init__(self,  set_class, number):
        self.number = number
        self.set_class = set_class

    def execute(self, env: Environment):
        res = frozenset()
        for i in range(self.number):
            res = frozenset([res, frozenset([res])])

        return env, res

    def __str__(self):
        return "Number"
