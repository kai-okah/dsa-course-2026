from abc import ABC, abstractmethod

#This is the interface for UF
class UF(ABC):

    @abstractmethod
    def union(self, p, q):
        pass

    @abstractmethod
    def find(self, p):
        pass
    def connected(self, p, q):
        return self.find(q) == self.find(p)