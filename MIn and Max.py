import numpy
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    t = list(map(int, input().split()))
    a.append(t)
my_arr = numpy.min(a, axis=1)
print(numpy.max(my_arr, axis=None))
