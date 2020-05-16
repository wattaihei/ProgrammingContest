N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]


def dfs1(i, p1=[], p2=[], p3=[], ans=[]):
    #print(i)
    if i == N:
        if len(p1) != 0 and len(p2) != 0 and len(p3)!= 0:
            ans.append([p1, p2, p3])
        return ans
    l = L[i]
    ans = dfs1(i+1, p1+[l], p2, p3, ans)
    ans = dfs1(i+1, p1, p2+[l], p3, ans)
    ans = dfs1(i+1, p1, p2, p3+[l], ans)
    ans = dfs1(i+1, p1, p2, p3, ans)
    return ans

def dfs2(R, L=[], ans=[]):
    if len(L) == 3:
        ans.append(L)
        return ans
    for r in R:
        if not r in L:
            ans = dfs2(R, L+[r], ans)
    return ans

indexes = dfs2([0, 1, 2])

ans = int(1E18)
for (p1, p2, p3) in dfs1(0):
    S = [sum(p1), sum(p2), sum(p3)]
    for i1, i2, i3 in indexes:
        p = abs(A-S[i1]) + abs(B-S[i2]) + abs(C-S[i3]) + (len(p1)+len(p2)+len(p3) - 3)*10
        ans = min(ans, p)

print(ans)