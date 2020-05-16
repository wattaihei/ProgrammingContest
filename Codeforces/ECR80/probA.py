import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, K in Query:
    P = [N//2, N//2+1]
    ok = False
    for p in P:
        if p + (K+p)//(p+1) <= N:
            ok = True
            break
    print("YES" if ok else "NO")