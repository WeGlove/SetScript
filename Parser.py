from set_ast.expression.set import Set
from set_ast.statement.assignment import Assignment
from set_ast.expression.Variable import Variable
from set_ast.expression.operation.union import Union
from set_ast.expression.operation.intersection import Intersection
from set_ast.expression.operation.difference import Difference
from set_ast.set_ast import SetAst


class Parser:

    @staticmethod
    def parse_set(tokens):
        token_open = tokens[0]
        if token_open.content != "{":
            raise ValueError()
        tokens = tokens[1:]

        elements = []
        while True:
            next_token = tokens[0]

            if next_token.content == ",":
                if len(elements) < 0:
                    raise ValueError()
                tokens = tokens[1:]
                element, tokens = Parser.parse_set(tokens)
                elements.append(element)
                return Set(elements), tokens
            elif next_token.content == "{":
                if len(elements) == 0:
                    element, tokens = Parser.parse_set(tokens)
                    next_token = tokens[0]
                    if next_token.content != "}":
                        raise ValueError()
                    elements.append(element)
                    return Set(elements), tokens[1:]
                else:
                    raise ValueError()
            elif next_token.content == "}":
                return Set(elements), tokens[1:]
            else:
                raise ValueError()

    @staticmethod
    def parse_expression(tokens):
        next_token = tokens[0]

        if next_token.content == "{":
            lhs, tokens = Parser.parse_set(tokens)
        elif next_token.type == "Word":
            lhs, tokens = Variable(next_token.content), tokens[1:]
        else:
            raise ValueError()

        next_token = tokens[0]
        if next_token.content == "+":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Union(lhs, rhs), tokens
        elif next_token.content == "*":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Intersection(lhs, rhs), tokens
        elif next_token.content == "/":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Difference(lhs, rhs), tokens
        else:
            return lhs, tokens

    @staticmethod
    def parse_assignment(tokens):
        variable = tokens[0]
        if variable.type != "Word":
            raise ValueError("Expression variable is not a Word")

        assign = tokens[1]
        if assign.content != "=":
            raise ValueError("Expression variable is not a Word")
        expression, tokens = Parser.parse_expression(tokens[2:])
        assignment = Assignment(Variable(variable.content), expression)
        return assignment, tokens

    @staticmethod
    def parse_statement(tokens):
        assignment, tokens = Parser.parse_assignment(tokens)
        token = tokens[0]
        if token.content == ";":
            return assignment, tokens[1:]
        else:
            raise ValueError("Missing Semicolon")

    @staticmethod
    def parse(tokens):
        statements = []
        while len(tokens) > 0:
            statement, tokens = Parser.parse_statement(tokens)
            statements.append(statement)

        return SetAst(statements)
