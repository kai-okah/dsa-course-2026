import random

def exchange(arr, i, r):
    temp = arr[i]
    arr[i] = arr[r]
    arr[r] = temp


def shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, i)
        exchange(arr, i, r)

        