from queue_with_array import Queue as ArrayQueue
from queue_with_single_linked_list import Queue as LinkedListQueue

# Number of test groups: 2
# Group 1: Queue with array
# Group 2: Queue with linked list

def show_result(test_name, expected, actual):
    print(test_name)
    print("Expected:", expected)
    print("Actual:  ", actual)

    if expected == actual:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print()

def test_queue_with_array():
    # Group 1: Testing Queue with Array
    # Number of conditions being tested: 10

    print("TESTING QUEUE WITH ARRAY")
    print("=" * 50)

    # Condition 1: Test a new queue starts empty
    queue = ArrayQueue()
    show_result(
        "Condition 1: New queue should be empty",
        True,
        queue.is_empty()
    )

    # Condition 2: Dequeue from empty queue should return None
    queue = ArrayQueue()
    show_result(
        "Condition 2: Dequeue from empty queue should return None",
        None,
        queue.dequeue()
    )

    # Condition 3: Enqueue one item should make queue not empty
    queue = ArrayQueue()
    queue.enqueue("A")
    show_result(
        "Condition 3: After enqueue, queue should not be empty",
        False,
        queue.is_empty()
    )

    # Condition 4: Dequeue should return the first item
    queue = ArrayQueue()
    queue.enqueue("A")
    removed_item = queue.dequeue()
    show_result(
        "Condition 4: Dequeue should return the first item",
        "A",
        removed_item
    )

    # Condition 5: Enqueue after emptying queue should not crash
    queue = ArrayQueue()

    try:
        queue.enqueue("A")
        queue.dequeue()
        queue.enqueue("B")
        actual = "No error"
    except Exception as error:
        actual = type(error).__name__

    show_result(
        "Condition 5: Enqueue after emptying queue should not crash",
        "No error",
        actual
    )

    # Condition 6: Queue should follow FIFO order
    queue = ArrayQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    actual = [
        queue.dequeue(),
        queue.dequeue(),
        queue.dequeue()
    ]

    show_result(
        "Condition 6: Queue should follow FIFO order",
        ["A", "B", "C"],
        actual
    )

    # Condition 7: Queue should grow when many items are added
    queue = ArrayQueue()

    try:
        queue.enqueue("A")
        queue.enqueue("B")
        queue.enqueue("C")
        queue.enqueue("D")

        actual = [
            queue.dequeue(),
            queue.dequeue(),
            queue.dequeue(),
            queue.dequeue()
        ]
    except Exception as error:
        actual = type(error).__name__

    show_result(
        "Condition 7: Queue should grow and keep FIFO order",
        ["A", "B", "C", "D"],
        actual
    )

    # Condition 8: Interleaved enqueue and dequeue should keep order
    queue = ArrayQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    first = queue.dequeue()
    queue.enqueue("C")
    second = queue.dequeue()
    third = queue.dequeue()

    actual = [first, second, third]

    show_result(
        "Condition 8: Interleaved enqueue/dequeue should keep FIFO order",
        ["A", "B", "C"],
        actual
    )

    # Condition 9: Queue should be empty after removing all items
    queue = ArrayQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.dequeue()
    queue.dequeue()

    show_result(
        "Condition 9: Queue should be empty after removing all items",
        True,
        queue.is_empty()
    )

    # Condition 10: size() should return 0 for a new queue
    queue = ArrayQueue()

    try:
        actual = queue.size()
    except Exception as error:
        actual = type(error).__name__

    show_result(
        "Condition 10: size() should return 0 for a new queue",
        0,
        actual
    )

def test_queue_with_linked_list():
    # Group 2: Testing Queue with Linked List
    # Number of conditions being tested: 10

    print("TESTING QUEUE WITH LINKED LIST")
    print("=" * 50)

    # Condition 1: Test a new queue starts empty
    queue = LinkedListQueue()
    show_result(
        "Condition 1: New queue should be empty",
        True,
        queue.is_empty()
    )

    # Condition 2: Dequeue from empty queue should return None
    queue = LinkedListQueue()
    show_result(
        "Condition 2: Dequeue from empty queue should return None",
        None,
        queue.dequeue()
    )

    # Condition 3: Enqueue one item should make queue not empty
    queue = LinkedListQueue()
    queue.enqueue("A")
    show_result(
        "Condition 3: After enqueue, queue should not be empty",
        False,
        queue.is_empty()
    )

    # Condition 4: Dequeue should return the first item
    queue = LinkedListQueue()
    queue.enqueue("A")
    removed_item = queue.dequeue()

    show_result(
        "Condition 4: Dequeue should return the first item",
        "A",
        removed_item
    )

    # Condition 5: After removing the only item, first and last should both be None
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.dequeue()

    actual = {
        "first_is_none": queue.first is None,
        "last_is_none": queue.last is None
    }

    expected = {
        "first_is_none": True,
        "last_is_none": True
    }

    show_result(
        "Condition 5: first and last should both be None after removing final item",
        expected,
        actual
    )

    # Condition 6: Enqueue after emptying queue should still work
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.dequeue()
    queue.enqueue("B")
    removed_item = queue.dequeue()

    show_result(
        "Condition 6: Enqueue after emptying should return the new item",
        "B",
        removed_item
    )

    # Condition 7: Queue should follow FIFO order
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    actual = [
        queue.dequeue(),
        queue.dequeue(),
        queue.dequeue()
    ]

    show_result(
        "Condition 7: Queue should follow FIFO order",
        ["A", "B", "C"],
        actual
    )

    # Condition 8: Interleaved enqueue and dequeue should keep order
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    first = queue.dequeue()
    queue.enqueue("C")
    second = queue.dequeue()
    third = queue.dequeue()

    actual = [first, second, third]

    show_result(
        "Condition 8: Interleaved enqueue/dequeue should keep FIFO order",
        ["A", "B", "C"],
        actual
    )

    # Condition 9: Queue should be empty after removing all items
    queue = LinkedListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.dequeue()
    queue.dequeue()

    actual = {
        "is_empty": queue.is_empty(),
        "first_is_none": queue.first is None,
        "last_is_none": queue.last is None
    }

    expected = {
        "is_empty": True,
        "first_is_none": True,
        "last_is_none": True
    }

    show_result(
        "Condition 9: Queue should be fully empty after removing all items",
        expected,
        actual
    )

    # Condition 10: size() should return 0 for a new queue
    queue = LinkedListQueue()

    try:
        actual = queue.size()
    except Exception as error:
        actual = type(error).__name__

    show_result(
        "Condition 10: size() should return 0 for a new queue",
        0,
        actual
    )

def main():
    test_queue_with_array()
    test_queue_with_linked_list()

if __name__ == "__main__":
	main()