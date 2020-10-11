import sys
input = sys.stdin.readline


def solve(N, A):
    Ind = [-1]*(N+1)
    for i, a in enumerate(A):
        Ind[a] = i
    
    minind = N+1; maxind = -1
    for n in range(1, N+1):
        ind = Ind[n]
        if minind < ind < maxind:
            print("YES")
            print(minind+1, ind+1, maxind+1)
            return
        minind = min(minind, ind)
        maxind = max(maxind, ind)
    
    print("NO")
    return
    

Q = int(input())
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)

