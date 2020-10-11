import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for a, b, n in Query:
    if a < b:
        a, b = b, a
    ans = 0
    while a <= n:
        a, b = b+a, a
        ans += 1
    print(ans)