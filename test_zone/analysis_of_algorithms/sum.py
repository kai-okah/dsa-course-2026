from binary_search import binary_search

def sum_1(a):
    n = len(a)
    count = 0
    for i in range(0, n):
        if a[i] == 0:
            count += 1
    return count

def sum_2(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == 0:
                count += 1
    return count

def sum_3(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range (j+1,n):
                if a[i] + a[j] + a[k] == 0:
                    count += 1
    return count

def sum_3_fast(a):
    n = len(a)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            k = binary_search(a, -(a[i] + a[j]))
            if k > j:
                count += 1
    return count
