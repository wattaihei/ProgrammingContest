import math

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

checked = [False]*N

def dfs(L, s):
    if len(L) == N:
        k = 0
        for i in range(len(L)-1):
            a1, b1 = XY[L[i]]
            a2, b2 = XY[L[i+1]]
            k += math.sqrt((a1-a2)**2+(b1-b2)**2)
        return s+k
    for i in range(N):
        if not checked[i]:
            checked[i] = True
            s = dfs(L+[i], s)
            checked[i] = False
    return s

ans = dfs([], 0)
for n in range(1, N+1):
    ans /= n
print(ans)