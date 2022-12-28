from abc import abstractmethod


class Factory:

    @abstractmethod
    def get_expression_factory(self):
        pass

    @abstractmethod
    def get_statement_factory(self):
        pass