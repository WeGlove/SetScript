from set_ast.statement.empty import Empty
from set_ast.statement.assignment import Assignment
from set_ast.statement.for_loop import ForLoop
from set_ast.statement.function import Function
from set_ast.statement.namespace import Namespace
from set_ast.statement.stmt_if import StmtIf
from set_ast.statement.stmt_import import StmtImport
from set_ast.statement.stmt_return import StmtReturn
from set_ast.statement.stmt_break import StmtBreak
from set_ast.statement.stmt_continue import StmtContinue
from set_ast.statement.while_loop import WhileLoop
from set_ast.expression.Variable import Variable
from parsing.ExpressionParser import ExpressionParser


class StatementParser:

    @staticmethod
    def parse_assignment(tokens):
        qualified, tokens = ExpressionParser.parse_qualified(tokens)

        assign = tokens[0]
        if assign.content != "=":
            raise ValueError("Expression variable is not a Word")
        expression, tokens = ExpressionParser.parse_expression(tokens[1:])
        assignment = Assignment(qualified, expression)
        return assignment, tokens

    @staticmethod
    def parse_while(tokens):
        token_while = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]
        condition, tokens = ExpressionParser.parse_expression(tokens)
        token_bracket_close = tokens[0]
        token_curl_open = tokens[1]
        tokens = tokens[2:]
        statements = []
        while tokens[0].content != "}":
            statement, tokens = StatementParser.parse_statement(tokens)
            statements.append(statement)
        tokens = tokens[1:]

        return WhileLoop(condition, statements), tokens

    @staticmethod
    def parse_for(tokens):
        token_for = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]
        start, tokens = StatementParser.parse_statement(tokens)
        condition, tokens = StatementParser.parse_statement(tokens)
        induction, tokens = StatementParser.parse_statement(tokens)
        token_bracket_close = tokens[0]
        token_curl_open = tokens[1]
        tokens = tokens[2:]
        statements = []
        while tokens[0].content != "}":
            statement, tokens = StatementParser.parse_statement(tokens)
            statements.append(statement)
        tokens = tokens[1:]

        return ForLoop(start, condition, induction, statements), tokens

    @staticmethod
    def parse_function_parameters(tokens):
        token_open = tokens[0]
        if token_open.content != "(":
            raise ValueError()
        tokens = tokens[1:]

        identifiers = []
        comma_count = 0
        while True:
            next_token = tokens[0]

            if next_token.content == ",":
                if comma_count > 0:
                    raise ValueError("Too many commas in set")
                if len(identifiers) == 0:
                    raise ValueError()

                comma_count += 1
                tokens = tokens[1:]
            elif next_token.content == ")":
                return identifiers, tokens[1:]
            else:
                comma_count = 0
                tokens = tokens[1:]
                identifiers.append(Variable(next_token.content))

    @staticmethod
    def parse_function_body(tokens):
        bracket_open = tokens[0]
        tokens = tokens[1:]

        statements = []
        while True:
            next_token = tokens[0]
            if next_token.content == "}":
                return statements, tokens[1:]
            else:
                statement, tokens = StatementParser.parse_statement(tokens)
                statements.append(statement)

    @staticmethod
    def parse_function(tokens):
        def_token = tokens[0]
        identifier_token = tokens[1]
        tokens = tokens[2:]
        identifiers, tokens = StatementParser.parse_function_parameters(tokens)
        statements, tokens = StatementParser.parse_function_body(tokens)

        return Function(Variable(identifier_token.content), [identifier.name for identifier in identifiers], statements), tokens

    @staticmethod
    def parse_import(tokens):
        import_token = tokens[0]
        tokens = tokens[1:]

        path_tokens = []
        while True:
            next_token = tokens[0]
            if next_token.type == "Identifier":
                path_tokens.append(next_token)
                tokens = tokens[1:]
            else:
                break

            next_token = tokens[0]
            if next_token.content == ".":
                path_tokens.append(next_token)
                tokens = tokens[1:]

        if len(path_tokens) == 0:
            raise ValueError(f"Empty Path in import {import_token.file}:{import_token.line_number}:{import_token.column_number}")

        return StmtImport(path_tokens), tokens

    @staticmethod
    def parse_if(tokens):
        if_token = tokens[0]
        tokens = tokens[1:]

        bracket_open = tokens[0]
        condition, tokens = ExpressionParser.parse_expression(tokens[1:])
        bracket_close = tokens[0]

        token_bracket_open = tokens[1]
        tokens = tokens[2:]

        if_statements = []
        while True:
            next_token = tokens[0]
            if next_token.content == "}":
                tokens = tokens[1:]
                break
            else:
                statement, tokens = StatementParser.parse_statement(tokens)
                if_statements.append(statement)

        else_token = tokens[0]
        else_statements = []
        if else_token.content == "else":
            token_bracket_open = tokens[1]
            tokens = tokens[2:]

            while True:
                next_token = tokens[0]
                if next_token.content == "}":
                    tokens = tokens[1:]
                    break
                else:
                    statement, tokens = StatementParser.parse_statement(tokens)
                    else_statements.append(statement)

        return StmtIf(condition, if_statements, else_statements), tokens

    @staticmethod
    def parse_namespace(tokens):
        token_namespace = tokens[0]
        token_bracket_open = tokens[1]
        token_identifier = tokens[2]
        token_bracket_close = tokens[3]
        token_curl_bracket_open = tokens[4]
        tokens = tokens[5:]
        statements = []
        while True:
            next_token = tokens[0]
            if next_token.content == "}":
                break
            statement, tokens = StatementParser.parse_statement(tokens)
            statements.append(statement)

        token_curl_bracket_close = tokens[0]
        tokens = tokens[1:]

        return Namespace(token_identifier, statements), tokens

    @staticmethod
    def parse_statement(tokens):
        token = tokens[0]
        if token.content == "while":
            statement, tokens = StatementParser.parse_while(tokens)
        elif token.content == "for":
            statement, tokens = StatementParser.parse_for(tokens)
        elif token.content == "def":
            statement, tokens = StatementParser.parse_function(tokens)
        elif token.content == "if":
            statement, tokens = StatementParser.parse_if(tokens)
        elif token.content == "return":
            expr, tokens = ExpressionParser.parse_expression(tokens[1:])
            statement = StmtReturn(expr)
        elif token.content == "continue":
            expr, tokens = ExpressionParser.parse_expression(tokens[1:])
            statement = StmtContinue(expr)
        elif token.content == "break":
            expr, tokens = ExpressionParser.parse_expression(tokens[1:])
            statement = StmtBreak(expr)
        elif token.content == "import":
            statement, tokens = StatementParser.parse_import(tokens)
        elif token.content == "namespace":
            statement, tokens = StatementParser.parse_namespace(tokens)
        elif token.type == "Identifier" and tokens[1].content == "=":
            statement, tokens = StatementParser.parse_assignment(tokens)
        elif token.content == ";":
            statement = Empty()
        else:
            statement, tokens = ExpressionParser.parse_expression(tokens)

        token = tokens[0]
        if token.content == ";":
            return statement, tokens[1:]
        else:
            raise ValueError(f"Missing Semicolon in {token.file}:{token.line_number}:{token.column_number}")
