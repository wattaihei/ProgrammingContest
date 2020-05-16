import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, R = map(int, input().split())
    A = set(map(int, input().split()))
    Query.append((N, R, A))

for N, R, A in Query:
    B = sorted(list(A), reverse=True)
    c = 0
    for b in B:
        if b - c*R > 0:
            c += 1
    print(c)
