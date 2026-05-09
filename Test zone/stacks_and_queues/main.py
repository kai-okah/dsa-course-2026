from stack_with_single_linked_list import Stack
from DSA import *


stack = Stack()
while not stdIsEmpty():
    stack.push(stdReadString())
while not stack.is_empty():
    print(stack.pop(), end=" ")
