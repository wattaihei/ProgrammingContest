import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, k in Query:
    ok = k**2 <= n and (n-k)%2 == 0
    print("YES" if ok else "NO")