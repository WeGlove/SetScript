from set_ast.node import Node


class Set(Node):

    def __init__(self, elements):
        self.elements = elements

    def execute(self, env=None):
        elements = []
        for element in self.elements:
            env, val = element.execute(env)
            elements.append(val)

        return env, set(elements)

    def __str__(self):
        s = "{"
        for element in self.elements:
            s += element
        return s + "}"