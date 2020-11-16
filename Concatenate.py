import numpy
n, m, p = list(map(int, input().split()))
a = []
for i in range(n+m):
    user = list(map(int, input().split()))
    a.append(user)
my_arr = numpy.array(a)
print(my_arr)
