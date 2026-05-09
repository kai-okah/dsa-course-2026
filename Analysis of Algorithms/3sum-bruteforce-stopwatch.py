import sys
import DSA

def count(a):
	N = len(a)
	count = 0
	for i in range(0,N):
		for j in range(i+1,N):
			for k in range(j+1,N):
				if a[i] + a[j] + a[k] == 0:
					count+=1
	return count

f = DSA.In(sys.argv[1])
a = f.readAllInts()
s = DSA.Stopwatch()
c = count(a)
time = s.elapsedTime()
print("elapsed time:",f"{time:.2f}","seconds")
print(c)
