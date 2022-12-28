from set_ast.node import Node
from set_ast.Environment import Environment


class Variable(Node):

    def __init__(self,  set_class, name):
        self.name = name
        self.set_class = set_class

    def execute(self, env: Environment):
        return env, env.get_value(self.name.names)

    def __str__(self):
        return f"Variable: {self.name.names}"
