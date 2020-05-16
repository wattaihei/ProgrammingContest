import numpy as np
import matplotlib.pyplot as plt 
import time

A = np.matrix([[0, 2], [5, 1]])

N = 100000
num = []
tim = []

for n in range(N):
    t0 = time.time()
    An = A**n
    t1 = time.time()
    num.append(n)
    tim.append(t1-t0)

plt.plot(num, tim)
plt.show()