from queue_api import QueueAPI

class Queue(QueueAPI):

    def __init__(self):
        self.item = [None]
        self.capacity = 1
        self._size = 0
        self.front = 0
        self.back = self.capacity - 1

    def __resize(self, capacity):
        copy = [None] * capacity
        for i in range(self._size):
            copy[i] = self.item[(i+ self.front) % self.capacity]
        self.front = 0
        self.back = self._size
        self.item = copy
        self.capacity = capacity

    def enqueue(self, item):
        if self._size == self.capacity:
            self.__resize(self.capacity * 2)
        self.item[self.back] = item
        self.back = (self.back + 1) % self.capacity
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None
        item  = self.item[self.front]
        self.item[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self._size -= 1
        if self.capacity > 1 and  self._size == self.capacity // 4:
            self.__resize(self.capacity // 2)
        return item

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size