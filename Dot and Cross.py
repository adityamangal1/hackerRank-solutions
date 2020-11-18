import numpy
n = int(input())
arr1 = []
for i in range(n):
    f = list(map(int, input().split()))
    arr1.append(f)
arr2 = []
for i in range(n):
    l = list(map(int, input().split()))
    arr2.append(l)
print(numpy.dot(arr1, arr2))
