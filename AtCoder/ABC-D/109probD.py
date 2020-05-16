H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

B = []
for h in range(H):
    for w in range(W):
        if A[h][w] % 2 == 1:
            if w == W-1:
                if h != H-1:
                    B.append((h, w, h+1, w))
                    A[h+1][w] += 1
            else:
                B.append((h, w, h, w+1))
                A[h][w+1] += 1
print(len(B))
for b in B:
    print(' '.join([str(q+1) for q in b]))