import sys
input = sys.stdin.readline

N, X, T = map(int, input().split())
ans = (N+X-1)//X * T
print(ans)