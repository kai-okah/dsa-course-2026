from DSA import *
from WeightedQuickUnionPCUF import WeightedQuickUnionPCUF

n = stdReadInt()
uf = WeightedQuickUnionPCUF(n)

while not stdIsEmpty():
    p = stdReadInt()
    q = stdReadInt()

    if not uf.connected(p, q):
        uf.union(p, q)
        print (p, q)