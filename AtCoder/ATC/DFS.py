# 知らずのうちにBFSになっていた

H, W = map(int, input().split()) # 横に2個
path = [[False for _ in range(W)] for _ in range(H)]
visited = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j, l in enumerate(list(input())):
        if l == 's':
            start = [i, j]
            visited[i][j] = True
        elif l == 'g':
            goal = [i, j]
        elif l == '.':
            path[i][j] = True

q = [start]

ans = 'No'
while q:
    qq = []
    for p in q:
        i = p[0]
        j = p[1]
        visited[i][j] = True
        nexts = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
        for next in nexts:
            ni = next[0]
            nj = next[1]
            if 0 <= ni <= H-1 and 0 <= nj <= W-1:
                if path[ni][nj] and not visited[ni][nj]:
                    qq.append(next)
                elif next == goal:
                    ans = 'Yes'
    q = qq

print(ans)