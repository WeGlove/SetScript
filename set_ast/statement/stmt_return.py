from set_ast.node import Node
from set_ast.Environment import Environment


class StmtReturn(Node):

    def __init__(self, expression):
        self.expression = expression

    def execute(self, env: Environment):
        env.close_scope()
        return self.expression.execute(env)

    def __str__(self):
        return "while"
