from set_ast.set_ast import SetAst
from .StatementParser import StatementParser


class Parser:

    @staticmethod
    def parse(tokens):
        statements = []
        while len(tokens) > 0:
            statement, tokens = StatementParser.parse_statement(tokens)
            statements.append(statement)

        return SetAst(statements)
