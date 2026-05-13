from date import Date
import insertion
import selection
import shellsort
from test_helpers import call_or_error, section, show_result


def date_strings(items):
    return [repr(item) for item in items]


def run_sort_case(sort_name, sort_function, condition, original, expected):
    items = list(original)

    def sort_items():
        result = sort_function(items)
        return {
            "return_value": result,
            "items": items
        }

    show_result(
        f"{condition}: {sort_name}",
        {
            "return_value": None,
            "items": expected
        },
        call_or_error(sort_items)
    )


def run_date_sort_case(sort_name, sort_function, condition):
    items = [
        Date(5, 5, 2020),
        Date(1, 1, 2019),
        Date(3, 5, 2020),
        Date(1, 2, 2019)
    ]

    def sort_items():
        result = sort_function(items)
        return {
            "return_value": result,
            "items": date_strings(items)
        }

    show_result(
        f"{condition}: {sort_name}",
        {
            "return_value": None,
            "items": ["1/1/2019", "1/2/2019", "3/5/2020", "5/5/2020"]
        },
        call_or_error(sort_items)
    )


def run_tests_for_sort(sort_name, sort_function):
    # Number of conditions being tested per sort: 8

    # Condition 1: Sort an unsorted list of numbers
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 1: Unsorted numbers should be sorted",
        [6, 7, 5, 3, 4, 10, 2, 9, 8],
        [2, 3, 4, 5, 6, 7, 8, 9, 10]
    )

    # Condition 2: Already sorted list should stay sorted
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 2: Already sorted numbers should stay sorted",
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    )

    # Condition 3: Reverse sorted list should be sorted
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 3: Reverse sorted numbers should be sorted",
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    )

    # Condition 4: Duplicate values should be sorted correctly
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 4: Duplicate values should be sorted",
        [3, 1, 2, 3, 1],
        [1, 1, 2, 3, 3]
    )

    # Condition 5: Negative values should be sorted correctly
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 5: Negative values should be sorted",
        [0, -5, 3, -1, 2],
        [-5, -1, 0, 2, 3]
    )

    # Condition 6: Empty list should stay empty
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 6: Empty list should stay empty",
        [],
        []
    )

    # Condition 7: One-item list should stay unchanged
    run_sort_case(
        sort_name,
        sort_function,
        "Condition 7: One-item list should stay unchanged",
        [42],
        [42]
    )

    # Condition 8: Sort should work with Date objects
    run_date_sort_case(
        sort_name,
        sort_function,
        "Condition 8: Date objects should be sorted by year, month, then day"
    )


def run_sort_tests():
    section("TESTING SELECTION SORT")
    run_tests_for_sort("selection.sort", selection.sort)

    section("TESTING INSERTION SORT")
    run_tests_for_sort("insertion.sort", insertion.sort)

    section("TESTING SHELLSORT")
    run_tests_for_sort("shellsort.sort", shellsort.sort)
