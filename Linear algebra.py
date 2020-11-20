import numpy
x = int(input())
arr = []
numpy.set_printoptions(legacy="1.13")
for i in range(x):
    l = list(map(float, input().split()))
    arr.append(l)
print(numpy.linalg.det(arr))
