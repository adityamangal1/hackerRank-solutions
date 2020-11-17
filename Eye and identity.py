import numpy
numpy.set_printoptions(legacy='1.13')
m, n = list(map(int, input().split()))
print(numpy.eye(m, n))
