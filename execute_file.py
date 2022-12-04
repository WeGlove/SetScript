from Lexer import Lexer
from Parser import Parser


def excecute_file(path, env):
    with open(path, "r") as f:
        tokens = Lexer.lex(f)
        ast = Parser.parse(tokens)
        env, val = ast.execute(env)
        return env, val
