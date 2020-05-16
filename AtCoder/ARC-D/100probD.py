import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
INF = 10**18

S = sum(A)

def dfs(ind, part, remain, prob):
    if part == 1:
        prob.append(remain)
        return max(prob)-min(prob)
    s = 0
    while s*part < remain and ind <= N-part:
        s += A[ind]
        ind += 1
    if s > A[ind-1]:
        a1 = dfs(ind-1, part-1, remain-s+A[ind-1], prob+[s-A[ind-1]])
    else:
        a1 = INF
    a2 = dfs(ind, part-1, remain-s, prob+[s])
    return min(a1, a2)

ans = dfs(0, 4, S, [])
print(ans)