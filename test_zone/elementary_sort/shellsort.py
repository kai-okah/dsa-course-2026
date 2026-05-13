def exchange( arr, i, h):
    temp = arr[i]
    arr[i] = arr[h]
    arr[h] = temp

def sort(arr):
    size = len(arr)
    h = 1

    # Starts with biggest h
    while h < size // 3:
        h = (3 * h) + 1

    # Keep reducing the size of h
    while h >= 1:
        for i in range(h, size):
            j = i
            while j >= h:
                if arr[j - h] > arr[j]:
                    exchange(arr, j-h, j)
                j -= h
        h = h // 3


