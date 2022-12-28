from set_ast.node import Node
from set_ast.Environment import Environment


class StmtImport(Node):

    def __init__(self,  set_class, ast):
        self.ast = ast
        self.set_class = set_class

    def execute(self, env: Environment):
        env, val = self.ast.execute(env)
        return env, val

    def __str__(self):
        return "import"
