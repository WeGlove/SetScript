class ExpressionParser:

    def __init__(self, expr_factory):
        self.expr_factory = expr_factory

    def parse_list(self, tokens, bracket_left, bracket_right, delimiter):
        token_open = tokens[0]
        if token_open.content != bracket_left:
            raise ValueError(f"Unexpected left bracket in {token_open.file}:{token_open.line_number}:{token_open.column_number}")
        tokens = tokens[1:]

        elements = []
        comma_count = 0
        while True:
            next_token = tokens[0]

            if next_token.content == delimiter:
                if comma_count > 0:
                    raise ValueError("Too many commas in set")
                if len(elements) == 0:
                    raise ValueError()

                comma_count += 1
                tokens = tokens[1:]
            elif next_token.content == bracket_right:
                return elements, tokens[1:]
            else:
                comma_count = 0
                out, tokens = self.parse_expression(tokens)
                elements.append(out)

    def parse_set(self, tokens):
        elements, tokens = self.parse_list(tokens, "{", "}", ",")
        return self.expr_factory.Set(elements), tokens

    def parse_Tuple(self, tokens):
        elements, tokens = self.parse_list(tokens, "<", ">", ",")
        return self.expr_factory.Tuple(elements), tokens

    def parse_function_call(self, tokens):
        identifier, tokens = self.parse_qualified(tokens)

        if identifier.names[-1] == "P":
            expressions, tokens = self.parse_list(tokens, "(", ")", ",")
            if len(expressions) != 1 or len(identifier.names) != 1:
                raise ValueError("Too many parameters in power set")
            return self.expr_factory.Power(expressions[0]), tokens

        expressions, tokens = self.parse_list(tokens, "(", ")", ",")
        return self.expr_factory.FunctionCall(identifier, expressions), tokens

    def parse_parentheses(self, tokens):
        token_open = tokens[0]
        expression, tokens = self.parse_expression(tokens[1:])
        token_close = tokens[0]

        return expression, tokens[1:]

    def parse_big_union(self, tokens):
        symbol = tokens[0]
        expr, tokens = self.parse_expression(tokens[1:])
        return self.expr_factory.BigUnion(expr), tokens

    def parse_big_intersection(self, tokens):
        symbol = tokens[0]
        expr, tokens = self.parse_expression(tokens[1:])
        return self.expr_factory.BigIntersection(expr), tokens

    def parse_expression(self, tokens):
        next_token = tokens[0]

        if next_token.content == "{":
            lhs, tokens = self.parse_set(tokens)
        elif next_token.content == "<":
            lhs, tokens = self.parse_Tuple(tokens)
        elif next_token.content == "(":
            lhs, tokens = self.parse_parentheses(tokens)
        elif next_token.type == "Identifier":
            qualified, q_tokens = self.parse_qualified(tokens)
            next_token = q_tokens[0]
            if next_token.content == "(":
                lhs, tokens = self.parse_function_call(tokens)
            else:
                lhs, tokens = self.parse_qualified(tokens)
        elif next_token.type == "Number":
            lhs = self.expr_factory.Number(int(next_token.content))
            tokens = tokens[1:]
        elif next_token.content == "&&":
            expr, tokens = self.parse_big_intersection(tokens)
            return expr, tokens
        elif next_token.content == "||":
            expr, tokens = self.parse_big_union(tokens)
            return expr, tokens
        else:
            raise ValueError(f"Unknown expression {next_token}")

        next_token = tokens[0]
        if next_token.content == "|":
            tokens = tokens[1:]
            rhs, tokens = self.parse_expression(tokens)
            return self.expr_factory.Union(lhs, rhs), tokens
        elif next_token.content == "&":
            tokens = tokens[1:]
            rhs, tokens = self.parse_expression(tokens)
            return self.expr_factory.Intersection(lhs, rhs), tokens
        elif next_token.content == "-":
            tokens = tokens[1:]
            rhs, tokens = self.parse_expression(tokens)
            return self.expr_factory.Difference(lhs, rhs), tokens
        elif next_token.content == "==":
            tokens = tokens[1:]
            rhs, tokens = self.parse_expression(tokens)
            return self.expr_factory.Equality(lhs, rhs), tokens
        elif next_token.content == "!=":
            tokens = tokens[1:]
            rhs, tokens = self.parse_expression(tokens)
            return self.expr_factory.InEquality(lhs, rhs), tokens
        elif next_token.content == "in":
            tokens = tokens[1:]
            rhs, tokens = self.parse_expression(tokens)
            return self.expr_factory.In(lhs, rhs), tokens

        else:
            return lhs, tokens

    def parse_qualified(self, tokens):
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
        return self.expr_factory.Qualified(name_tokens), tokens
