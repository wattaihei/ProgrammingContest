from numpy.fft import rfft, irfft
import numpy as np

import sys
input = sys.stdin.readline

N = int(input())
AB = np.array([list(map(int, input().split())) for _ in range(N)], np.int32)
A = AB[:, 0]
B = AB[:, 1]

fft_len = 2*10**5

AA = rfft(A, fft_len)
BB = rfft(B, fft_len)
#XX = np.array([i for i in range(len(AA))])
X = (irfft(AA*BB)[:2*N-1]+0.5).astype(int)
print(0)
for x in X:
    print(x)