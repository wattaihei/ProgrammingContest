import numpy as np
from numpy.fft import rfft, irfft

p = int(input())
n = int(input())

L = [0]*p
for x in range(p):
    L[pow(x, n, p)] += 1

A = np.array(L, np.int32)
iA = rfft(A, 2*p)
X = (irfft(iA*iA)[:2*p]+0.5).astype(int)
ans = 0
for x in range(2*p):
    ans += X[x] * L[x%p]
print(ans)