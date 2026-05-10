import random

def exch(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t

def shuffle(a):
	N = len(a)
	for i in range(N):
		r = random.randint(0, i)
		exch(a, i, r)

if __name__ == "__main__":
	a = [1,2,3,4,5,6,7,8]
	shuffle(a)
	print(a)