import sys
input = sys.stdin.readline

import math

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    tmp = N-1
    a = N-1; b = 1
    for t in range(2, int(math.sqrt(N))+2):
        if N%t == 0:
            x = t; y = N//t
            l = (x-1)*y
            if l !=0 and l < tmp:
                tmp = l
                a = (x-1)*y; b = y
            k = (y-1)*x
            if k != 0 and k < tmp:
                tmp = k
                a = x; b = (y-1)*x
    print(a, b)