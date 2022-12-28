from Lexer import Lexer
from parsing.Parser import Parser


def compile(path, factory):
    tokens = Lexer.lex(path)
    parser = Parser(factory)
    ast = parser.parse(tokens)
    return ast
