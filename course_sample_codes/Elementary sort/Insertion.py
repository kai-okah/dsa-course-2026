def exch(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t

def sort(a):
	N = len(a)
	for i in range(N):
		for j in range(i,0,-1):
			if a[j] < a[j-1]:
				exch(a, j, j-1)
			else:
				break
