# This is the implementation of Stack using a single linked list
from stack_api import StackAPI

class Stack(StackAPI):

    class _Node:

        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.count = 0
        self.first = None

    def pop(self):
        if self.count == 0:
            return None
        item = self.first.item
        self.first = self.first.next
        self.count -= 1
        return item

    def push(self, item):
        new_node = self._Node(item)
        self.count += 1
        if None == self.first:
            self.first = new_node
            new_node.next = None
            return
        new_node.next = self.first
        self.first = new_node

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count