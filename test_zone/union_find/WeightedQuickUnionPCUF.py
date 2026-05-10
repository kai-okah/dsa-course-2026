from UF import UF
from array import array

class WeightedQuickUnionPCUF(UF):

    def __init__(self, n):
        self.id = array("i", [0]*n)
        self.weight = array("i", [1]*n)
        for i in range(len(self.id)):
            self.id[i] = i

    def find(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def union(self, p, q):
        q_id = self.find(q)
        p_id = self.find(p)
        if self.weight[p_id] > self.weight[q_id]:
            self.id[q_id] = p_id
            self.weight[p_id] += self.weight[q_id]
        else:
            self.id[p_id] = q_id
            self.weight[q_id] += self.weight[p_id]
