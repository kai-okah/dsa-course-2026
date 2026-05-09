import sys
import DSA

def count(a):
	N = len(a)
	count = 0
	for i in range(0,N):
		if a[i] == 0:
			count+=1
	return count

f = DSA.In(sys.argv[1])
a = f.readAllInts()
print(count(a))
