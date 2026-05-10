from queue_with_single_linked_list import Queue
from DSA import *


queue = Queue()
while not stdIsEmpty():
	queue.enqueue(stdReadString())
while not queue.is_empty():
	print(queue.dequeue(), end=" ")
print()