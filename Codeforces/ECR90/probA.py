import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for A, B, C in Query:
    a1 = -1
    if A < C:
        a1 = 1
    a2 = -1
    if A*B > C:
        a2 = B
    print(a1, a2)