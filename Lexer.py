from Token import Token


class Lexer:

    keywords = ["{", "}", "+", "=", "*", "==", ",", "/", ";"]
    whitespace = [" ", "\n", "\t", "\r"]

    @staticmethod
    def lex_line(line):
        tokens = []

        word = ""
        for i in range(len(line)):
            if line[i] in Lexer.whitespace:
                if len(word) > 0:
                    tokens.append(Token("Word", word))
                    word = ""
            elif line[i] in Lexer.keywords:
                tokens.append(Token("Symbol",line[i]))
            else:
                word += line[i]
        return tokens

    @staticmethod
    def lex(f):
        tokens = []
        while True:
            line = f.readline()
            if line == "":
                break
            tokens.extend(Lexer.lex_line(line))

        return tokens


