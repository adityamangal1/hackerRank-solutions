import numpy
my_arr = list(map(float,input().split()))
value = int(input())
print(numpy.polyval(my_arr,value))