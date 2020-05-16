import sys
input = sys.stdin.readline


Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, X, a, b in Query:
    print(min(N-1, abs(a-b)+X))