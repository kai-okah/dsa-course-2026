from array import array

from sum import sum_1, sum_2, sum_3, sum_3_fast
from test_helpers import call_or_error, section, show_result


def run_sum_1_tests():
    # Testing 1-Sum
    # Number of conditions being tested: 6

    section("TESTING 1-SUM")

    # Condition 1: One zero should count as one match
    show_result(
        "Condition 1: One zero should count as one match",
        1,
        call_or_error(lambda: sum_1(array("i", [4, 0, 7])))
    )

    # Condition 2: Multiple zeros should all be counted
    show_result(
        "Condition 2: Multiple zeros should all be counted",
        3,
        call_or_error(lambda: sum_1(array("i", [0, 5, 0, -2, 0])))
    )

    # Condition 3: No zero should return 0
    show_result(
        "Condition 3: No zero should return 0",
        0,
        call_or_error(lambda: sum_1(array("i", [1, 2, 3, 4])))
    )

    # Condition 4: Empty array should return 0
    show_result(
        "Condition 4: Empty array should return 0",
        0,
        call_or_error(lambda: sum_1(array("i", [])))
    )

    # Condition 5: A single zero should return 1
    show_result(
        "Condition 5: Single zero array should return 1",
        1,
        call_or_error(lambda: sum_1(array("i", [0])))
    )

    # Condition 6: A single non-zero item should return 0
    show_result(
        "Condition 6: Single non-zero array should return 0",
        0,
        call_or_error(lambda: sum_1(array("i", [9])))
    )


def run_sum_2_tests():
    # Testing 2-Sum
    # Number of conditions being tested: 7

    section("TESTING 2-SUM")

    # Condition 1: One pair should be counted
    show_result(
        "Condition 1: One pair that sums to zero should be counted",
        1,
        call_or_error(lambda: sum_2(array("i", [-3, 1, 3, 5])))
    )

    # Condition 2: Multiple pairs should be counted
    show_result(
        "Condition 2: Multiple zero-sum pairs should be counted",
        3,
        call_or_error(lambda: sum_2(array("i", [-3, -2, -1, 1, 2, 3])))
    )

    # Condition 3: No pairs should return 0
    show_result(
        "Condition 3: No zero-sum pairs should return 0",
        0,
        call_or_error(lambda: sum_2(array("i", [1, 2, 3, 4])))
    )

    # Condition 4: Two zeros should count as one pair
    show_result(
        "Condition 4: Two zeros should count as one pair",
        1,
        call_or_error(lambda: sum_2(array("i", [0, 0])))
    )

    # Condition 5: Three zeros should count as three pairs
    show_result(
        "Condition 5: Three zeros should count every index pair",
        3,
        call_or_error(lambda: sum_2(array("i", [0, 0, 0])))
    )

    # Condition 6: Empty array should return 0
    show_result(
        "Condition 6: Empty array should return 0",
        0,
        call_or_error(lambda: sum_2(array("i", [])))
    )

    # Condition 7: One-item array should return 0
    show_result(
        "Condition 7: One-item array should return 0",
        0,
        call_or_error(lambda: sum_2(array("i", [0])))
    )


def run_sum_3_tests():
    # Testing 3-Sum
    # Number of conditions being tested: 8

    section("TESTING 3-SUM")

    # Condition 1: One triple should be counted
    show_result(
        "Condition 1: One triple that sums to zero should be counted",
        1,
        call_or_error(lambda: sum_3(array("i", [-3, 1, 2, 5])))
    )

    # Condition 2: Multiple triples should be counted
    show_result(
        "Condition 2: Multiple zero-sum triples should be counted",
        2,
        call_or_error(lambda: sum_3(array("i", [-4, -1, 0, 1, 2, 3])))
    )

    # Condition 3: No triples should return 0
    show_result(
        "Condition 3: No zero-sum triples should return 0",
        0,
        call_or_error(lambda: sum_3(array("i", [1, 2, 3, 4])))
    )

    # Condition 4: Three zeros should count as one triple
    show_result(
        "Condition 4: Three zeros should count as one triple",
        1,
        call_or_error(lambda: sum_3(array("i", [0, 0, 0])))
    )

    # Condition 5: Four zeros should count every index triple
    show_result(
        "Condition 5: Four zeros should count four triples",
        4,
        call_or_error(lambda: sum_3(array("i", [0, 0, 0, 0])))
    )

    # Condition 6: Empty array should return 0
    show_result(
        "Condition 6: Empty array should return 0",
        0,
        call_or_error(lambda: sum_3(array("i", [])))
    )

    # Condition 7: Two-item array should return 0
    show_result(
        "Condition 7: Two-item array should return 0",
        0,
        call_or_error(lambda: sum_3(array("i", [-1, 1])))
    )

    # Condition 8: Repeated values should count different index triples
    show_result(
        "Condition 8: Repeated values should count different valid triples",
        4,
        call_or_error(lambda: sum_3(array("i", [-1, -1, 0, 1, 1])))
    )


def run_sum_3_fast_tests():
    # Testing Fast 3-Sum
    # Number of conditions being tested: 8
    # Important: sum_3_fast uses binary search, so the array must be sorted.

    section("TESTING FAST 3-SUM")

    # Condition 1: One sorted triple should be counted
    show_result(
        "Condition 1: One sorted triple that sums to zero should be counted",
        1,
        call_or_error(lambda: sum_3_fast(array("i", [-3, 1, 2, 5])))
    )

    # Condition 2: Multiple sorted triples should be counted
    show_result(
        "Condition 2: Multiple sorted zero-sum triples should be counted",
        2,
        call_or_error(lambda: sum_3_fast(array("i", [-4, -1, 0, 1, 2, 3])))
    )

    # Condition 3: No triples should return 0
    show_result(
        "Condition 3: No zero-sum triples should return 0",
        0,
        call_or_error(lambda: sum_3_fast(array("i", [1, 2, 3, 4])))
    )

    # Condition 4: Three zeros should count as one triple
    show_result(
        "Condition 4: Three zeros should count as one triple",
        1,
        call_or_error(lambda: sum_3_fast(array("i", [0, 0, 0])))
    )

    # Condition 5: Four zeros should count every index triple
    show_result(
        "Condition 5: Four zeros should count four triples",
        4,
        call_or_error(lambda: sum_3_fast(array("i", [0, 0, 0, 0])))
    )

    # Condition 6: Empty array should return 0
    show_result(
        "Condition 6: Empty array should return 0",
        0,
        call_or_error(lambda: sum_3_fast(array("i", [])))
    )

    # Condition 7: Two-item array should return 0
    show_result(
        "Condition 7: Two-item array should return 0",
        0,
        call_or_error(lambda: sum_3_fast(array("i", [-1, 1])))
    )

    # Condition 8: Fast 3-sum should match normal 3-sum on sorted input
    items = array("i", [-8, -4, -2, -1, 0, 1, 2, 3, 5])
    expected = call_or_error(lambda: sum_3(items))
    actual = call_or_error(lambda: sum_3_fast(items))
    show_result(
        "Condition 8: Fast 3-sum should match normal 3-sum on sorted input",
        expected,
        actual
    )


def run_sum_tests():
    run_sum_1_tests()
    run_sum_2_tests()
    run_sum_3_tests()
    run_sum_3_fast_tests()
