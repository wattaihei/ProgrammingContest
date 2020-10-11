import sys
input = sys.stdin.readline
import math
Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    n2 = 0
    t = N
    while t%2 == 0:
        t //= 2
        n2 += 1
    ok = False
    for k in range(3, int(math.sqrt(t))+3):
        if t%k == 0 and t != k:
            ok = True
    print("FastestFinger" if ((t == 1) or (not ok and n2==1)) and N != 2 else "Ashishgup")