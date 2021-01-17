import sys
input = sys.stdin.buffer.readline

N, Q = map(int, input().rstrip().split())
H = list(map(int, input().rstrip().split()))

dics = [{}, {}]
Ds = []
for i in range(N-1):
    d = H[i+1] - H[i]
    dics[i%2][d] = dics[i%2].get(d, 0) + 1
    Ds.append(d)

U = [0, 0]
for _ in range(Q):
    query = list(map(int, input().rstrip().split()))
    if query[0] == 1:
        v = query[1]
        U[0] += v
    elif query[0] == 2:
        v = query[1]
        U[1] += v
    else:
        u = query[1]-1; h = query[2]
        if u > 0:
            d0 = Ds[u-1]
            dics[(u%2)^1][d0] -= 1
            dics[(u%2)^1][d0+h] = dics[(u%2)^1].get(d0+h, 0) + 1
            Ds[u-1] = d0 + h
        if u < N-1:
            d1 = Ds[u]
            dics[u%2][d1] -= 1
            dics[u%2][d1-h] = dics[u%2].get(d1-h, 0) + 1
            Ds[u] = d1 - h
    
    s1 = dics[1].get(U[1]-U[0], 0)
    s2 = dics[0].get(U[0]-U[1], 0)
    print(s1 + s2)