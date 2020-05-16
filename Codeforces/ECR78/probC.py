import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    D = [-1]*(2*N+1)
    diff = 0
    D[0] = 0
    for i in range(N):
        if A[-i-1] == 1:
            diff += 1
        else:
            diff -= 1
        D[diff] = i+1
    
    ans = min(2*N, 2*N-D[0])
    diff = 0
    for i in range(N):
        if A[i] == 1:
            diff += 1
        else:
            diff -= 1
        if D[-diff] == -1:
            continue
        ans = min(ans, 2*N-D[-diff]-i-1)
    print(ans)