class ParsingUtils:

    @staticmethod
    def parse_list(tokens, bracket_left, bracket_right, delimiter, action):
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
                out, tokens = action(tokens)
                elements.append(out)
