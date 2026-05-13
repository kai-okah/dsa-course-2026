def binary_search(a, key):
    low = 0
    high = len(a) - 1
    while high >= low:
        mid = (low + high) // 2
        if a[mid] > key:
            high = mid - 1
        elif a[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1

