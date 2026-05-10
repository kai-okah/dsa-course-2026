# This the implementation of a Stack using an array that dynamically reallocates itself.
from stack_api import StackAPI

class Stack(StackAPI):

    def __init__(self):
        self.data = [None]
        self.capacity = 1
        self.size = 0

    def __resize(self, capacity):
        new_array = [None] * capacity
        for i in  range(self.size):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity =  len(self.data)

    def push(self, item):
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)
        self.data[self.size] = item
        self.size += 1

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            item = self.data[self.size]
            self.data[self.size] = None
        if self.size == self.capacity // 4:
            self.__resize(self.capacity // 2)
        return item

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0