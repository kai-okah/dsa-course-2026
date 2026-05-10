import sys, random
import DSA, Selection

N = int(sys.argv[1])
a = DSA.floatArray(N)
for i in range(N):
	a[i] = random.uniform(0,1)
Selection.sort(a)
for i in range(N):
	print(a[i])
