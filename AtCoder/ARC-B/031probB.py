A = [[1 if a == 'o' else 0 for a in list(input())] for _ in range(10)]
su = 0
for a in A:
    su += sum(a)

def dfs(p, checked, k):
    x, y = p
    checked[x][y] = True
    k += 1
    nears = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for near in nears:
        nx, ny = near
        if not 0 <= nx <= 9 or not 0 <= ny <= 9:
            continue
        if checked[nx][ny] or A[nx][ny] == 0:
            continue
        k = dfs(near, checked, k)
    return k


ans = 'NO'
for i in range(10):
    for j in range(10):
        checked = [[False for _ in range(10)] for _ in range(10)]
        K = dfs((i, j), checked, 0)
        l = 0 if A[i][j] == 1 else 1
        if K == su+l:
            ans = 'YES'
            break
        
print(ans)
