import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Query.append((N, A, B))

for N, A, B in Query:
    A.sort()
    B.sort()
    print(*A)
    print(*B)