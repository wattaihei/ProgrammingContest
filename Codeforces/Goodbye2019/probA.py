import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, K1, K2 = map(int, input().split())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    Query.append((N, K1, K2, A1, A2))

for N, K1, K2, A1, A2 in Query:
    ok = False
    for a in A1:
        if a == N:
            ok = True
    print("YES" if ok else "NO")