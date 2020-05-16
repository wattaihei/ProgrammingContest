import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Edges = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]


def dfs(maxd, L, ans):
    if len(L) == N:
        dominos = [set() for _ in range(7)]
        score = 0
        for a, b in Edges:
            ca, cb = L[a], L[b]
            if ca in dominos[cb]:
                continue
            dominos[ca].add(cb)
            dominos[cb].add(ca)
            score += 1
        #print(L, score)
        return max(score, ans)
    for l in range(maxd+2):
        if l == 6: continue
        ans = dfs(max(maxd,l), L+[l], ans)
    return ans

print(dfs(-1, [], -2))