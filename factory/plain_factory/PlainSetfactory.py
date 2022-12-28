from factory.factory import Factory
from factory.plain_factory.PlainExpFactory import PlainExpFactory
from factory.plain_factory.PlainStmtFactory import PlainStmtFactory


class PlainSetFactory(Factory):

    def __init__(self):
        self.exp_factory = PlainExpFactory()
        self.stmt_factory = PlainStmtFactory()

    def get_expression_factory(self):
        return self.exp_factory

    def get_statement_factory(self):
        return self.stmt_factory
