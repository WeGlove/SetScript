from set_ast.node import Node
from set_ast.Environment import Environment


class StmtReturn(Node):

    def __init__(self, set_class,  expression):
        self.expression = expression
        self.set_class = set_class

    def execute(self, env: Environment):
        env, val = self.expression.execute(env)
        env.return_flag = True
        return env, val

    def __str__(self):
        return "return"
