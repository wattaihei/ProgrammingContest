import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Query.append((N, M, A))

for N, M, A in Query:
    if N != M or N == 2:
        print(-1)
    else:
        print(2*sum(A))
        for i in range(M-1):
            print(i+1, i+2)
        print(M, 1)