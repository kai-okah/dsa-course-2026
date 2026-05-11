from queue_api import QueueAPI

class Queue(QueueAPI):

    class _Node:

        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def enqueue(self, item):
        new_node = self._Node(item)
        self._size += 1
        if None == self.last:
            self.first = new_node
            self.last = new_node
            return
        self.last.next = new_node
        self.last  = new_node

    def dequeue(self):
        if None == self.first:
            return None
        data = self.first.item
        self.first = self.first.next
        self._size -= 1
        if self.first == None:
            self.last = None
        return data

    def is_empty(self):
        return None == self.first

    def size(self):
        return self._size