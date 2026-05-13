def sort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        if mini != i:
            exchange(arr, mini, i)

def exchange(arr, mini, i):
    temp = arr[i]
    arr[i] = arr[mini]
    arr[mini] = temp

