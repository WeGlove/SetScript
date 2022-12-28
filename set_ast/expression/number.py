from set_ast.node import Node
from set_ast.Environment import Environment


class Number(Node):

    def __init__(self,  set_class, number):
        self.number = number
        self.set_class = set_class

    def execute(self, env: Environment):
        return env, self.set_class.number(self.number)

    def __str__(self):
        return "Number"
