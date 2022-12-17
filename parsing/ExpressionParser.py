from set_ast.expression.power import Power
from set_ast.expression.function_call import FunctionCall
from set_ast.expression.qualified import Qualified
from set_ast.expression.number import Number
from set_ast.expression.set import Set
from set_ast.expression.tuple import Tuple
from set_ast.expression.operation.big_union import BigUnion
from set_ast.expression.operation.big_intersection import BigIntersection
from set_ast.expression.operation.binary.difference import Difference
from set_ast.expression.operation.binary.equality import Equality
from set_ast.expression.operation.binary.In import In
from set_ast.expression.operation.binary.inequality import InEquality
from set_ast.expression.operation.binary.intersection import Intersection
from set_ast.expression.operation.binary.union import Union
from parsing.ParsingUtils import ParsingUtils


class ExpressionParser:

    @staticmethod
    def parse_set(tokens):
        elements, tokens = ParsingUtils.parse_list(tokens, "{", "}", ",", ExpressionParser.parse_expression)
        return Set(elements), tokens

    @staticmethod
    def parse_Tuple(tokens):
        elements, tokens = ParsingUtils.parse_list(tokens, "<", ">", ",", ExpressionParser.parse_expression)
        return Tuple(elements), tokens

    @staticmethod
    def parse_function_call(tokens):
        identifier, tokens = ExpressionParser.parse_qualified(tokens)

        if identifier.names[-1] == "P":
            expressions, tokens = ParsingUtils.parse_list(tokens, "(", ")", ",", ExpressionParser.parse_expression)
            if len(expressions) != 1 or len(identifier.names) != 1:
                raise ValueError("Too many parameters in power set")
            return Power(expressions[0]), tokens

        expressions, tokens = ParsingUtils.parse_list(tokens, "(", ")", ",", ExpressionParser.parse_expression)
        return FunctionCall(identifier, expressions), tokens

    @staticmethod
    def parse_parentheses(tokens):
        token_open = tokens[0]
        expression, tokens = ExpressionParser.parse_expression(tokens[1:])
        token_close = tokens[0]

        return expression, tokens[1:]


    @staticmethod
    def parse_big_union(tokens):
        symbol = tokens[0]
        expr, tokens = ExpressionParser.parse_expression(tokens[1:])
        return BigUnion(expr), tokens

    @staticmethod
    def parse_big_intersection(tokens):
        symbol = tokens[0]
        expr, tokens = ExpressionParser.parse_expression(tokens[1:])
        return BigIntersection(expr), tokens

    @staticmethod
    def parse_expression(tokens):
        next_token = tokens[0]

        if next_token.content == "{":
            lhs, tokens = ExpressionParser.parse_set(tokens)
        elif next_token.content == "<":
            lhs, tokens = ExpressionParser.parse_Tuple(tokens)
        elif next_token.content == "(":
            lhs, tokens = ExpressionParser.parse_parentheses(tokens)
        elif next_token.type == "Identifier":
            qualified, q_tokens = ExpressionParser.parse_qualified(tokens)
            next_token = q_tokens[0]
            if next_token.content == "(":
                lhs, tokens = ExpressionParser.parse_function_call(tokens)
            else:
                lhs, tokens = ExpressionParser.parse_qualified(tokens)
        elif next_token.type == "Number":
            lhs = Number(int(next_token.content))
            tokens = tokens[1:]
        elif next_token.content == "&&":
            expr, tokens = ExpressionParser.parse_big_intersection(tokens)
            return expr, tokens
        elif next_token.content == "||":
            expr, tokens = ExpressionParser.parse_big_union(tokens)
            return expr, tokens
        else:
            raise ValueError(f"Unknown expression {next_token}")

        next_token = tokens[0]
        if next_token.content == "|":
            tokens = tokens[1:]
            rhs, tokens = ExpressionParser.parse_expression(tokens)
            return Union(lhs, rhs), tokens
        elif next_token.content == "&":
            tokens = tokens[1:]
            rhs, tokens = ExpressionParser.parse_expression(tokens)
            return Intersection(lhs, rhs), tokens
        elif next_token.content == "-":
            tokens = tokens[1:]
            rhs, tokens = ExpressionParser.parse_expression(tokens)
            return Difference(lhs, rhs), tokens
        elif next_token.content == "==":
            tokens = tokens[1:]
            rhs, tokens = ExpressionParser.parse_expression(tokens)
            return Equality(lhs, rhs), tokens
        elif next_token.content == "!=":
            tokens = tokens[1:]
            rhs, tokens = ExpressionParser.parse_expression(tokens)
            return InEquality(lhs, rhs), tokens
        elif next_token.content == "in":
            tokens = tokens[1:]
            rhs, tokens = ExpressionParser.parse_expression(tokens)
            return In(lhs, rhs), tokens

        else:
            return lhs, tokens

    @staticmethod
    def parse_qualified(tokens):
        name_tokens = []
        while True:
            next_token = tokens[0]
            if next_token.type == "Identifier":
                name_tokens.append(next_token)
                tokens = tokens[1:]
            else:
                break

            next_token = tokens[0]
            if next_token.content == ".":
                tokens = tokens[1:]
        return Qualified(name_tokens), tokens
