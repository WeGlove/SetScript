from set_ast.node import Node
from set_ast.Environment import Environment


class StmtContinue(Node):

    def __init__(self, expression):
        self.expression = expression

    def execute(self, env: Environment):
        env, val = self.expression.execute(env)
        env.continue_flag = True
        return env, val

    def __str__(self):
        return "return"
