import sys
input = sys.stdin.readline

N, M, H, K = map(int, input().split())
Score_before = [int(input()) for _ in range(N)]
Lnk = [[] for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    Lnk[b].append(a-1)

Loc = [i for i in range(N)]
Swaps = []
for h in range(H+1):
    for a in Lnk[h]:
        x, y = Loc[a], Loc[a+1]
        if x < K and K <= y:
            Swaps.append((x, y))
        if y < K and K <= x:
            Swaps.append((y, x))
        Loc[a] = y; Loc[a+1] = x

Score = [0]*N
for l, s in zip(Loc, Score_before):
    Score[l] = s

basic = 0
for i in range(K):
    basic += Score[i]

ans = basic
for x, y in Swaps:
    ans = min(ans, basic - Score[x] + Score[y])

print(ans)