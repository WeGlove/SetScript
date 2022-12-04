from set_ast.expression.set import Set
from set_ast.expression.tuple import Tuple
from set_ast.statement.assignment import Assignment
from set_ast.expression.Variable import Variable
from set_ast.expression.operation.binary.union import Union
from set_ast.expression.operation.binary.intersection import Intersection
from set_ast.expression.operation.binary.difference import Difference
from set_ast.expression.operation.binary.equality import Equality
from set_ast.expression.operation.binary.inequality import InEquality
from set_ast.expression.operation.big_intersection import BigIntersection
from set_ast.expression.operation.big_union import BigUnion
from set_ast.statement.while_loop import WhileLoop
from set_ast.statement.for_loop import ForLoop
from set_ast.set_ast import SetAst
from set_ast.expression.operation.binary.In import In
from set_ast.statement.stmt_return import StmtReturn
from set_ast.statement.function import Function
from set_ast.expression.function_call import FunctionCall
from set_ast.statement.stmt_import import StmtImport
from set_ast.statement.stmt_if import StmtIf


class Parser:

    @staticmethod
    def parse_list(tokens, bracket_left, bracket_right, delimiter, action):
        token_open = tokens[0]
        if token_open.content != bracket_left:
            raise ValueError("Unexpected lef bracket")
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

    @staticmethod
    def parse_set(tokens):
        elements, tokens = Parser.parse_list(tokens, "{", "}", ",", Parser.parse_expression)
        return Set(elements), tokens

    @staticmethod
    def parse_Tuple(tokens):
        elements, tokens = Parser.parse_list(tokens, "<", ">", ",", Parser.parse_expression)
        return Tuple(elements), tokens

    @staticmethod
    def parse_function_call(tokens):
        identifier = tokens[0]
        tokens = tokens[1:]

        expressions, tokens = Parser.parse_list(tokens, "(", ")", ",", Parser.parse_expression)
        return FunctionCall(Variable(identifier.content), expressions), tokens

    @staticmethod
    def parse_parentheses(tokens):
        token_open = tokens[0]
        expression, tokens = Parser.parse_expression(tokens[1:])
        token_close = tokens[0]

        return expression, tokens[1:]

    @staticmethod
    def parse_big_union(tokens):
        symbol = tokens[0]
        expr, tokens = Parser.parse_expression(tokens[1:])
        return BigUnion(expr), tokens

    @staticmethod
    def parse_big_intersection(tokens):
        symbol = tokens[0]
        expr, tokens = Parser.parse_expression(tokens[1:])
        return BigIntersection(expr), tokens

    @staticmethod
    def parse_expression(tokens):
        next_token = tokens[0]

        if next_token.content == "{":
            lhs, tokens = Parser.parse_set(tokens)
        elif next_token.content == "<":
            lhs, tokens = Parser.parse_Tuple(tokens)
        elif next_token.content == "(":
            lhs, tokens = Parser.parse_parentheses(tokens)
        elif next_token.type == "Identifier":
            over_next_token = tokens[1]
            if over_next_token.content == "(":
                lhs, tokens = Parser.parse_function_call(tokens)
            else:
                lhs, tokens = Variable(next_token.content), tokens[1:]
        elif next_token.content == "&&":
            expr, tokens = Parser.parse_big_intersection(tokens)
            return expr, tokens
        elif next_token.content == "||":
            expr, tokens = Parser.parse_big_union(tokens)
            return expr, tokens
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
        elif next_token.content == "!=":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return InEquality(lhs, rhs), tokens
        elif next_token.content == "in":
            tokens = tokens[1:]
            rhs, tokens = Parser.parse_expression(tokens)
            return In(lhs, rhs), tokens

        else:
            return lhs, tokens

    @staticmethod
    def parse_assignment(tokens):
        variable = tokens[0]
        if variable.type != "Identifier":
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
    def parse_for(tokens):
        token_for = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]
        start, tokens = Parser.parse_statement(tokens)
        condition, tokens = Parser.parse_statement(tokens)
        induction, tokens = Parser.parse_statement(tokens)
        token_bracket_close = tokens[0]
        token_curl_open = tokens[1]
        tokens = tokens[2:]
        statements = []
        while tokens[0].content != "}":
            statement, tokens = Parser.parse_statement(tokens)
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
                statement, tokens = Parser.parse_statement(tokens)
                statements.append(statement)

    @staticmethod
    def parse_function(tokens):
        def_token = tokens[0]
        identifier_token = tokens[1]
        tokens = tokens[2:]
        identifiers, tokens = Parser.parse_function_parameters(tokens)
        statements, tokens = Parser.parse_function_body(tokens)

        return Function(Variable(identifier_token.content), [identifier.name for identifier in identifiers], statements), tokens

    @staticmethod
    def parse_import(tokens):
        import_token = tokens[0]
        path = tokens[1]

        return StmtImport(path.content), tokens[2:]

    @staticmethod
    def parse_if(tokens):
        if_token = tokens[0]
        tokens = tokens[1:]

        bracket_open = tokens[0]
        condition, tokens = Parser.parse_expression(tokens[1:])
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
                statement, tokens = Parser.parse_statement(tokens)
                if_statements.append(statement)

        else_token = tokens[0]
        token_bracket_open = tokens[1]
        tokens = tokens[2:]

        else_statements = []
        while True:
            next_token = tokens[0]
            if next_token.content == "}":
                tokens = tokens[1:]
                break
            else:
                statement, tokens = Parser.parse_statement(tokens)
                else_statements .append(statement)

        return StmtIf(condition, if_statements, else_statements), tokens


    @staticmethod
    def parse_statement(tokens):
        token = tokens[0]
        if token.content == "while":
            statement, tokens = Parser.parse_while(tokens)
        elif token.content == "for":
            statement, tokens = Parser.parse_for(tokens)
        elif token.content == "def":
            statement, tokens = Parser.parse_function(tokens)
        elif token.content == "if":
            statement, tokens = Parser.parse_if(tokens)
        elif token.content == "return":
            expr, tokens = Parser.parse_expression(tokens[1:])
            statement = StmtReturn(expr)
        elif token.content == "import":
            statement, tokens = Parser.parse_import(tokens)
        elif token.type == "Identifier" and tokens[1].content == "=":
            statement, tokens = Parser.parse_assignment(tokens)
        else:
            statement, tokens = Parser.parse_expression(tokens)

        token = tokens[0]
        if token.content == ";":
            return statement, tokens[1:]
        else:
            raise ValueError(f"Missing Semicolon in {token.file}:{token.line_number}:{token.column_number}")

    @staticmethod
    def parse(tokens):
        statements = []
        while len(tokens) > 0:
            statement, tokens = Parser.parse_statement(tokens)
            statements.append(statement)

        return SetAst(statements)
