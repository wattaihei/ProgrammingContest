H, W = map(int, input().split())
state = [[1 if a == 'o' else 0 for a in list(input())] for _ in range(H)]

for h in range(H):
    for w in range(W):
        if state[]