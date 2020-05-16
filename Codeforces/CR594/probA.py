import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    P1 = list(map(int, input().split()))
    M = int(input())
    P2 = list(map(int, input().split()))
    Query.append((N, M, P1, P2))

for N, M, P1, P2 in Query:
    a = [0, 0]
    b = [0, 0]
    for p in P1:
        a[p%2] += 1
    for q in P2:
        b[q%2] += 1
    print(a[0]*b[0]+a[1]*b[1])