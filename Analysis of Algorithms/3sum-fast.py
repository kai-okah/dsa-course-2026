import sys
import DSA

def binSearch(a,e):
	lo = 0
	hi = len(a)-1
	while hi >= lo:
		mid =  lo+(hi-lo)//2
		if e > a[mid]:
			lo = mid+1
		elif e < a[mid]:
			hi = mid-1
		else:
			return mid
	return -1



def count(a):
	N = len(a)
	a.sort()
	count = 0
	for i in range(0,N):
		for j in range(i+1,N):
			k = binSearch(a, -(a[i] + a[j]))
			if k > j: count += 1
					
	return count

f = DSA.In(sys.argv[1])
a = f.readAllInts()
print(count(a))
