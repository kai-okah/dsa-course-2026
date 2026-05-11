def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while high >= low:
        mid = (high + low) // 2
        if array[mid] > item:
            high = mid - 1
        elif array[mid] < item:
            low = mid + 1
        else:
            return mid
    return -1
