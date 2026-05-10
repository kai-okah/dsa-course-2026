def exch(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t

def sort(a):
	N = len(a)
	for i in range(N):
		min = i
		for j in range(i+1,N):
			if a[j] < a[min]:
				min = j
		exch(a, i, min)
	
	