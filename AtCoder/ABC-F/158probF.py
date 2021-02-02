import sys
input = sys.stdin.readline
# from bisect import bisect_left

mod = 998244353
INF = 10**18

N = int(input())
XD = [list(map(int, input().rstrip().split())) for _ in range(N)]
XD.sort(reverse=True)


nowhas = 0
stack = []
for x, d in XD:
    to_app = nowhas + 1
    while stack and stack[-1][0] < x+d:
        _, dd = stack.pop()
        nowhas = (nowhas - dd) % mod
    nowhas = (nowhas + to_app) % mod
    stack.append((x, to_app))

ans = 1
for _, d in stack:
    ans = (ans + d) % mod

print(ans)