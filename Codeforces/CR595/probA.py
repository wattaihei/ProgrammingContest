import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    C = set(A)
    ok = True
    for c in C:
        if c+1 in C or c-1 in C:
            ok = False
    print(1 if ok else 2)