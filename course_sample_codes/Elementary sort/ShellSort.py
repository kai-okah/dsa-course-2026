def exch(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t

def sort(a):
	N = len(a)
	h = 1
	while h < N//3:  h = 3*h + 1 # 1, 4, 13, 40, 121, 364, ...
	while h >= 1: #  h-sort the array.
		for i in range(h,N):
			j = i
			while j >= h and a[j] < a[j-h]:				
				exch(a, j, j-h)
				j -= h
		h = h//3