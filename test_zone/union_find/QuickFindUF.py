from array import array
from UF import UF

class QuickFindUF(UF):

    def __init__(self, n):
        self.id = array("i", [0]*n)
        for i, value in enumerate(self.id):
            self.id[i] = i

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        p_id = self.id[p]
        q_id = self.id[q]
        for i, value in enumerate(self.id):
            if self.id[i] == p_id:
                self.id[i] = q_id