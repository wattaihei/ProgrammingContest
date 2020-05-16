from numpy.fft import rfft, irfft
import numpy as np

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

C = [0]*(10**5+1)
for a in A:
    C[a] += 1

L = 2*10**5+4

CC = rfft(np.array(C), L)
X = (irfft(CC*CC)+0.5).astype(int)
count = 0
ans = 0
for i in reversed(range(L)):
    x = X[i]
    if count + x >= M:
        ans += i*(M-count)
        break
    ans += i*x
    count += x

print(ans)