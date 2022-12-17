from set_ast.node import Node
from set_ast.Environment import Environment


class Empty(Node):

    def execute(self, env: Environment):
        return env, frozenset()

    def __str__(self):
        return "Empty"
