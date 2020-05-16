import sys
input = sys.stdin.readline

Q = int(input())
Query = [int(input()) for _ in range(Q)]

for N in Query:
    c = 0
    for n in range(1, 10):
        for m in range(1, 10):
            a = int(str(m)*n)
            if N >= a:
                c += 1
    print(c)