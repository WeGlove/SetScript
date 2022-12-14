from abc import abstractmethod
from set_ast.Environment import Environment
from typing import Tuple


class Node:

    @abstractmethod
    def execute(self, env: Environment) -> Tuple[Environment, frozenset]:
        pass
