import sys
input = sys.stdin.readline

H, W = map(int, input().split())
state = [list(input()) for _ in range(H)]

ans = 0
for h in range(H-1):
    for w in range(W):
        if state[h+1][w] == "." and state[h][w] == ".":
            ans += 1

for w in range(W-1):
    for h in range(H):
        if state[h][w] == "." and state[h][w+1] == ".":
            ans += 1
print(ans)