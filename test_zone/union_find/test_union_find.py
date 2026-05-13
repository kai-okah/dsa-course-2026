from QuickFindUF import QuickFindUF
from QuickUnionUF import QuickUnionUF
from WeightedQuickUnionPCUF import WeightedQuickUnionPCUF
from WeightedQuickUnionUF import WeightedQuickUnionUF
from test_helpers import call_or_error, section, show_result


def ids_as_list(uf):
    return list(uf.id)


def roots_for_all_items(uf, n):
    return [uf.find(i) for i in range(n)]


def test_union_find(uf_class, name):
    # Number of conditions being tested for this union-find class: 10

    section("TESTING " + name)

    # Condition 1: New structure should start with every item in its own component
    uf = uf_class(5)
    show_result("Condition 1: Initial id array should contain each item itself", [0, 1, 2, 3, 4], ids_as_list(uf))

    # Condition 2: find(i) should return i before any unions
    uf = uf_class(5)
    show_result("Condition 2: find(i) should return i before unions", [0, 1, 2, 3, 4], roots_for_all_items(uf, 5))

    # Condition 3: Different items should not be connected at the start
    uf = uf_class(5)
    show_result("Condition 3: Different items should not be connected at first", False, uf.connected(0, 1))

    # Condition 4: An item should always be connected to itself
    uf = uf_class(5)
    show_result("Condition 4: An item should be connected to itself", True, uf.connected(3, 3))

    # Condition 5: union(p, q) should connect p and q
    uf = uf_class(5)
    uf.union(0, 1)
    show_result("Condition 5: union(0, 1) should connect 0 and 1", True, uf.connected(0, 1))

    # Condition 6: Connections should be transitive
    uf = uf_class(5)
    uf.union(0, 1)
    uf.union(1, 2)
    show_result("Condition 6: If 0-1 and 1-2 are connected, 0-2 should be connected", True, uf.connected(0, 2))

    # Condition 7: Separate components should stay separate
    uf = uf_class(6)
    uf.union(0, 1)
    uf.union(2, 3)
    actual = {
        "0_connected_1": uf.connected(0, 1),
        "2_connected_3": uf.connected(2, 3),
        "0_connected_3": uf.connected(0, 3)
    }
    expected = {
        "0_connected_1": True,
        "2_connected_3": True,
        "0_connected_3": False
    }
    show_result("Condition 7: Separate groups should not become connected by accident", expected, actual)

    # Condition 8: Repeated union on already connected items should not break anything
    uf = uf_class(5)
    uf.union(0, 1)
    uf.union(0, 1)
    uf.union(1, 0)
    show_result("Condition 8: Repeated union should keep items connected", True, uf.connected(0, 1))

    # Condition 9: All items should be connected after enough unions
    uf = uf_class(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)
    actual = [uf.connected(0, i) for i in range(5)]
    show_result("Condition 9: All items should become connected", [True, True, True, True, True], actual)

    # Condition 10: Invalid positive index should raise IndexError
    uf = uf_class(5)
    actual = call_or_error(lambda: uf.connected(0, 5))
    show_result("Condition 10: Using index 5 in a size-5 structure should raise IndexError", "IndexError", actual)


def run_union_find_tests():
    test_union_find(QuickFindUF, "QUICK FIND")
    test_union_find(QuickUnionUF, "QUICK UNION")
    test_union_find(WeightedQuickUnionUF, "WEIGHTED QUICK UNION")
    test_union_find(WeightedQuickUnionPCUF, "WEIGHTED QUICK UNION WITH PATH COMPRESSION")
