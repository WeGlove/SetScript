from abc import abstractmethod


class Node:

    @abstractmethod
    def execute(self, env=None):
        pass