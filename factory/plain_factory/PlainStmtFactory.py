from abc import abstractmethod
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


class PlainStmtFactory(StatementFactory):

    def Assignment(self, x, X):
        return Assignment(x, X)

    def Empty(self):
        return Empty()

    def ForLoop(self, inital, condition, inc, statements):
        return ForLoop(inital, condition, inc, statements)

    def Function(self, name, parameters, statements):
        return Function(name, parameters, statements)

    def Namespace(self, name, statements):
        return Namespace(name, statements)

    def StmtBreak(self, ):
        return StmtBreak(...)

    def StmtContinue(self, ):
        return StmtContinue()

    def StmtIf(self, condition, if_statements, else_statements):
        return StmtIf(condition, if_statements, else_statements)

    def StmtImport(self, expr):
        return StmtImport(expr)

    def WhileLoop(self, condition, statements):
        return WhileLoop(condition, statements)

    def StmtReturn(self, expr):
        return StmtReturn(expr)

