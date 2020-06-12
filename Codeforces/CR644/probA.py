import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b in Query:
    n1 = max(2*a, b)
    n2 = max(2*b, a)
    ans = min(n1, n2)**2
    print(ans)