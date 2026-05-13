from stack_with_array import Stack as ArrayStack
from stack_with_single_linked_list import Stack as LinkedListStack
from test_helpers import call_or_error, section, show_result


def test_stack_with_array():
    # Testing Stack with Array
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
    # Testing Stack with Linked List
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


def run_stack_tests():
    test_stack_with_array()
    test_stack_with_linked_list()
