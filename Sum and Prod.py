import numpy
n, m = map(int, input().split())
a = []

for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

my_arr = numpy.array(a)
a = numpy.sum(my_arr, axis=0)
print(numpy.prod(a, axis=None))
