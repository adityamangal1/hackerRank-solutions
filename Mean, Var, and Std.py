import numpy
n, m = list(map(int, input().split()))
my_arr = []
for i in range(n):
    t = list(map(int, input().split()))
    my_arr.append(t)
print(numpy.mean(my_arr, axis=1))
print(numpy.var(my_arr, axis=0))
print(numpy.around(numpy.std(my_arr), 11))
