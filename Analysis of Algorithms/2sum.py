import sys
import DSA

def count(a):
	N = len(a)
	count = 0
	for i in range(0,N):
		for j in range(i+1,N):
			if a[i] + a[j] == 0:
				count+=1
	return count

f = DSA.In(sys.argv[1]) 
a = f.readAllInts()
print(count(a))
