import numpy

l = list(map(int, input().split()))
a = tuple(l)
print(numpy.zeros((a), dtype=numpy.int))
print(numpy.ones((a), dtype=numpy.int))
