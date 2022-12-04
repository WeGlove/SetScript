from Lexer import Lexer
from Parser import Parser


if __name__ == "__main__":
    path = "test.txt"
    tokens = Lexer.lex(path)
    print(tokens)
    ast = Parser.parse(tokens)
    print(ast)
    env = ast.execute()[0]
    print(env)
