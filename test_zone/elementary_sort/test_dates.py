from date import Date
from test_helpers import section, show_result


def run_date_tests():
    # Testing Date
    # Number of conditions being tested: 6

    section("TESTING DATE")

    # Condition 1: Earlier year should be less than later year
    show_result(
        "Condition 1: Earlier year should be less than later year",
        True,
        Date(1, 1, 2020) < Date(1, 1, 2021)
    )

    # Condition 2: Same year, earlier month should be less than later month
    show_result(
        "Condition 2: Earlier month should be less when years match",
        True,
        Date(1, 3, 2020) < Date(1, 4, 2020)
    )

    # Condition 3: Same month and year, earlier day should be less
    show_result(
        "Condition 3: Earlier day should be less when month and year match",
        True,
        Date(3, 4, 2020) < Date(4, 4, 2020)
    )

    # Condition 4: Later date should not be less than earlier date
    show_result(
        "Condition 4: Later date should not be less than earlier date",
        False,
        Date(4, 4, 2020) < Date(3, 4, 2020)
    )

    # Condition 5: Equal dates should not be less than each other
    show_result(
        "Condition 5: Equal dates should not be less than each other",
        False,
        Date(4, 4, 2020) < Date(4, 4, 2020)
    )

    # Condition 6: Date representation should use day/month/year
    show_result(
        "Condition 6: repr should show day/month/year",
        "4/5/2020",
        repr(Date(4, 5, 2020))
    )
