import numpy


numpy.set_printoptions(sign=' ')
x = list(map(float, input().split()))

my_arr = numpy.array(x)

print(numpy.floor(my_arr))
print(numpy.ceil(my_arr))
print(numpy.rint(my_arr))
