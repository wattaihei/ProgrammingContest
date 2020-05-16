import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    P = set(map(int, input().split()))
    Query.append((N, M, A, P))

for N, M, A, P in Query:
    must = [False]*N
    for i, a in enumerate(A):
        cl = False
        for j in range(i):
            if cl or A[j] > a:
                cl = True
                must[j] = True
    ok = True
    for i in range(N):
        if must[i] and not i+1 in P:
            ok = False
    print("YES" if ok else "NO")