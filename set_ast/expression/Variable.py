from set_ast.node import Node
from set_ast.Environment import Environment


class Variable(Node):

    def __init__(self, name):
        self.name = name

    def execute(self, env: Environment):
        return env, env.get_value(self.name)

    def __str__(self):
        return f"Variable: {self.name}"