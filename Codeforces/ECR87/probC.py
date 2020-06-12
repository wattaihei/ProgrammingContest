import math

import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]


def get(N, theta):
    r = 1/(2*math.sin(math.pi/N))
    return 2*max(r*math.cos(theta), r*math.cos(math.pi/N-theta))

for N in Query:
    if N%2 == 0:
        print(1/math.tan(math.pi/(N*2)))
    else:
        N *= 2
        l1 = 0
        l2 = math.pi/N
        while l2 - l1 > 10**(-15):
            m1 = (2*l1+l2)/3
            m2 = (l1+2*l2)/3
            s_l1 = get(N, l1)
            s_l2 = get(N, l2)
            if s_l1 >= s_l2:
                l1 = m1
            else:
                l2 = m2
        print(get(N, l1))