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
