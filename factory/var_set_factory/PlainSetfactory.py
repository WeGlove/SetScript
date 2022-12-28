from factory.factory import Factory
from factory.var_set_factory.PlainExpFactory import VarSetExpFactory
from factory.var_set_factory.PlainStmtFactory import VarSetStmtFactory


class VarSetSetFactory(Factory):

    def __init__(self, set_class):
        self.set_class = set_class
        self.exp_factory = VarSetExpFactory(self.set_class)
        self.stmt_factory = VarSetStmtFactory(self.set_class)

    def get_expression_factory(self):
        return self.exp_factory

    def get_statement_factory(self):
        return self.stmt_factory
