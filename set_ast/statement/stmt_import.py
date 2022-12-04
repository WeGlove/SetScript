from set_ast.node import Node
from set_ast.Environment import Environment


class StmtImport(Node):

    def __init__(self, path):
        self.path = path

    def execute(self, env: Environment):
        import execute_file
        env, val = execute_file.excecute_file(self.path, env)
        return env, val

    def __str__(self):
        return "Function: " + self.identifier
