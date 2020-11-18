import numpy
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
print(numpy.inner(arr_1, arr_2))
print(numpy.outer(arr_1, arr_2))
