import execute_file
from parsing.ExpressionParser import ExpressionParser


class StatementParser:

    def __init__(self, factory):
        self.factory = factory
        self.stmt_factory = factory.get_statement_factory()
        self.expression_parser = ExpressionParser(self.factory.get_expression_factory())

    def parse_assignment(self, tokens):
        qualified, tokens = self.expression_parser.parse_qualified(tokens)

        assign = tokens[0]
        if assign.content != "=":
            raise ValueError("Expression variable is not a Word")
        expression, tokens = self.expression_parser.parse_expression(tokens[1:])
        assignment = self.stmt_factory.Assignment(qualified, expression)
        return assignment, tokens

    def parse_while(self, tokens):
        token_while = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]
        condition, tokens = self.expression_parser.parse_expression(tokens)
        token_bracket_close = tokens[0]
        token_curl_open = tokens[1]
        tokens = tokens[2:]
        statements = []
        while tokens[0].content != "}":
            statement, tokens = self.parse_statement(tokens)
            statements.append(statement)
        tokens = tokens[1:]

        return self.stmt_factory.WhileLoop(condition, statements), tokens

    def parse_for(self, tokens):
        token_for = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]
        start, tokens = self.parse_statement(tokens)
        condition, tokens = self.parse_statement(tokens)
        induction, tokens = self.parse_statement(tokens)
        token_bracket_close = tokens[0]
        token_curl_open = tokens[1]
        tokens = tokens[2:]
        statements = []
        while tokens[0].content != "}":
            statement, tokens = self.parse_statement(tokens)
            statements.append(statement)
        tokens = tokens[1:]

        return self.stmt_factory.ForLoop(start, condition, induction, statements), tokens

    def parse_function_parameters(self, tokens):
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
                identifiers.append(self.factory.get_expression_factory().Variable(next_token.content))

    def parse_function_body(self, tokens):
        bracket_open = tokens[0]
        tokens = tokens[1:]

        statements = []
        while True:
            next_token = tokens[0]
            if next_token.content == "}":
                return statements, tokens[1:]
            else:
                statement, tokens = self.parse_statement(tokens)
                statements.append(statement)

    def parse_function(self, tokens):
        def_token = tokens[0]
        identifier_token = tokens[1]
        tokens = tokens[2:]
        identifiers, tokens = self.parse_function_parameters(tokens)
        statements, tokens = self.parse_function_body(tokens)

        return self.stmt_factory.Function(self.factory.get_expression_factory().Variable(identifier_token.content),
                                          [identifier.name for identifier in identifiers], statements), tokens

    def parse_import(self, tokens):
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

        from parsing.Parser import Parser
        path = ""
        for name in path_tokens:
            path += name.content
        print(path)
        subtree = execute_file.compile(path, self.factory)

        return self.stmt_factory.StmtImport(subtree), tokens

    def parse_if(self, tokens):
        if_token = tokens[0]
        tokens = tokens[1:]

        bracket_open = tokens[0]
        condition, tokens = self.expression_parser.parse_expression(tokens[1:])
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
                statement, tokens = self.parse_statement(tokens)
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
                    statement, tokens = self.parse_statement(tokens)
                    else_statements.append(statement)

        return self.stmt_factory.StmtIf(condition, if_statements, else_statements), tokens

    def parse_namespace(self, tokens):
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
            statement, tokens = self.parse_statement(tokens)
            statements.append(statement)

        token_curl_bracket_close = tokens[0]
        tokens = tokens[1:]

        return self.stmt_factory.Namespace(token_identifier, statements), tokens

    def parse_statement(self, tokens):
        token = tokens[0]
        if token.content == "while":
            statement, tokens = self.parse_while(tokens)
        elif token.content == "for":
            statement, tokens = self.parse_for(tokens)
        elif token.content == "def":
            statement, tokens = self.parse_function(tokens)
        elif token.content == "if":
            statement, tokens = self.parse_if(tokens)
        elif token.content == "return":
            expr, tokens = self.expression_parser.parse_expression(tokens[1:])
            statement = self.stmt_factory.StmtReturn(expr)
        elif token.content == "continue":
            expr, tokens = self.expression_parser.parse_expression(tokens[1:])
            statement = self.stmt_factory.StmtContinue()
        elif token.content == "break":
            expr, tokens = self.expression_parser.parse_expression(tokens[1:])
            statement = self.stmt_factory.StmtBreak()
        elif token.content == "import":
            statement, tokens = self.parse_import(tokens)
        elif token.content == "namespace":
            statement, tokens = self.parse_namespace(tokens)
        elif token.type == "Identifier" and tokens[1].content == "=":
            statement, tokens = self.parse_assignment(tokens)
        elif token.content == ";":
            statement = self.stmt_factory.Empty()
        else:
            statement, tokens = self.expression_parser.parse_expression(tokens)

        token = tokens[0]
        if token.content == ";":
            return statement, tokens[1:]
        else:
            raise ValueError(f"Missing Semicolon in {token.file}:{token.line_number}:{token.column_number}")
