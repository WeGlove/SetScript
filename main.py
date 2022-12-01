from Lexer import Lexer
from Parser import Parser


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        print(set(set()))
        tokens = Lexer.lex(f)
        print(tokens)
        ast = Parser.parse(tokens)
        print(ast)
        env = ast.execute()[0]
        print(env)
