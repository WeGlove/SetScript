from set_ast.node import Node
from set_ast.Environment import Environment


class Qualified(Node):

    def __init__(self,  set_class, name_tokens):
        self.name_tokens = name_tokens
        self.names = [token.content for token in self.name_tokens]
        self.set_class = set_class

    def execute(self, env: Environment):
        val = env.get_value(self.names)
        return env, val

    def __str__(self):
        return str(self.name_tokens)
