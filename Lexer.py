from Token import Token


class Lexer:

    keywords = ["{", "}", "|", "=", "&", "==", ",", "-", ";"]
    whitespace = [" ", "\n", "\t", "\r"]

    @staticmethod
    def lex_line(line, line_number):
        tokens = []

        word = ""
        for i in range(len(line)):
            if line[i] in Lexer.whitespace:
                if len(word) > 0:
                    tokens.append(Token("Word", word, line_number))
                    word = ""
            elif line[i] in Lexer.keywords:
                if len(word) > 0:
                    tokens.append(Token("Word", word, line_number))
                    word = ""
                tokens.append(Token("Symbol", line[i], line_number))
            else:
                word += line[i]
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


