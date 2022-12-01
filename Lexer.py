from Token import Token


class Lexer:

    keywords = ["{", "}", "|", "=", "&", "==", ",", "-", ";", "in", "while", "(", ")", "def", "return"]
    whitespace = [" ", "\n", "\t", "\r"]

    @staticmethod
    def lex_keyword(line, line_number):
        possible_key_words = list(Lexer.keywords)

        chain = ""
        matches = []
        for i in range(len(line)):
            char = line[i]
            chain += char
            possible_key_words = [word for word in possible_key_words if word.startswith(chain)]
            matches.extend([word for word in possible_key_words if word == chain])

            if len(possible_key_words) == 0:
                break

        if len(matches) == 0:
            raise ValueError

        out = max(matches, key=lambda x: len(x))

        return Token("Symbol", out, line_number), line[len(out):]

    @staticmethod
    def lex_line(line, line_number):
        tokens = []

        word = ""
        while len(line) > 0:
            char = line[0]
            if char in Lexer.whitespace:
                if len(word) > 0:
                    tokens.append(Token("Word", word, line_number))
                    word = ""
                line = line[1:]
            elif char in Lexer.keywords:
                if len(word) > 0:
                    tokens.append(Token("Word", word, line_number))
                    word = ""
                token, line = Lexer.lex_keyword(line, line_number)
                tokens.append(token)
            else:
                word += line[0]
                line = line[1:]
        return tokens

    @staticmethod
    def lex(f):
        tokens = []
        line_number = 0

        while True:
            line = f.readline()
            if line == "":
                break
            tokens.extend(Lexer.lex_line(line, line_number))
            line_number += 1

        return tokens


