from set_ast.node import Node
from set_ast.Environment import Environment


class SetAst(Node):

    def __init__(self, set_class, statements):
        self.statements = statements
        self.set_class = set_class

    def execute(self, env=None):
        if env is None:
            env = Environment()
        for statement in self.statements:
            env, _ = statement.execute(env)
            if env.return_flag:
                break
        return env, None
