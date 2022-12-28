from set_ast.node import Node
from set_ast.Environment import Environment


class Namespace(Node):

    def __init__(self,  set_class, identifier, statements):
        self.identifier = identifier
        self.statements = statements
        self.set_class = set_class

    def execute(self, env: Environment):
        new_env = Environment()
        env.set_value(self.identifier.content, new_env)
        for statement in self.statements:
            new_env, _ = statement.execute(new_env)

        return env, frozenset()

    def __str__(self):
        return f"Namespace: {self.identifier}"
