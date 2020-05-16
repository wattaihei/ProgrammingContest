import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    S = list(map(int, list(input().rstrip())))
    Query.append((N, S))

for N, S in Query:
    A = []
    for s in S:
        if s % 2 == 1:
            A.append(s)
    if len(A) < 2:
        print(-1)
    else:
        print(str(A[0])+str(A[1]))