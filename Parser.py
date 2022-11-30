from set_ast.expression.set import Set
from set_ast.statement.assignment import Assignment
from set_ast.expression.Variable import Variable
from set_ast.expression.operation.union import Union
from set_ast.expression.operation.intersection import Intersection
from set_ast.expression.operation.difference import Difference
from set_ast.expression.operation.equality import Equality
from set_ast.statement.while_loop import WhileLoop
from set_ast.set_ast import SetAst


class Parser:

    @staticmethod
    def parse_set(tokens):
        token_open = tokens[0]
        if token_open.content != "{":
            raise ValueError()
        tokens = tokens[1:]

        elements = []
        comma_count = 0
        while True:
            next_token = tokens[0]

            if next_token.content == ",":
                if comma_count > 0:
                    raise ValueError("Too many commas in set")
                if len(elements) == 0:
                    raise ValueError()

                comma_count += 1
                tokens = tokens[1:]
            elif next_token.content == "}":
                return Set(elements), tokens[1:]
            else:
                comma_count = 0
                element, tokens = Parser.parse_expression(tokens)
                elements.append(element)

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
        if next_token.content == "|":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Union(lhs, rhs), tokens
        elif next_token.content == "&":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Intersection(lhs, rhs), tokens
        elif next_token.content == "-":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Difference(lhs, rhs), tokens
        elif next_token.content == "==":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return Equality(lhs, rhs), tokens
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
    def parse_while(tokens):
        token_while = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]
        condition, tokens = Parser.parse_expression(tokens)
        token_bracket_close = tokens[0]
        token_curl_open = tokens[1]
        tokens = tokens[2:]
        statements = []
        while tokens[0].content != "}":
            statement, tokens = Parser.parse_statement(tokens)
            statements.append(statement)
        tokens = tokens[1:]

        return WhileLoop(condition, statements), tokens

    @staticmethod
    def parse_statement(tokens):
        if tokens[0].content == "while":
            assignment, tokens = Parser.parse_while(tokens)
        else:
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
