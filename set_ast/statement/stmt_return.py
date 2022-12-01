from set_ast.node import Node


class StmtReturn(Node):

    def __init__(self, expression):
        self.expression = expression

    def execute(self, env=None):
        env.close_scope()
        return self.expression.execute(env)

    def __str__(self):
        return "while"
