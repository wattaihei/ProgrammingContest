import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Query.append((N, A, B))

for N, A, B in Query:
    ism = N
    isp = N
    for i, a in enumerate(A):
        if a < 0 and ism == N:
            ism = i
        if a > 0 and isp == N:
            isp = i
    ok = True
    for i, (a, b) in enumerate(zip(A, B)):
        if a > b and ism >= i:
            ok = False
        if a < b and isp >= i:
            ok = False
    print("YES" if ok else "NO")