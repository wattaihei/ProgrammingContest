N, K = map(int, input().split())
L = (N-1)*(N-2)//2

if K > L:
    print(-1)
else:
    Ms = []
    for i in range(2, N+1):
        Ms.append((1, i))
    c = L
    for i in range(2, N):
        if c <= K:
            break
        for j in range(i+1, N+1):
            Ms.append((i, j))
            c -= 1
            if c <= K:
                break

    print(len(Ms))
    for u, v in Ms:
        print(u, v)