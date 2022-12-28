from abc import abstractmethod


class AbstractSet:

    @abstractmethod
    def union(self, Y):
        pass

    @abstractmethod
    def difference(self, Y):
        pass

    @abstractmethod
    def intersection(self, Y):
        pass

    @abstractmethod
    def is_in(self, Y):
        pass

    @abstractmethod
    def big_union(self):
        pass

    @abstractmethod
    def big_intersection(self):
        pass
