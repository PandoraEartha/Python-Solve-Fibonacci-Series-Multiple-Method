import time

import recursion
import loop
import binaryExponentiation

start=time.time()
n=10000000
print(binaryExponentiation.fibonacci(n))
end=time.time()
print('TIME CONSUMPTION: ',end-start,'s')
