from Token import Token


class Lexer:

    symbols = ["{", "}", "|", "=", "&", "==", ",", "-", ";", "!=", "(", ")", "#", "<", ">",  "&&", "||",  "."]
    keywords = ["import", "if", "else", "namespace", "def", "return", "for", "in", "while", ]

    whitespace = [" ", "\n", "\t", "\r"]

    @staticmethod
    def lex_symbol(line, file, line_number, column_number):
        possible_symbols = list(Lexer.symbols)

        chain = ""
        matches = []
        for i in range(len(line)):
            char = line[i]
            chain += char
            possible_symbols = [word for word in possible_symbols if word.startswith(chain)]
            matches.extend([word for word in possible_symbols if word == chain])

            if len(possible_symbols) == 0:
                break

        if len(matches) == 0:
            return None, line

        out = max(matches, key=lambda x: len(x))

        return Token("Symbol", out, file, line_number, column_number), line[len(out):]

    @staticmethod
    def lex_line(line, file, line_number):
        tokens = []

        word = ""
        column_number = 0
        while len(line) > 0:
            char = line[0]
            if char == "#":
                break
            if char in Lexer.whitespace:
                if len(word) > 0:
                    tokens.append(Token("Identifier", word, file, line_number, column_number))
                    word = ""
                line = line[1:]
            elif char in [l[0] for l in Lexer.symbols]:
                token, line = Lexer.lex_symbol(line, file, line_number, column_number)
                if token is None:
                    word += line[0]
                    line = line[1:]
                else:
                    if len(word) > 0:
                        tokens.append(Token("Identifier", word, file, line_number, column_number))
                        word = ""
                    tokens.append(token)
            else:
                word += line[0]
                line = line[1:]

            column_number += 1
        return tokens

    @staticmethod
    def lex(path):
        with open(path, "r") as f:
            tokens = []
            line_number = 0

            while True:
                line = f.readline()
                if line == "":
                    break
                tokens.extend(Lexer.lex_line(line, path, line_number))
                line_number += 1

            return tokens


