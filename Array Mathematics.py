import numpy
n, m = map(int, input().split())
ar1 = []
ar2 = []
for i in range(n):
    tmp = list(map(int, input().split()))
    ar1.append(tmp)
for i in range(n):
    tmp = list(map(int, input().split()))
    ar2.append(tmp)
np_ar1 = numpy.array(ar1)
np_ar2 = numpy.array(ar2)
print(numpy.add(np_ar1, np_ar2))
print(numpy.subtract(np_ar1, np_ar2))
print(numpy.multiply(np_ar1, np_ar2))
print(numpy.floor_divide(np_ar1, np_ar2))
print(numpy.mod(np_ar1, np_ar2))
print(numpy.power(np_ar1, np_ar2))
