from set_ast.node import Node
from set_ast.Environment import Environment


class StmtContinue(Node):

    def __init__(self, set_class, ):
        self.set_class = set_class

    def execute(self, env: Environment):
        env.continue_flag = True
        return env, frozenset()

    def __str__(self):
        return "return"
