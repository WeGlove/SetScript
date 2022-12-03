from abc import abstractmethod
from set_ast.Environment import Environment


class Node:

    @abstractmethod
    def execute(self, env: Environment):
        pass
