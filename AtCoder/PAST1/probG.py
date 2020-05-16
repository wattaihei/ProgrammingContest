N = int(input())
score = [[0] + list(map(int, input().split())) for _ in range(N-1)]

Lists1 = []
def dfs1(p, L):
    if p == N:
        Lists1.append(L)
        return
    dfs1(p+1, L+[0])
    dfs1(p+1, L+[1])
    dfs1(p+1, L+[2])
    return

dfs1(0, [])

ans = -10**14
for List in Lists1:
    Groups = [[] for _ in range(3)]
    for n in range(N):
        Groups[List[n]].append(n)
    s = 0
    for group in Groups:
        l = len(group)
        for l1, n1 in enumerate(group):
            for l2 in range(l1+1, l):
                n2 = group[l2]
                s += score[n1][n2-n1]
    if s > ans:
        ans = s

print(ans)
