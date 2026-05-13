import random

import shuffle as shuffle_module
from test_helpers import call_or_error, section, show_result


def run_shuffle_tests():
    # Testing Shuffle
    # Number of conditions being tested: 6

    section("TESTING SHUFFLE")

    # Condition 1: Shuffle should keep the same length
    items = [1, 2, 3, 4, 5]
    random.seed(1)
    shuffle_module.shuffle(items)
    show_result(
        "Condition 1: Shuffle should keep the same length",
        5,
        len(items)
    )

    # Condition 2: Shuffle should keep the same items
    items = [1, 2, 3, 4, 5]
    random.seed(1)
    shuffle_module.shuffle(items)
    show_result(
        "Condition 2: Shuffle should keep the same items",
        [1, 2, 3, 4, 5],
        sorted(items)
    )

    # Condition 3: Shuffle should usually change order when seeded
    items = [1, 2, 3, 4, 5]
    random.seed(1)
    shuffle_module.shuffle(items)
    show_result(
        "Condition 3: Seeded shuffle should produce expected order",
        [4, 3, 1, 5, 2],
        items
    )

    # Condition 4: Empty list should stay empty
    items = []
    random.seed(1)
    shuffle_module.shuffle(items)
    show_result(
        "Condition 4: Empty list should stay empty",
        [],
        items
    )

    # Condition 5: One-item list should stay unchanged
    items = [42]
    random.seed(1)
    shuffle_module.shuffle(items)
    show_result(
        "Condition 5: One-item list should stay unchanged",
        [42],
        items
    )

    # Condition 6: Shuffle should return None and mutate the list
    items = [1, 2, 3]
    actual = call_or_error(lambda: shuffle_module.shuffle(items))
    show_result(
        "Condition 6: Shuffle should return None",
        None,
        actual
    )
