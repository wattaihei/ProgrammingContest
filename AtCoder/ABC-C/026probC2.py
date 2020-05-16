N = int(input())
A = [[] for _ in range(N)]
for i in range(1, N):
    a = int(input())
    A[a-1].append(i)

checked = [False for _ in range(N)]
def dfs(p, checked):
    checked[p] = True
    gains = []
    for q in A[p]:
        if not checked[q]:
            gains.append(dfs(q, checked))
    if not gains:
        return 1
    return min(gains) + max(gains) + 1
ans = dfs(0, checked)
print(ans)