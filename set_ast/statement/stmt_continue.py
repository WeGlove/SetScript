from set_ast.node import Node
from set_ast.Environment import Environment


class StmtContinue(Node):

    def execute(self, env: Environment):
        env.continue_flag = True
        return env, frozenset()

    def __str__(self):
        return "return"
