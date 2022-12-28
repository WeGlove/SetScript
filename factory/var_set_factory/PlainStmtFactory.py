from factory.statement_factory import StatementFactory
from set_ast.statement.assignment import Assignment
from set_ast.statement.empty import Empty
from set_ast.statement.for_loop import ForLoop
from set_ast.statement.function import Function
from set_ast.statement.namespace import Namespace
from set_ast.statement.stmt_break import StmtBreak
from set_ast.statement.stmt_continue import StmtContinue
from set_ast.statement.stmt_if import StmtIf
from set_ast.statement.stmt_import import StmtImport
from set_ast.statement.while_loop import WhileLoop
from set_ast.statement.stmt_return import StmtReturn
from set_ast.set_ast import SetAst


class VarSetStmtFactory(StatementFactory):

    def __init__(self, set_class):
        self.set_class = set_class

    def SetAst(self, statments):
        return SetAst(self.set_class, statments)

    def Assignment(self, x, X):
        return Assignment(self.set_class, x, X)

    def Empty(self):
        return Empty(self.set_class)

    def ForLoop(self, inital, condition, inc, statements):
        return ForLoop(self.set_class, inital, condition, inc, statements)

    def Function(self, name, parameters, statements):
        return Function(self.set_class, name, parameters, statements)

    def Namespace(self, name, statements):
        return Namespace(self.set_class, name, statements)

    def StmtBreak(self, ):
        return StmtBreak(self.set_class)

    def StmtContinue(self, ):
        return StmtContinue(self.set_class)

    def StmtIf(self, condition, if_statements, else_statements):
        return StmtIf(self.set_class, condition, if_statements, else_statements)

    def StmtImport(self, expr):
        return StmtImport(self.set_class, expr)

    def WhileLoop(self, condition, statements):
        return WhileLoop(self.set_class, condition, statements)

    def StmtReturn(self, expr):
        return StmtReturn(self.set_class, expr)

