# This the implementation of a Stack using an array that dynamically reallocates itself.
from stack_api import StackAPI

class Stack(StackAPI):

    def __init__(self):
        self.data = [None]
        self.capacity = 1
        self._size = 0

    def __resize(self, capacity):
        new_array = [None] * capacity
        for i in  range(self._size):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity =  len(self.data)

    def push(self, item):
        if self._size == self.capacity:
            self.__resize(self.capacity * 2)
        self.data[self._size] = item
        self._size += 1

    def pop(self):
        if self._size == self.capacity // 4:
            self.__resize(self.capacity // 2)
        if not self.is_empty():
            self._size -= 1
            item = self.data[self._size]
            self.data[self._size] = None
            return item
        return None

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0