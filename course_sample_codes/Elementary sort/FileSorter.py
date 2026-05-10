import sys
import DSA, Selection

a = DSA.readFiles(sys.argv[1])
Selection.sort(a)
for e in a:
	print(e)