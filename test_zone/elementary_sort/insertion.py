def sort(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i, 0, -1):
            if arr[j-1] > arr [j]:
                exchange(arr, j, j-1)
            else: break
                
def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp