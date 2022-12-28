from set_ast.set_ast import SetAst
from .StatementParser import StatementParser


class Parser:

    def __init__(self, factory):
        self.factory = factory

    def parse(self, tokens):
        statements = []
        statement_parser = StatementParser(self.factory)
        while len(tokens) > 0:
            statement, tokens = statement_parser.parse_statement(tokens)
            statements.append(statement)

        return SetAst(statements)
