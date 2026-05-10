from abc import ABC, abstractmethod

class QueueAPI(ABC):

    @abstractmethod
    def enqueue (self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass