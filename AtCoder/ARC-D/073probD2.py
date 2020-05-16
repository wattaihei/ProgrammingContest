N, W = map(int, input().split())

V = [[] for _ in range(4)]
for i in range(N):
    w, v = map(int, input().split())
    if i == 0:
        w0 = w
        V[0].append(v)
    else:
        V[w-w0].append(v)
J = []
for i in range(4):
    F = sorted(V[i], reverse=True)
    G = [0]
    for f in F:
        G.append(f+G[-1])
    J.append(G)

ans = 0
for s0 in range(len(J[0])):
    for s1 in range(len(J[1])):
        for s2 in range(len(J[2])):
            for s3 in range(len(J[3])):
                if s0*w0 + s1*(w0+1) + s2*(w0+2) + s3*(w0+3) > W:
                    continue
                ans = max(ans, J[0][s0]+J[1][s1]+J[2][s2]+J[3][s3])
print(ans)