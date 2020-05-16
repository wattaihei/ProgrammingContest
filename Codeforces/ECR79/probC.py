import sys
input = sys.stdin.readline


Q = int(input())
Query = []
for _ in range(Q):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Query.append((N, M, A, B))

for N, M, A, B in Query:
    Ind = [None]*(N+1)
    for i, a in enumerate(A):
        Ind[a] = i
    
    max_ind = -1
    ans = 0
    for i, b in enumerate(B):
        if Ind[b] > max_ind:
            ans += 2*(Ind[b]-i)+1
            max_ind = Ind[b]
        else:
            ans += 1
    print(ans)