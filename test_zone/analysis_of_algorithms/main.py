from array import array

from binary_search import binary_search


# Number of test groups: 1
# Group 1: Binary search


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


def test_binary_search():
    # Group 1: Testing Binary Search
    # Number of conditions being tested: 12

    section("TESTING BINARY SEARCH")

    items = array("i", [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97])

    # Condition 1: Search for an item in the middle of the array
    show_result(
        "Condition 1: Search should find an item in the middle",
        6,
        call_or_error(lambda: binary_search(items, 51))
    )

    # Condition 2: Search for the first item in the array
    show_result(
        "Condition 2: Search should find the first item",
        0,
        call_or_error(lambda: binary_search(items, 6))
    )

    # Condition 3: Search for the last item in the array
    show_result(
        "Condition 3: Search should find the last item",
        14,
        call_or_error(lambda: binary_search(items, 97))
    )

    # Condition 4: Search for an item that is not in the array
    show_result(
        "Condition 4: Search should return -1 when the item is missing",
        -1,
        call_or_error(lambda: binary_search(items, 52))
    )

    # Condition 5: Search for an item smaller than every array item
    show_result(
        "Condition 5: Search should return -1 for an item below the range",
        -1,
        call_or_error(lambda: binary_search(items, 1))
    )

    # Condition 6: Search for an item larger than every array item
    show_result(
        "Condition 6: Search should return -1 for an item above the range",
        -1,
        call_or_error(lambda: binary_search(items, 100))
    )

    # Condition 7: Search in an empty array
    empty_items = array("i", [])
    show_result(
        "Condition 7: Search in an empty array should return -1",
        -1,
        call_or_error(lambda: binary_search(empty_items, 10))
    )

    # Condition 8: Search in an array with one matching item
    one_item = array("i", [42])
    show_result(
        "Condition 8: Search should find the only item",
        0,
        call_or_error(lambda: binary_search(one_item, 42))
    )

    # Condition 9: Search in an array with one non-matching item
    one_item = array("i", [42])
    show_result(
        "Condition 9: Search should return -1 when the only item is different",
        -1,
        call_or_error(lambda: binary_search(one_item, 7))
    )

    # Condition 10: Search should work with an even number of items
    even_items = array("i", [1, 2, 3, 4, 5, 6])
    show_result(
        "Condition 10: Search should work with an even-sized array",
        3,
        call_or_error(lambda: binary_search(even_items, 4))
    )

    # Condition 11: Search should work with negative numbers
    negative_items = array("i", [-10, -5, 0, 8, 12])
    show_result(
        "Condition 11: Search should work with negative numbers",
        1,
        call_or_error(lambda: binary_search(negative_items, -5))
    )

    # Condition 12: Search with duplicates should return an index containing the item
    duplicate_items = array("i", [1, 2, 2, 2, 3])
    index = call_or_error(lambda: binary_search(duplicate_items, 2))

    if isinstance(index, int) and index != -1:
        actual = duplicate_items[index] == 2
    else:
        actual = index

    show_result(
        "Condition 12: Search with duplicates should find the target value",
        True,
        actual
    )


def main():
    test_binary_search()


if __name__ == "__main__":
    main()
