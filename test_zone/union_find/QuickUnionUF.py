from UF import UF
from array import array

class QuickUnionUF(UF):

    def __init__(self, n):
        self.id = array("i", [0]*n)
        for i , value in enumerate(self.id):
            self.id[i] = i

    def find(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        self.id[p_id] = q_id
