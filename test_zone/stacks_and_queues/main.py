from queue_with_array import Queue as ArrayQueue
from queue_with_single_linked_list import Queue as LinkedListQueue
from stack_with_array import Stack as ArrayStack
from stack_with_single_linked_list import Stack as LinkedListStack

# Number of test groups: 4
# Group 1: Queue with array
# Group 2: Queue with linked list
# Group 3: Stack with array
# Group 4: Stack with linked list

def show_result(test_name, expected, actual):
    print(test_name)
    print("Expected:", expected)
    print("Actual:  ", actual)

    if expected == actual:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print()

def call_or_error(function):
    try:
        return function()
    except Exception as error:
        return type(error).__name__

def section(title):
    print()
    print(title)
    print("=" * 60)

def test_queue_with_array():
    # Group 1: Testing Queue with Array
    # Number of conditions being tested: 12

    section("TESTING QUEUE WITH ARRAY")

    # Condition 1: Test a new queue starts empty
    queue = ArrayQueue()
    show_result("Condition 1: New queue should be empty", True, queue.is_empty())

    # Condition 2: Dequeue from empty queue should return None
    queue = ArrayQueue()
    show_result("Condition 2: Dequeue from empty queue should return None", None, queue.dequeue())

    # Condition 3: Enqueue one item should make queue not empty
    queue = ArrayQueue()
    queue.enqueue("A")
    show_result("Condition 3: After enqueue, queue should not be empty", False, queue.is_empty())

    # Condition 4: Dequeue should return the first item
    queue = ArrayQueue()
    queue.enqueue("A")
    show_result("Condition 4: Dequeue should return the first item", "A", queue.dequeue())

    # Condition 5: Enqueue after emptying queue should not crash
    queue = ArrayQueue()

    def reuse_after_emptying():
        queue.enqueue("A")
        queue.dequeue()
        queue.enqueue("B")
        return queue.dequeue()

    show_result("Condition 5: Queue should work after becoming empty", "B", call_or_error(reuse_after_emptying))

    # Condition 6: Queue should follow FIFO order
    queue = ArrayQueue()
    for item in ["A", "B", "C"]:
        queue.enqueue(item)
    actual = [queue.dequeue(), queue.dequeue(), queue.dequeue()]
    show_result("Condition 6: Queue should follow FIFO order", ["A", "B", "C"], actual)

    # Condition 7: Queue should grow when many items are added
    queue = ArrayQueue()

    def grow_and_dequeue():
        for item in ["A", "B", "C", "D", "E", "F"]:
            queue.enqueue(item)
        return [queue.dequeue(), queue.dequeue(), queue.dequeue(), queue.dequeue(), queue.dequeue(), queue.dequeue()]

    show_result("Condition 7: Queue should grow and keep FIFO order", ["A", "B", "C", "D", "E", "F"], call_or_error(grow_and_dequeue))

    # Condition 8: Interleaved enqueue and dequeue should keep order
    queue = ArrayQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    first = queue.dequeue()
    queue.enqueue("C")
    second = queue.dequeue()
    third = queue.dequeue()
    show_result("Condition 8: Interleaved enqueue/dequeue should keep FIFO order", ["A", "B", "C"], [first, second, third])

    # Condition 9: Queue should be empty after removing all items
    queue = ArrayQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.dequeue()
    queue.dequeue()
    show_result("Condition 9: Queue should be empty after removing all items", True, queue.is_empty())

    # Condition 10: size() should return 0 for a new queue
    queue = ArrayQueue()
    show_result("Condition 10: size() should return 0 for a new queue", 0, call_or_error(queue.size))

    # Condition 11: size() should update after enqueue and dequeue
    queue = ArrayQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.dequeue()
    show_result("Condition 11: size() should update after operations", 1, call_or_error(queue.size))

    # Condition 12: Enqueuing None should still behave as a stored item
    queue = ArrayQueue()
    queue.enqueue(None)
    actual = {
        "size_before_dequeue": call_or_error(queue.size),
        "dequeue_result": queue.dequeue(),
        "is_empty_after_dequeue": queue.is_empty()
    }
    expected = {
        "size_before_dequeue": 1,
        "dequeue_result": None,
        "is_empty_after_dequeue": True
    }
    show_result("Condition 12: Queue should allow None as an item", expected, actual)

def test_queue_with_linked_list():
    # Group 2: Testing Queue with Linked List
    # Number of conditions being tested: 12

    section("TESTING QUEUE WITH LINKED LIST")

    # Condition 1: Test a new queue starts empty
    queue = LinkedListQueue()
    show_result("Condition 1: New queue should be empty", True, queue.is_empty())

    # Condition 2: Dequeue from empty queue should return None
    queue = LinkedListQueue()
    show_result("Condition 2: Dequeue from empty queue should return None", None, queue.dequeue())

    # Condition 3: Enqueue one item should make queue not empty
    queue = LinkedListQueue()
    queue.enqueue("A")
    show_result("Condition 3: After enqueue, queue should not be empty", False, queue.is_empty())

    # Condition 4: Dequeue should return the first item
    queue = LinkedListQueue()
    queue.enqueue("A")
    show_result("Condition 4: Dequeue should return the first item", "A", queue.dequeue())

    # Condition 5: After removing the only item, first and last should both be None
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.dequeue()
    expected = {"first_is_none": True, "last_is_none": True}
    actual = {"first_is_none": queue.first is None, "last_is_none": queue.last is None}
    show_result("Condition 5: first and last should both be None after removing final item", expected, actual)

    # Condition 6: Enqueue after emptying queue should still work
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.dequeue()
    queue.enqueue("B")
    show_result("Condition 6: Enqueue after emptying should return the new item", "B", queue.dequeue())

    # Condition 7: Queue should follow FIFO order
    queue = LinkedListQueue()
    for item in ["A", "B", "C"]:
        queue.enqueue(item)
    actual = [queue.dequeue(), queue.dequeue(), queue.dequeue()]
    show_result("Condition 7: Queue should follow FIFO order", ["A", "B", "C"], actual)

    # Condition 8: Interleaved enqueue and dequeue should keep order
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    first = queue.dequeue()
    queue.enqueue("C")
    second = queue.dequeue()
    third = queue.dequeue()
    show_result("Condition 8: Interleaved enqueue/dequeue should keep FIFO order", ["A", "B", "C"], [first, second, third])

    # Condition 9: Queue should be empty after removing all items
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.dequeue()
    queue.dequeue()
    expected = {"is_empty": True, "first_is_none": True, "last_is_none": True}
    actual = {"is_empty": queue.is_empty(), "first_is_none": queue.first is None, "last_is_none": queue.last is None}
    show_result("Condition 9: Queue should be fully empty after removing all items", expected, actual)

    # Condition 10: size() should return 0 for a new queue
    queue = LinkedListQueue()
    show_result("Condition 10: size() should return 0 for a new queue", 0, call_or_error(queue.size))

    # Condition 11: size() should update after enqueue and dequeue
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.dequeue()
    show_result("Condition 11: size() should update after operations", 1, call_or_error(queue.size))

    # Condition 12: Enqueuing None should still behave as a stored item
    queue = LinkedListQueue()
    queue.enqueue(None)
    actual = {
        "size_before_dequeue": call_or_error(queue.size),
        "dequeue_result": queue.dequeue(),
        "is_empty_after_dequeue": queue.is_empty()
    }
    expected = {
        "size_before_dequeue": 1,
        "dequeue_result": None,
        "is_empty_after_dequeue": True
    }
    show_result("Condition 12: Queue should allow None as an item", expected, actual)

def test_stack_with_array():
    # Group 3: Testing Stack with Array
    # Number of conditions being tested: 11

    section("TESTING STACK WITH ARRAY")

    # Condition 1: Test a new stack starts empty
    stack = ArrayStack()
    show_result("Condition 1: New stack should be empty", True, stack.is_empty())

    # Condition 2: Pop from empty stack should return None
    stack = ArrayStack()
    show_result("Condition 2: Pop from empty stack should return None", None, call_or_error(stack.pop))

    # Condition 3: Push one item should make stack not empty
    stack = ArrayStack()
    stack.push("A")
    show_result("Condition 3: After push, stack should not be empty", False, stack.is_empty())

    # Condition 4: Pop should return the last pushed item
    stack = ArrayStack()
    stack.push("A")
    show_result("Condition 4: Pop should return the pushed item", "A", call_or_error(stack.pop))

    # Condition 5: Push after emptying stack should not crash
    stack = ArrayStack()

    def reuse_after_emptying():
        stack.push("A")
        stack.pop()
        stack.push("B")
        return stack.pop()

    show_result("Condition 5: Stack should work after becoming empty", "B", call_or_error(reuse_after_emptying))

    # Condition 6: Stack should follow LIFO order
    stack = ArrayStack()
    for item in ["A", "B", "C"]:
        stack.push(item)
    actual = [call_or_error(stack.pop), call_or_error(stack.pop), call_or_error(stack.pop)]
    show_result("Condition 6: Stack should follow LIFO order", ["C", "B", "A"], actual)

    # Condition 7: Stack should grow when many items are added
    stack = ArrayStack()

    def grow_and_pop():
        for item in ["A", "B", "C", "D", "E", "F"]:
            stack.push(item)
        return [stack.pop(), stack.pop(), stack.pop(), stack.pop(), stack.pop(), stack.pop()]

    show_result("Condition 7: Stack should grow and keep LIFO order", ["F", "E", "D", "C", "B", "A"], call_or_error(grow_and_pop))

    # Condition 8: Interleaved push and pop should keep order
    stack = ArrayStack()
    stack.push("A")
    stack.push("B")
    first = call_or_error(stack.pop)
    stack.push("C")
    second = call_or_error(stack.pop)
    third = call_or_error(stack.pop)
    show_result("Condition 8: Interleaved push/pop should keep LIFO order", ["B", "C", "A"], [first, second, third])

    # Condition 9: Stack should be empty after removing all items
    stack = ArrayStack()
    stack.push("A")
    stack.push("B")
    stack.pop()
    stack.pop()
    show_result("Condition 9: Stack should be empty after popping all items", True, stack.is_empty())

    # Condition 10: size() should return 0 for a new stack
    stack = ArrayStack()
    show_result("Condition 10: size() should return 0 for a new stack", 0, call_or_error(stack.size))

    # Condition 11: size() should update after push and pop
    stack = ArrayStack()
    stack.push("A")
    stack.push("B")
    stack.pop()
    show_result("Condition 11: size() should update after operations", 1, call_or_error(stack.size))

def test_stack_with_linked_list():
    # Group 4: Testing Stack with Linked List
    # Number of conditions being tested: 11

    section("TESTING STACK WITH LINKED LIST")

    # Condition 1: Test a new stack starts empty
    stack = LinkedListStack()
    show_result("Condition 1: New stack should be empty", True, stack.is_empty())

    # Condition 2: Pop from empty stack should return None
    stack = LinkedListStack()
    show_result("Condition 2: Pop from empty stack should return None", None, stack.pop())

    # Condition 3: Push one item should make stack not empty
    stack = LinkedListStack()
    stack.push("A")
    show_result("Condition 3: After push, stack should not be empty", False, stack.is_empty())

    # Condition 4: Pop should return the last pushed item
    stack = LinkedListStack()
    stack.push("A")
    show_result("Condition 4: Pop should return the pushed item", "A", stack.pop())

    # Condition 5: Push after emptying stack should still work
    stack = LinkedListStack()
    stack.push("A")
    stack.pop()
    stack.push("B")
    show_result("Condition 5: Stack should work after becoming empty", "B", stack.pop())

    # Condition 6: Stack should follow LIFO order
    stack = LinkedListStack()
    for item in ["A", "B", "C"]:
        stack.push(item)
    actual = [stack.pop(), stack.pop(), stack.pop()]
    show_result("Condition 6: Stack should follow LIFO order", ["C", "B", "A"], actual)

    # Condition 7: Stack should handle many items
    stack = LinkedListStack()
    for item in ["A", "B", "C", "D", "E", "F"]:
        stack.push(item)
    actual = [stack.pop(), stack.pop(), stack.pop(), stack.pop(), stack.pop(), stack.pop()]
    show_result("Condition 7: Stack should keep LIFO order with many items", ["F", "E", "D", "C", "B", "A"], actual)

    # Condition 8: Interleaved push and pop should keep order
    stack = LinkedListStack()
    stack.push("A")
    stack.push("B")
    first = stack.pop()
    stack.push("C")
    second = stack.pop()
    third = stack.pop()
    show_result("Condition 8: Interleaved push/pop should keep LIFO order", ["B", "C", "A"], [first, second, third])

    # Condition 9: Stack should be empty after removing all items
    stack = LinkedListStack()
    stack.push("A")
    stack.push("B")
    stack.pop()
    stack.pop()
    show_result("Condition 9: Stack should be empty after popping all items", True, stack.is_empty())

    # Condition 10: size() should return 0 for a new stack
    stack = LinkedListStack()
    show_result("Condition 10: size() should return 0 for a new stack", 0, stack.size())

    # Condition 11: size() should update after push and pop
    stack = LinkedListStack()
    stack.push("A")
    stack.push("B")
    stack.pop()
    show_result("Condition 11: size() should update after operations", 1, stack.size())

def main():
    test_queue_with_array()
    test_queue_with_linked_list()
    test_stack_with_array()
    test_stack_with_linked_list()

if __name__ == "__main__":
    main()
