from abc import abstractmethod


class StatementFactory:

    @staticmethod
    def Assignment(variable, expr):
        pass

    @staticmethod
    def Empty():
        pass

    @staticmethod
    def ForLoop(inital, condition, inc, statements):
        pass

    @staticmethod
    def Function(name, parameters, statements):
        pass

    @staticmethod
    def Namespace(name, statements):
        pass

    @staticmethod
    def StmtBreak():
        pass

    @staticmethod
    def StmtContinue():
        pass

    @staticmethod
    def StmtIf(condition, if_statements, else_statements):
        pass

    @staticmethod
    def StmtImport(expr):
        pass

    @staticmethod
    def WhileLoop(condition, statements):
        pass
