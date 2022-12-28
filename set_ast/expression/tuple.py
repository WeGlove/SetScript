from set_ast.node import Node
from set_ast.Environment import Environment


class Tuple(Node):

    def __init__(self,  set_class, elements):
        self.elements = elements
        self.set_class = set_class

    def execute(self, env: Environment):
        if len(self.elements) == 0:
            return env, frozenset()

        env, res_set = self.elements[0].execute(env)

        for element in self.elements[1:]:
            env, val = element.execute(env)
            res_set = frozenset([frozenset([res_set]), frozenset([res_set, val])])

        return env, res_set

    def __str__(self):
        s = "<"
        for element in self.elements:
            s += element
        return s + ">"
