from set_ast.node import Node
from set_ast.Environment import Environment


class StmtImport(Node):

    def __init__(self, path_tokens):
        self.path_tokens = path_tokens
        self.path = ""
        for token in self.path_tokens:
            self.path += token.content

    def execute(self, env: Environment):
        import execute_file
        env, val = execute_file.excecute_file(self.path, env)
        return env, val

    def __str__(self):
        return "import: " + self.path
