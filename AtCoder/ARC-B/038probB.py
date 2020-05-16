H, W = map(int, input().split())
state = [list(input()) for _ in range(H)]

result = [[1 for _ in range(W+1)] for _ in range(H+1)]
for h in reversed(range(H)):
    for w in reversed(range(W)):
        if state[h][w] == "#": continue
        if result[h+1][w] and result[h][w+1] and result[h+1][w+1]:
            result[h][w] = 0

ans = "First" if result[0][0] else "Second"
print(ans)