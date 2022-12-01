from set_ast.node import Node
from set_ast.Environment import Environment


class SetAst(Node):

    def __init__(self, statements):
        self.statements = statements

    def execute(self, env=None):
        if env is None:
            env = Environment()
        for statement in self.statements:
            env, _ = statement.execute(env)
        return env, None
