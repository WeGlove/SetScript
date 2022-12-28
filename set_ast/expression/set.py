from set_ast.node import Node
from set_ast.Environment import Environment


class Set(Node):

    def __init__(self,  set_class, elements):
        self.elements = elements
        self.set_class = set_class

    def execute(self, env: Environment):
        elements = []
        for element in self.elements:
            env, val = element.execute(env)
            elements.append(val)

        return env, self.set_class()

    def __str__(self):
        s = "{"
        for element in self.elements:
            s += element
        return s + "}"