from Lexer import Lexer
from parsing.Parser import Parser


def excecute_file(path, env):
    tokens = Lexer.lex(path)
    ast = Parser.parse(tokens)
    env, val = ast.execute(env)
    return env, val
