H, W = map(int, input().split())
state = [[1 if a == '#' else 0 for a in list(input()+'.')] for _ in range(H)]
state.extend([[0]*(W+1)])


ans = 'Yes'
for h in range(H):
    for w in range(W):
        if state[h][w] == 0:
            continue
        nexts = [[h+1, w], [h-1, w], [h, w+1], [h, w-1]]
        ok = False
        for n in nexts:
            if state[n[0]][n[1]] == 1:
                ok = True
        if not ok:
            ans = 'No'
            break
    if ans == 'No':
        break

print(ans)
