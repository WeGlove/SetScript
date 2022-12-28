from set_ast.node import Node
from set_ast.Environment import Environment


class Set(Node):

    def __init__(self, elements):
        self.elements = elements

    def execute(self, env: Environment):
        elements = []
        for element in self.elements:
            env, val = element.execute(env)
            elements.append(val)

        return env, frozenset([])

    def __str__(self):
        s = "{"
        for element in self.elements:
            s += element
        return s + "}"