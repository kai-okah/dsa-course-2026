import random

class Date:
	def __init__(self, d, m, y):
		self.d = d
		self.m = m
		self.y = y
	
	def __lt__(self, other):
		if self.y < other.y: return True
		if self.y > other.y: return False
		if self.m < other.m: return True
		if self.m > other.m: return False
		return self.d < other.d
		
	def __repr__(self):
		return str(self.m) + "/" + str(self.d) + "/" + str(self.y)

# ...

if __name__ == "__main__":
	a = []
	for i in range(10):
		a += [Date(random.randint(1,28), random.randint(1,12), random.randint(1900,2100))]
	print(a)
	a.sort()
	print(a)
