H, W = map(int, input().split())
S = [[0 if a == '.' else '#' for a in list(input()) ]for _ in range(H)]

for h in range(H):
    S[h].extend([0])
S.append([0 for _ in range(W+1)])

for h in range(H):
    for w in range(W):
        if S[h][w] == 0:
            near = [(h-1, w-1), (h, w-1), (h+1, w-1), (h-1, w), (h+1, w), (h-1, w+1), (h, w+1), (h+1, w+1)]
            for nh, nw in near:
                if S[nh][nw] == '#':
                    S[h][w] += 1
for h in range(H):
    print(''.join([str(a) for a in S[h][:-1]]))