import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]

for N, M in Query:
    print("YES" if N%M == 0 else "NO")