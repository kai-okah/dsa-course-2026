from DSA import *

class WeightedQuickUnionUF:
	def __init__(self, n):
		self.id = intArray(n)
		self.sz = intArray(n)
		for i in range(len(self.id)):
			self.id[i] = i
			self.sz[i] = 1

   # ...
	
	def find(self, i):
		while i != self.id[i]: i = self.id[i]
		return i

	def union(self, p, q):
		i = self.find(p)
		j = self.find(q)
		if i == j:return
		if self.sz[i] < self.sz[j]:
			self.id[i] = j
			self.sz[j] += self.sz[i]
		else:
			self.id[j] = i
			self.sz[i] += self.sz[j]
				
	def connected(self, p, q):
		return self.find(p) == self.find(q)

n = stdReadInt()
uf = WeightedQuickUnionUF(n)
while not stdIsEmpty():
	p = stdReadInt()
	q = stdReadInt()
	if not uf.connected(p, q):
		uf.union(p, q)
		print(p,q)
