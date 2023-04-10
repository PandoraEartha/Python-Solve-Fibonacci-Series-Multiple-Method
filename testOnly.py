import numpy

A=numpy.array([[1,1],[1,0]],dtype=object)
power=numpy.linalg.matrix_power(A,10000)
print(power)