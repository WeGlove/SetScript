from set_ast.node import Node


class SetAst(Node):

    def __init__(self, statements):
        self.statements = statements

    def execute(self, env=None):
        for statement in self.statements:
            env, _ = statement.execute(env)
        return env, None
