import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    t = 4
    while True:
        if N%(t-1) == 0:
            break
        t *= 2
    print(N//(t-1))