N, M, Q = map(int, input().split()) # 横に2個

L = [0 for _ in range(N)]
R = [0 for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    L[l-1] += 1
    R[r-1] += 1

PQs = [list(map(int, input().split())) for _ in range(Q)]

Ls = [L[0]]
Rs = [R[0]]
for i in range(1, N):
    Ls.append(Ls[-1] + L[i])
    Rs.append(Rs[-1] + R[i])

print(Ls, Rs)
for i, (p, q) in enumerate(PQs):
    start = Ls[q-1] - Ls[p-1]
    end = Rs[q-1] - Rs[p-1]
    print(end-start)

