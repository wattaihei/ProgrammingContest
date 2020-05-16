H, W = map(int, input().split()) # 横に2個
path = [[False for _ in range(W+1)] for _ in range(H+1)]
visited = [[False for _ in range(W+1)] for _ in range(H+1)]
for i in range(H):
    for j, l in enumerate(list(input())):
        if l == 's':
            start = [i, j]
            visited[i][j] = True
        elif l == 'g':
            goal = [i, j]
            path[i][j] = True
        elif l == '.':
            path[i][j] = True

stack = [start]

ans = 'No'
while stack:
    now = stack[-1]
    if now == goal:
        ans = 'Yes'
        break
    i = now[0]
    j = now[1]
    visited[i][j] = True
    nexts = [[i, j+1], [i, j-1], [i+1, j], [i-1, j]]
    for next in nexts:
        ni = next[0]
        nj = next[1]
        if path[ni][nj] and not visited[ni][nj]:
            stack.append(next)
            break
    if now == stack[-1]:
        stack.pop()

print(ans)