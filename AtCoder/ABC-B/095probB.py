N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

A = X - sum(M)
print(N + A//min(M))