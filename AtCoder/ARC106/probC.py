import sys
input = sys.stdin.buffer.readline

def solve(N, M):
    if N >= 2 and not 0 <= M <= N-2:
        print(-1)
        return
    k = N-M-1
    ans = [(1, 10**9)]
    for i in range(k):
        ans.append((i+2, 2*k-i+1))
    for i in range(M):
        ans.append((2*k+2+2*i, 2*k+2+2*i+1))
    
    for l, r in ans:
        print(l, r)

N, M = map(int, input().split())
solve(N, M)