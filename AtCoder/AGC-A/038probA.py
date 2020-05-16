H, W, A, B = map(int, input().split())

for h in range(H):
    S = ''
    for w in range(W):
        if (h < B and w < A) or (h >= B and w >= A):
            S += '1'
        else:
            S += '0'
    print(S)