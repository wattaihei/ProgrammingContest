import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for n, x, y in Query:
    s = x+y
    ans1 = min(max(s-(n-1), 1), n)
    ans2 = min(s-1, n)
    print(ans1, ans2)